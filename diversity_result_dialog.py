from qgis.PyQt.QtWidgets import *
from .diversity_result_dialog_ui import Ui_dlgResult

class DlgResult(QDialog, Ui_dlgResult):
    def __init__(self):
        super(DlgResult, self).__init__()
        self.setupUi(self)


        self.setLayout(self.lytMain)
        self.trwResults.setColumnWidth(0, 230)
        self.trwResults.setColumnWidth(1, 80)
        self.trwResults.setColumnWidth(2, 80)
        self.trwResults.setColumnWidth(3, 80)
        self.trwResults.setColumnWidth(4, 80)
        self.trwResults.setColumnWidth(5, 80)
