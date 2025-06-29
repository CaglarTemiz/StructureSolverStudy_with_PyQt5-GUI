import numpy as np
from ShowResults import ShowResults


class FrameSolver:
    def __init__(self, model_data):
        self.model = model_data
        self.num_eq = 0
        self.E = None  # Equation numbering
        self.K_global = None
        self.F_global = None
        self.displacements = None

    def solve(self):
        self._number_equations()
        self._assemble_global_stiffness()
        self._assemble_global_load_vector()
        self._solve_displacements()
        self._compute_element_end_forces()

        self.results_window = ShowResults(
                                            self.model,
                                            displacements=self.displacements,
                                            eq_matrix=self.E,
                                            coords=self.model.node_coordinates,
                                            elements=self.model.element_connectivity,
                                            element_end_forces = self.element_end_forces
                                         )
        self.results_window.show()

    def _number_equations(self):
        node_count = self.model.node_coordinates.shape[0]
        self.E = np.zeros((node_count, 3), dtype=int)

        for i in range(self.model.support_conditions.shape[0]):
            node_id = int(self.model.support_conditions[i, 0]) - 1
            self.E[node_id] = self.model.support_conditions[i, 1:]

        eq_num = 1
        for i in range(node_count):
            for j in range(3):  # x, y, rotation
                if self.E[i, j] == 0:
                    self.E[i, j] = eq_num
                    eq_num += 1
                else:
                    self.E[i, j] = 0
        self.num_eq = eq_num - 1

        print("Equation numbering (E):\n", self.E)
        print("Number of equations (num_eq):", self.num_eq)

    def _assemble_global_stiffness(self):
        self.K_global = np.zeros((self.num_eq, self.num_eq))

        rowConnectivity = self.model.element_connectivity.shape[0]

        for row in range(rowConnectivity):
            n1, n2 = self.model.element_connectivity[row, 0] - 1, self.model.element_connectivity[row, 1] - 1
            x1, y1 = self.model.node_coordinates[n1]
            x2, y2 = self.model.node_coordinates[n2]

            A, I, E = self.model.element_properties[row]

            print(f"Processing element {row+1}: Nodes {n1+1}-{n2+1}, Coordinates ({x1}, {y1}) to ({x2}, {y2}), Properties (A={A}, I={I}, E={E})")

            L = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            c = (x2 - x1) / L
            s = (y2 - y1) / L

            # Transformation matrix T and local k
            k_local = self._element_stiffness_matrix(E, A, I, L)
            print(f"Element {n1+1}-{n2+1} local stiffness matrix:\n", k_local)
            T = self._transformation_matrix(c, s)
            k_global = T.T @ k_local @ T

            
            # Global DOF indices
            dof_indices = self._get_global_dof_indices(n1, n2)

            # Assemble into K_global
            for i in range(6):
                for j in range(6):
                    if dof_indices[i] != 0 and dof_indices[j] != 0:
                        self.K_global[dof_indices[i]-1, dof_indices[j]-1] += k_global[i, j]

        print("Global stiffness matrix (K_global):\n", self.K_global)

    def _assemble_global_load_vector(self):
        self.F_global = np.zeros((self.num_eq, 1))

        for force in self.model.force_conditions:
            node = int(force[0]) - 1
            for i in range(3):  # Fx, Fy, M
                dof = self.E[node, i]
                if dof != 0:
                    self.F_global[dof - 1] += force[i + 1]
        
        print("Global load vector (F_global):\n", self.F_global)

    def _solve_displacements(self):
        self.displacements = np.linalg.solve(self.K_global, self.F_global)
        print("Displacements:\n", self.displacements)

    def _get_global_dof_indices(self, n1, n2):
        return [
            self.E[n1, 0], self.E[n1, 1], self.E[n1, 2],
            self.E[n2, 0], self.E[n2, 1], self.E[n2, 2]
        ]

    def _transformation_matrix(self, c, s):
        T = np.zeros((6, 6))
        T[0, 0] = T[3, 3] = c
        T[0, 1] = T[3, 4] = s
        T[1, 0] = T[4, 3] = -s
        T[1, 1] = T[4, 4] = c
        T[2, 2] = T[5, 5] = 1
        return T

    def _element_stiffness_matrix(self, E, A, I, L):
        EA_L = E * A / L
        EI_L2 = E * I / L**2
        EI_L3 = E * I / L**3

        k = np.array([
            [ EA_L,      0,           0,     -EA_L,      0,           0],
            [ 0,      12*EI_L3,   6*EI_L2,     0,   -12*EI_L3,   6*EI_L2],
            [ 0,      6*EI_L2,    4*E*I/L,     0,   -6*EI_L2,    2*E*I/L],
            [-EA_L,     0,           0,      EA_L,      0,           0],
            [ 0,     -12*EI_L3,  -6*EI_L2,     0,    12*EI_L3,  -6*EI_L2],
            [ 0,      6*EI_L2,    2*E*I/L,     0,   -6*EI_L2,    4*E*I/L]
        ])
        return k
    
    # Define the function to be used in FrameSolver for post-processing member end forces

    def _compute_element_end_forces(self):
        """
        Computes local member end forces for all elements in the structure.
        Assumes self.displacements contains global DOFs per node: [ux, uy, rz]
        Assumes self.model_data has node_coordinates, element_connectivity, and material_props
        Returns a list of local force vectors for each element.
        """
        self.element_end_forces = {}
        coords = self.model.node_coordinates
        connectivity = self.model.element_connectivity
        materials = self.model.element_properties  # [A, I, E] per element
        eq_matrix = self.E  # Equation numbering matrix
        disps = np.zeros((self.model.node_coordinates.shape[0], 3))

        for i in range(self.model.node_coordinates.shape[0]):
            for j in range(3):
                eq = eq_matrix[i, j]
                if eq > 0:
                    disps[i,j] = self.displacements[eq - 1][0]
                else:
                    disps[i,j] = 0.0

        print("Displacements for each node:\n", disps)

        for i, (n1, n2) in enumerate(connectivity):
            n1 -= 1  # zero-based
            n2 -= 1

            x1, y1 = coords[n1]
            x2, y2 = coords[n2]
            ux1, uy1, rz1 = disps[n1]
            ux2, uy2, rz2 = disps[n2]
            d_global = np.array([ux1, uy1, rz1, ux2, uy2, rz2])

            A, I, E = materials[i]
            L = np.hypot(x2 - x1, y2 - y1)
            c = (x2 - x1) / L
            s = (y2 - y1) / L

            # Rotation matrix R (6x6)
            R = np.array([
                [ c,  s, 0,  0,  0, 0],
                [-s,  c, 0,  0,  0, 0],
                [ 0,  0, 1,  0,  0, 0],
                [ 0,  0, 0,  c,  s, 0],
                [ 0,  0, 0, -s,  c, 0],
                [ 0,  0, 0,  0,  0, 1]
            ])

            # Local displacement vector
            d_local = R @ d_global

            # Local stiffness matrix k'
            k_local = np.array([
                [ A*E/L,        0,          0,        -A*E/L,        0,          0],
                [ 0,     12*E*I/L**3,  6*E*I/L**2,     0, -12*E*I/L**3,  6*E*I/L**2],
                [ 0,     6*E*I/L**2,   4*E*I/L,        0, -6*E*I/L**2,   2*E*I/L],
                [-A*E/L,        0,          0,         A*E/L,        0,          0],
                [ 0, -12*E*I/L**3, -6*E*I/L**2,        0,  12*E*I/L**3, -6*E*I/L**2],
                [ 0,     6*E*I/L**2,   2*E*I/L,        0, -6*E*I/L**2,   4*E*I/L]
            ])

            # Local force vector
            f_local = k_local @ d_local
            self.element_end_forces[f"Element {i+1}"] = f_local

            print(f"Element {i+1} local end forces:\n", f_local)
         


