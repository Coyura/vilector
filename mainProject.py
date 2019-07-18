import sys
from PySide2.QtWidgets import (QApplication, QWidget)
from PySide2 import QtCore, QtUiTools

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile("vilectorDesign.ui")
        file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(file,self)
        file.close()
        self.ui.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    sys.exit(app.exec_())