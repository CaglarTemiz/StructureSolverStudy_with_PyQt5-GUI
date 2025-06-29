import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from MenuWindow import Ui_MenuWindow

# Import the two new windows
from PreFrameProperties import PreFrameProperties


class MainApp(QMainWindow):
    def __init__(self):
        # Initialize the main application window as a QMainWindow in Qt
        super().__init__()
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)

        # Sub-windows
        self.frame_window = None
        self.fem_window = None

        self.ui.button_StiffnessFrameSolver.clicked.connect(self.open_frame_calculator)
        self.ui.button_FiniteElementSolver.clicked.connect(self.open_fem_calculator)
        self.ui.button_Exit.clicked.connect(self.close)

    def open_frame_calculator(self):
        if self.frame_window is None:
            self.frame_window = PreFrameProperties()
        self.frame_window.show()


    # Since the FEM calculator is still under development, the message box will shown to user.
    # In future, this method will be replaced with the actual FEM calculator window.
    def open_fem_calculator(self):

        QMessageBox.information(
        self, "FEM Feature Under Development", "Dear User!\nFEM Calculator is still developing to give you" \
        " accurate and efficient results. Please stay tuned for upcoming updates. ", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
