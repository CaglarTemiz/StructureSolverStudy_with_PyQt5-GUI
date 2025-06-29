from PyQt5.QtWidgets import QWidget, QVBoxLayout
from MainFramePropertiesWindow import Ui_Form_MainPropertiesWindow
from FrameModelData import FrameModelData
from FrameSolver import FrameSolver

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.patches import Arc



class MainFrameProperties(QWidget):
    def __init__(self, model_data: FrameModelData):
        super().__init__()
        self.ui = Ui_Form_MainPropertiesWindow()
        self.ui.setupUi(self)
        self.model_data = model_data

        #Set the table properties for the model data
        self.model_data.setNodeTable(self.ui.table_NodeProperties)
        self.model_data.setElementTable(self.ui.table_ElementProperties)
        self.model_data.setSupportTable(self.ui.table_SupportProperties)
        self.model_data.setForceTable(self.ui.table_ForceProperties)

        self.ui.button_Draw.clicked.connect(self.handle_draw)

        self.solver = FrameSolver(model_data)
        
        self.ui.button_RunSolver.clicked.connect(self.solver.solve)

        
    
    def handle_draw(self):
        self.model_data.setNodeMatrixFromNodeTable(self.ui.table_NodeProperties, self)
        self.model_data.setElementConnectivityFromTable(self.ui.table_ElementProperties, self)
        self.model_data.setElementPropertiesFromTable(self.ui.table_ElementProperties, self)
        self.model_data.setSupportConditionsFromTable(self.ui.table_SupportProperties, self)
        self.model_data.setForceConditionsFromTable(self.ui.table_ForceProperties, self)

        print("Node Coordinates:")
        print(self.model_data.node_coordinates)

        print("Element Connectivity:")
        print(self.model_data.element_connectivity)

        print("Element Properties:")
        print(self.model_data.element_properties)

        print("Support Conditions:")
        print(self.model_data.support_conditions)

        print("Force Conditions:")
        print(self.model_data.force_conditions)

        self.draw_model()

    def draw_model(self):
        model_data = self.model_data
        XY = model_data.node_coordinates
        C = model_data.element_connectivity
        S = model_data.support_conditions
        F = model_data.force_conditions

        fig = Figure()
        ax = fig.add_subplot(111)
        ax.set_aspect('equal')
        ax.axis('off')

        # === Draw Elements ===
        for i in range(C.shape[0]):
            n1, n2 = int(C[i, 0]) - 1, int(C[i, 1]) - 1
            x1, y1 = XY[n1]
            x2, y2 = XY[n2]
            ax.plot([x1, x2], [y1, y2], color='black', linewidth=2)

        # === Draw Supports ===
        support_markers = {
            (0, 0, 0): None,
            (1, 0, 0): 'o',     # Roller support (fixed in X)
            (0, 1, 0): 'o',     # Roller support (fixed in X)
            (1, 1, 0): '^',     # Pinned
            (1, 1, 1): 's',     # Fully fixed
        }

        for i in range(S.shape[0]):
            nid = int(S[i, 0]) - 1
            x, y = XY[nid]
            code = tuple(S[i, 1:4].astype(int))
            marker = support_markers.get(code, 'd')
            if marker:
                ax.scatter(x, y, s=150, c='red', marker=marker)

        # === Draw Forces ===
        scale = 0.1
        for i in range(F.shape[0]):
            nid = int(F[i, 0]) - 1
            x, y = XY[nid]
            fx = float(F[i, 1])
            fy = float(F[i, 2])
            mz = float(F[i, 3]) if F.shape[1] > 3 else 0

            if fx != 0:
                ax.arrow(x, y, fx * scale, 0,
                        head_width=0.07, head_length=0.07, linewidth=2,
                        length_includes_head=True, color='blue')
                ax.text(x + fx * scale * 1.1, y, f"Fx={fx:.1f}", fontsize=9, fontweight='bold', color='blue')

            if fy != 0:
                ax.arrow(x, y, 0, fy * scale,
                        head_width=0.07, head_length=0.07, linewidth=2,
                        length_includes_head=True, color='blue')
                ax.text(x, y + fy * scale * 1.1, f"Fy={fy:.1f}", fontsize=9, fontweight='bold', color='blue')

            if mz != 0:
                angle = 270 
                arc = Arc((x, y), 0.4, 0.4, theta1=0, theta2=angle,
                        color='green', linewidth=3)
                ax.add_patch(arc)
                # Add an arrowhead to indicate direction
                direction = 1 if mz > 0 else -1
                dx = 0.1 * direction
                dy = -0.1
                ax.text(x + 0.2 * direction, y + 0.2, f"M={mz:.1f}", fontsize=8, color='green')

        # === Add node labels ===
        for i, (x, y) in enumerate(XY):
            ax.text(x + 0.05, y + 0.05, f"N{i+1}", color='black', fontsize=8)

        # === Display on Qt Widget ===
        area = self.ui.widget_DrawingArea  # updated widget name
        layout = area.layout()
        if layout is None:
            layout = QVBoxLayout(area)
            area.setLayout(layout)
        else:
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

        canvas = FigureCanvas(fig)
        toolbar = NavigationToolbar(canvas, self)

        layout.addWidget(toolbar)
        layout.addWidget(canvas)