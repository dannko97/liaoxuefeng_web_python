import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('StatusBar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())