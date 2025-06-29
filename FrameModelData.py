from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
import numpy as np

class FrameModelData:

    node_coordinates = np.array([])  # Placeholder for node coordinates
    element_connectivity = np.array([])  # Placeholder for element connectivity
    support_conditions = np.array([])  # Placeholder for support conditions
    force_conditions = np.array([])  # Placeholder for force conditions


    def __init__(self, node_count=0, element_count=0, support_count=0, force_count=0):
        # Metadata
        self.node_count = node_count
        self.element_count = element_count
        self.support_count = support_count
        self.force_count = force_count

        print(f"Initializing FrameModelData with {node_count} nodes, {element_count} elements, "
              f"{support_count} supports, and {force_count} forces.")

    
    def setNodeTable(self, tableWidget):
        # This method will be used to set the node table in the UI
        if self.node_count > 1:
            tableWidget.setRowCount(self.node_count)

            for i in range(self.node_count):

                # Node ID (non-editable, center-aligned)
                node_item = QTableWidgetItem(str(i + 1))
                node_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                node_item.setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(i, 0, node_item)

                # X coordinate (editable, center-aligned)
                x_item = QTableWidgetItem("")
                x_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                x_item.setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(i, 1, x_item)

                # Y coordinate (editable, center-aligned)
                y_item = QTableWidgetItem("")
                y_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                y_item.setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(i, 2, y_item)


            return tableWidget
        
        else:
            # Error handling purposes
            return None


    def setElementTable(self, tableWidget):

        # This method will be used to set the element table in the UI

        if self.element_count > 0:

            tableWidget.setRowCount(self.element_count)

            for i in range(self.element_count):

                # Element ID (non-editable, center-aligned)
                element_item = QTableWidgetItem(str(i + 1))
                element_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                element_item.setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(i, 0, element_item)

                # Start Node (editable, center-aligned)
                start_node_item = QTableWidgetItem("")
                start_node_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                start_node_item.setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(i, 1, start_node_item)

                # End Node (editable, center-aligned)
                end_node_item = QTableWidgetItem("")
                end_node_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                end_node_item.setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(i, 2, end_node_item)

            return tableWidget
        
        else:
            # Error handling purposes
            return None
    
    def setSupportTable(self, tableWidget):
        
        if self.support_count > 0:
            tableWidget.setRowCount(self.force_count)

            for i in range(self.support_count):
                # Editable Node ID (center-aligned)
                node_item = QTableWidgetItem("")
                node_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                node_item.setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(i, 0, node_item)

                # Columns 1–3: Checkboxes
                for j in range(1, 4):
                    check_item = QTableWidgetItem()
                    check_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    check_item.setCheckState(Qt.Unchecked)
                    check_item.setTextAlignment(Qt.AlignCenter)
                    tableWidget.setItem(i, j, check_item)

            return tableWidget
        
        else:
            # Error handling purposes
            return None
        

    def setForceTable(self, tableWidget):
        # This method will be used to set the force table in the UI
        if self.force_count > 0:
            tableWidget.setRowCount(self.force_count)

            for i in range(self.force_count):
                # Node ID (editable, center-aligned)
                node_item = QTableWidgetItem("")
                node_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
                node_item.setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(i, 0, node_item)

                # Force X (editable, center-aligned)
                fx_item = QTableWidgetItem("")
                fx_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                fx_item.setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(i, 1, fx_item)

                # Force Y (editable, center-aligned)
                fy_item = QTableWidgetItem("")
                fy_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                fy_item.setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(i, 2, fy_item)

                # Moment Z (editable, center-aligned)
                mz_item = QTableWidgetItem("")
                mz_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                mz_item.setTextAlignment(Qt.AlignCenter)
                tableWidget.setItem(i, 3, mz_item)

            return tableWidget
        
        else:
            # Error handling purposes
            return None
        
    def setNodeMatrixFromNodeTable(self, node_table, parent=None):

        self.node_coordinates = np.zeros((self.node_count, 2))
        
        for i in range(self.node_count):
            try:
                x = float(node_table.item(i, 1).text())
                y = float(node_table.item(i, 2).text())
                self.node_coordinates[i] = [x, y]
            except (AttributeError, ValueError):
                QMessageBox.critical(parent, "Error", f"Invalid or missing value at row {i} of node table")


    def setElementConnectivityFromTable(self, table_widget, parent=None):

        self.element_connectivity = np.zeros((self.element_count, 2), dtype=int)

        for i in range(self.element_count):
            try:
                start_node = int(table_widget.item(i, 1).text())
                end_node = int(table_widget.item(i, 2).text())
                self.element_connectivity[i] = [start_node, end_node]
            except (AttributeError, ValueError):
                QMessageBox.critical(parent, "Error" ,f"Invalid or missing value at row {i} of element table")

    def setElementPropertiesFromTable(self, table_widget, parent=None):

        self.element_properties = np.zeros((self.element_count, 3), dtype=float)

        for i in range(self.element_count):
            try:
                area = float(table_widget.item(i, 3).text())
                inertia = float(table_widget.item(i, 4).text())
                elastic_modulus = float(table_widget.item(i, 5).text())
                self.element_properties[i] = [area, inertia, elastic_modulus]
            except (AttributeError, ValueError):
                QMessageBox.critical(parent, "Error" ,f"Invalid or missing value at row {i} of element table")

    
    def setSupportConditionsFromTable(self, table_widget, parent=None):
        self.support_conditions = np.zeros((self.support_count, 4), dtype=int)

        for i in range(self.support_count):
            try:
                node_id = int(table_widget.item(i, 0).text())
                support_x = table_widget.item(i, 1).checkState() == Qt.Checked
                support_y = table_widget.item(i, 2).checkState() == Qt.Checked
                support_mz = table_widget.item(i, 3).checkState() == Qt.Checked

                self.support_conditions[i] = [node_id, int(support_x), int(support_y), int(support_mz)]
            except (AttributeError, ValueError):
                QMessageBox.critical(parent, "Error", f"Invalid or missing value at row {i} of support table")

    
    def setForceConditionsFromTable(self, table_widget, parent=None):
        self.force_conditions = np.zeros((self.force_count, 4))

        for i in range(self.force_count,):
            try:
                node_id = int(table_widget.item(i, 0).text())
                fx = float(table_widget.item(i, 1).text())
                fy = float(table_widget.item(i, 2).text())
                mz = float(table_widget.item(i, 3).text())

                self.force_conditions[i] = [node_id, fx, fy, mz]
            except (AttributeError, ValueError):
                QMessageBox.critical(parent, "Error", f"Invalid or missing value at row {i} of force table")

            


