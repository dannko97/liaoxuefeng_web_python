import easy_test
import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication

from python_github.pyqt.designer.easy_test import Ui_MainWindow


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.myprint)

    def myprint(self):
        self.ui.textBrowser.append('我喜欢你')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
