import sys
import time
from PyQt5.QtWidgets import QFileDialog, QPushButton, QHBoxLayout,QVBoxLayout, QLabel, QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt
from PyQt5 import uic
import cv2
import qimage2ndarray
import numpy as np

class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        # 动态加载ui
        self.ui = uic.loadUi("ui/window.ui")
        self.ui.openfile_btn.clicked.connect(self.openfile)
        self.ui.openvideo_btn.clicked.connect(self.videoprocessing)
        self.ui.savefile_btn.clicked.connect(self.saveSlot)
        self.ui.process_btn.clicked.connect(self.blur)

    # 打开图片
    def openfile(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, 'Open file', '')
        if imgName:
            self.img = cv2.imread(imgName)
            print(self.img.shape)    # 一直报错
            # self.refeshShow()

            # 固定大小显示
            self.ui.showlabel.setPixmap(QPixmap(imgName).scaled(self.ui.showlabel.width(), self.ui.showlabel.height(), Qt.KeepAspectRatio))
            # 跟随图片原始大小
            # self.ui.showlabel.resize(self.img.shape[1], self.img.shape[0])
            # self.ui.showlabel.setPixmap(QPixmap(imgName))

    def saveSlot(self):
        # 调用存储文件dialog
        fileName, tmp = QFileDialog.getSaveFileName(
            self, 'Save Image', './__data', '*.png *.jpg *.bmp', '*.png')

        if fileName == '':
            return
        if self.img.size == 1:
            return

        # 调用opencv写入图像
        cv2.imwrite(fileName, self.img)

    # ...完善
    def refreshShow(self):
        # 提取图像的尺寸和通道, 用于将opencv下的image转换成Qimage
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()
        # 将Qimage显示出来
        self.ui.showlabel.setPixmap(QPixmap.fromImage(self.qImg).scaled(self.ui.showlabel.width(), self.ui.showlabel.height(), Qt.KeepAspectRatio))


    # 打开视频
    def setImage(self, image):
        self.ui.showlabel.setPixmap(QPixmap.fromImage(image))

    def videoprocessing(self):
        global videoName
        videoName, videoType = QFileDialog.getOpenFileName(self, 'open videofile', '')
        print(videoName)
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()


    def blur(self):
        if self.img.size == 1:
            return

        # 对图像做模糊处理, 窗口设定为5x5
        self.img = cv2.blur(self.img, (20, 20))

        self.refreshShow()

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



if __name__=="__main__":
    app=QApplication(sys.argv)
    window = mainwindow()
    window.ui.show()
    sys.exit(app.exec_())
