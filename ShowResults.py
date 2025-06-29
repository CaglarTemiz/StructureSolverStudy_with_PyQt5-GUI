from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from ResultsWindow import Ui_Form_Results
import numpy as np

class ShowResults(QWidget):
    def __init__(self, model, displacements, eq_matrix, coords, elements, element_end_forces):
         super().__init__()
         self.ui = Ui_Form_Results()
         self.ui.setupUi(self)
 
         self.model_data = model
         self.displacements = displacements
         self.eq_matrix = eq_matrix
         self.coords = coords
         self.elements = elements
         self.element_end_forces = element_end_forces
 
         self.populate_displacement_table()
         self.create_element_tabs()

    def populate_displacement_table(self):
        num_nodes = self.eq_matrix.shape[0]
        self.ui.table_displacements.setColumnCount(4)
        self.ui.table_displacements.setRowCount(num_nodes)
        self.ui.table_displacements.setHorizontalHeaderLabels(["Node", "Ux (mm)", "Uy (mm)", "Rz (mrad)"])

        for i in range(num_nodes):
            id_item = QTableWidgetItem(str(i+1))
            id_item.setTextAlignment(QtCore.Qt.AlignCenter)
            id_item.setFlags(id_item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.ui.table_displacements.setItem(i, 0, id_item)

            for j in range(3):
                eq = self.eq_matrix[i, j]
                if eq > 0:
                    val = self.displacements[eq - 1][0]
                    val *= 1000 if j < 2 else 1000  # mm or mrad
                    item = QTableWidgetItem(f"{val:.3f}")
                else:
                    item = QTableWidgetItem("0.000")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.ui.table_displacements.setItem(i, j+1, item)

        self.ui.table_displacements.resizeColumnsToContents()

    def create_element_tabs(self):

        index = self.ui.tabs_Results.indexOf(self.ui.tab_Element1)
        self.ui.tabs_Results.removeTab(index)

        from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

        for i, (n1, n2) in enumerate(self.elements):
            tab = QWidget()
            layout = QHBoxLayout(tab)

            # === Left: Label panel ===
            labels_layout = QVBoxLayout()
            labels = {}

            for key in (["Element", "Start Node Fx", "Start Node Fy", "Start Node M",
                        "End Node Fx", "End Node Fy", "End Node M"]):
                lbl = QLabel(f"{key}:")
                lbl.setObjectName(f"label_{key.replace(' ', '_')}_{i}")
                labels[key] = lbl
                labels_layout.addWidget(lbl)

            # Set values for labels
            labels["Element"].setText(f"Element {i+1}")
            forces = self.element_end_forces[f"Element {i+1}"]
            labels["Start Node Fx"].setText(f"Fx: {forces[0]:.2f} kN")
            labels["Start Node Fy"].setText(f"Fy: {forces[1]:.2f} kN")
            labels["Start Node M"].setText(f"M: {forces[2]:.2f} kNm")
            labels["End Node Fx"].setText(f"Fx: {forces[3]:.2f} kN")
            labels["End Node Fy"].setText(f"Fy: {forces[4]:.2f} kN")
            labels["End Node M"].setText(f"M: {forces[5]:.2f} kNm")

            layout.addLayout(labels_layout)

            # === Right: Drawing area ===
            fig = plt.figure(figsize=(4, 4))
            ax = fig.add_subplot(111)

            # Dummy element line
            x1, y1 = self.coords[n1 - 1]
            x2, y2 = self.coords[n2 - 1]
            ax.plot([x1, x2], [y1, y2], 'k-')
            ax.set_title(f"Element {i+1}")
            ax.axis("equal")

            canvas = FigureCanvas(fig)
            drawing_layout = QVBoxLayout()
            drawing_layout.addWidget(canvas)
            right_widget = QWidget()
            right_widget.setLayout(drawing_layout)

            layout.addWidget(right_widget)

            # Add the tab
            self.ui.tabs_Results.addTab(tab, f"Element {i+1}")