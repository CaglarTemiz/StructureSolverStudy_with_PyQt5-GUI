# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ResultsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Results(object):
    def setupUi(self, Form_Results):
        Form_Results.setObjectName("Form_Results")
        Form_Results.resize(697, 576)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_Results)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs_Results = QtWidgets.QTabWidget(Form_Results)
        self.tabs_Results.setEnabled(True)
        self.tabs_Results.setObjectName("tabs_Results")
        self.tab_Displacements = QtWidgets.QWidget()
        self.tab_Displacements.setObjectName("tab_Displacements")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_Displacements)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.table_displacements = QtWidgets.QTableWidget(self.tab_Displacements)
        self.table_displacements.setObjectName("table_displacements")
        self.table_displacements.setColumnCount(0)
        self.table_displacements.setRowCount(0)
        self.horizontalLayout.addWidget(self.table_displacements)
        self.tabs_Results.addTab(self.tab_Displacements, "")
        self.tab_Element1 = QtWidgets.QWidget()
        self.tab_Element1.setObjectName("tab_Element1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_Element1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Element = QtWidgets.QLabel(self.tab_Element1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_Element.setFont(font)
        self.label_Element.setObjectName("label_Element")
        self.verticalLayout_2.addWidget(self.label_Element)
        self.label_StartNodeDisp = QtWidgets.QLabel(self.tab_Element1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_StartNodeDisp.setFont(font)
        self.label_StartNodeDisp.setObjectName("label_StartNodeDisp")
        self.verticalLayout_2.addWidget(self.label_StartNodeDisp)
        self.label_EndNodeDisp = QtWidgets.QLabel(self.tab_Element1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_EndNodeDisp.setFont(font)
        self.label_EndNodeDisp.setObjectName("label_EndNodeDisp")
        self.verticalLayout_2.addWidget(self.label_EndNodeDisp)
        self.label_StartNodeFx = QtWidgets.QLabel(self.tab_Element1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_StartNodeFx.setFont(font)
        self.label_StartNodeFx.setObjectName("label_StartNodeFx")
        self.verticalLayout_2.addWidget(self.label_StartNodeFx)
        self.label_StartNodeFy = QtWidgets.QLabel(self.tab_Element1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_StartNodeFy.setFont(font)
        self.label_StartNodeFy.setObjectName("label_StartNodeFy")
        self.verticalLayout_2.addWidget(self.label_StartNodeFy)
        self.label_StartNodeM = QtWidgets.QLabel(self.tab_Element1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_StartNodeM.setFont(font)
        self.label_StartNodeM.setObjectName("label_StartNodeM")
        self.verticalLayout_2.addWidget(self.label_StartNodeM)
        self.label_EndNodeFx = QtWidgets.QLabel(self.tab_Element1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_EndNodeFx.setFont(font)
        self.label_EndNodeFx.setObjectName("label_EndNodeFx")
        self.verticalLayout_2.addWidget(self.label_EndNodeFx)
        self.label_EndNodeFy = QtWidgets.QLabel(self.tab_Element1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_EndNodeFy.setFont(font)
        self.label_EndNodeFy.setObjectName("label_EndNodeFy")
        self.verticalLayout_2.addWidget(self.label_EndNodeFy)
        self.label_EndNodeM = QtWidgets.QLabel(self.tab_Element1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_EndNodeM.setFont(font)
        self.label_EndNodeM.setObjectName("label_EndNodeM")
        self.verticalLayout_2.addWidget(self.label_EndNodeM)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.widget = QtWidgets.QWidget(self.tab_Element1)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3.addWidget(self.widget)
        self.tabs_Results.addTab(self.tab_Element1, "")
        self.verticalLayout.addWidget(self.tabs_Results)

        self.retranslateUi(Form_Results)
        self.tabs_Results.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form_Results)

    def retranslateUi(self, Form_Results):
        _translate = QtCore.QCoreApplication.translate
        Form_Results.setWindowTitle(_translate("Form_Results", "Results"))
        self.tabs_Results.setTabText(self.tabs_Results.indexOf(self.tab_Displacements), _translate("Form_Results", "Displacements"))
        self.label_Element.setText(_translate("Form_Results", "Element 1"))
        self.label_StartNodeDisp.setText(_translate("Form_Results", "Start Node Displacement:"))
        self.label_EndNodeDisp.setText(_translate("Form_Results", "End Node Displacement:"))
        self.label_StartNodeFx.setText(_translate("Form_Results", "Start Node Fx:"))
        self.label_StartNodeFy.setText(_translate("Form_Results", "Start Node Fy:"))
        self.label_StartNodeM.setText(_translate("Form_Results", "Start Node M:"))
        self.label_EndNodeFx.setText(_translate("Form_Results", "End Node Fx:"))
        self.label_EndNodeFy.setText(_translate("Form_Results", "End Node Fy:"))
        self.label_EndNodeM.setText(_translate("Form_Results", "End Node M:"))
        self.tabs_Results.setTabText(self.tabs_Results.indexOf(self.tab_Element1), _translate("Form_Results", "Element 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Results = QtWidgets.QWidget()
    ui = Ui_Form_Results()
    ui.setupUi(Form_Results)
    Form_Results.show()
    sys.exit(app.exec_())
