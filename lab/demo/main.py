import sys
import time
from PyQt5.QtWidgets import QFileDialog, QPushButton, QHBoxLayout,QVBoxLayout, QLabel, QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt
import cv2


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        hbox.addStretch(1)
        vbox = QVBoxLayout(self)
        vbox.addStretch(1)
        hbox.addLayout(vbox)

        pixmap = QPixmap("girl.png")

        self.image_lbl = QLabel(self)
        self.image_lbl.setGeometry(20, 20, 300, 400)
        self.image_lbl.setPixmap(pixmap.scaled(self.image_lbl.width(), self.image_lbl.height()))



        openfile_lbl = QPushButton('打开文件', self)
        hbox.addWidget(openfile_lbl)
        openfile_lbl.clicked.connect(self.videoprocessing)
        openfile_lbl.move(100, 450)

        self.setLayout(hbox)
        self.setGeometry(500, 400, 500, 500)
        self.move(1000, 200)
        self.setWindowTitle('demo')
        self.show()

    def openfile(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, 'Open file', '')
        print(imgName)  # ('D:/code/github/python_github/毕设/demo/girl.png', 'All Files (*)')
        # 这里截取文件格式来决定怎么操作
        if imgName:
            img = cv2.imread(imgName)
            print(img.shape())
            self.image_lbl.setPixmap(QPixmap(imgName).scaled(self.image_lbl.width(), self.image_lbl.height()))

    def setImage(self, image):
        self.image_lbl.setPixmap(QPixmap.fromImage(image))

    def videoprocessing(self):
        global videoName
        videoName, videoType = QFileDialog.getOpenFileName(self, 'open videofile', '')
        print(videoName)
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()


class Thread(QThread): # 采用线程来播放视频
    changePixmap = pyqtSignal(QImage)
    def run(self):
        cap = cv2.VideoCapture(videoName)
        print(videoName)
        while(cap.isOpened()==True):
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 在这里可以对每帧图像进行处理
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                time.sleep(0.01) # 控制视频播放的速度
            else:
                print('ret error')
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())
