import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class FirstMainWindow(QMainWindow):
    def __init__(self):
        super(FirstMainWindow,self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")
        # 设置窗口的尺寸
        self.resize(400, 300)
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的信息', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./image/icon.ico'))
    main = FirstMainWindow()
    main.show()
    sys.exit(app.exec_())