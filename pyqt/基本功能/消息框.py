import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', '你确认退出吗？', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())