from ui import Ui_Form
from PyQt5 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
dir = r"E:/paddle_reader/file/test"
ui = Ui_Form(dir)
ui.show()
sys.exit(app.exec_())