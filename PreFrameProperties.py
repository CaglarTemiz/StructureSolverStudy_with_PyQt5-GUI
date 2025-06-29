from PyQt5.QtWidgets import QWidget, QMessageBox
from MainFramePropertiesWindow import Ui_Form_MainPropertiesWindow
from PreFramePropertiesWindow import Ui_Form_PreFrameProperties
from MainFrameProperties import MainFrameProperties

# Import the FrameModelData class
from FrameModelData import FrameModelData

class PreFrameProperties(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_PreFrameProperties()
        self.ui.setupUi(self)

        # Connect the button to open the next window
        self.ui.button_Submit.clicked.connect(self.open_next_window)

    def open_next_window(self):
       
        # Get the values from the spin boxes
        node_count = self.ui.spinBox_NodeCount.value()
        element_count = self.ui.spinBox_ElementCount.value()
        support_count = self.ui.spinBox_SupportCount.value()
        force_count = self.ui.spinBox_NodalForceCount.value()


        # Validate the input values
        if node_count < 2:
            node_error_text = "Invalid Node Count!\n"
        else:
            node_error_text = ""
        
        if element_count < 1:
            element_error_text = "Invalid Element Count!\n"
        else:
            element_error_text = ""
        
        if support_count < 1:
            support_error_text = "Invalid Support Count!\n"
        else:
            support_error_text = ""
        
        if force_count < 1:
            force_error_text = "Invalid Force Count!\n"
        else:
            force_error_text = ""
        
        if node_error_text or element_error_text or support_error_text or force_error_text:
            error_message = "Please correct the following errors:\n"
            error_message += node_error_text + element_error_text + support_error_text + force_error_text
            QMessageBox.critical(self, "Input Error", error_message)
        
        else:

            # If all inputs are valid, create the FrameModelData
            model_data = FrameModelData(node_count, element_count, support_count, force_count)

            self.window2 = MainFrameProperties(model_data)
            self.window2.show()
            self.close()

