
from PyQt5 import QtCore, QtGui, QtWidgets


# click vào volume
class Slider(QtWidgets.QSlider):
    sliderClicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isEnabled() is True:
            x = event.pos().x()
            value = round(
                (
                    self.maximum()
                    - self.minimum()
                )
                * x
                / self.width()
                + self.minimum()
            )
            if 0 <= value < 100:
                self.setValue(value)
                self.sliderClicked.emit()



# click vào volume
class Label(QtWidgets.QLabel):
    labelClicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.labelClicked.emit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(500, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name_song = QtWidgets.QLabel(self.centralwidget)
        self.label_name_song.setGeometry(QtCore.QRect(0, 500, 500, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_name_song.setFont(font)
        self.label_name_song.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "color: rgb(255, 255, 255);")
        self.label_name_song.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_song.setObjectName("label_name_song")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 530, 500, 61))
        self.widget.setStyleSheet("background-color: rgb(71, 64, 64);")
        self.widget.setObjectName("widget")
        self.button_play = QtWidgets.QPushButton(self.widget)
        self.button_play.setGeometry(QtCore.QRect(220, 20, 51, 41))
        self.button_play.setStyleSheet("background-color: rgb(71, 64, 64);")
        self.button_play.setText("")
        self.button_play.setObjectName("button_play")
        self.button_stop = QtWidgets.QPushButton(self.widget)
        self.button_stop.setGeometry(QtCore.QRect(160, 20, 31, 41))
        self.button_stop.setStyleSheet("")
        self.button_stop.setText("")
        self.button_stop.setObjectName("button_stop")
        self.button_open = QtWidgets.QPushButton(self.widget)
        self.button_open.setGeometry(QtCore.QRect(300, 20, 31, 41))
        self.button_open.setStyleSheet("")
        self.button_open.setText("")
        self.button_open.setObjectName("button_open")
        self.label_time_up = QtWidgets.QLabel(self.widget)
        self.label_time_up.setGeometry(QtCore.QRect(10, 30, 31, 16))
        self.label_time_up.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_time_up.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
        )
        self.label_time_up.setObjectName("label_time_up")
        self.label_total_time = QtWidgets.QLabel(self.widget)
        self.label_total_time.setGeometry(QtCore.QRect(60, 30, 31, 16))
        self.label_total_time.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_total_time.setObjectName("label_total_time")
        self.slider_volume = QtWidgets.QSlider(self.widget)
        self.slider_volume.setGeometry(QtCore.QRect(390, 30, 61, 22))
        self.slider_volume.setMaximum(100)
        self.slider_volume.setSingleStep(0)
        self.slider_volume.setPageStep(10)
        self.slider_volume.setProperty("value", 50)
        self.slider_volume.setOrientation(QtCore.Qt.Horizontal)
        self.slider_volume.setInvertedAppearance(False)
        self.slider_volume.setInvertedControls(False)
        self.slider_volume.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slider_volume.setObjectName("slider_volume")
        self.label_vol_value = QtWidgets.QLabel(self.widget)
        self.label_vol_value.setGeometry(QtCore.QRect(460, 30, 21, 21))
        self.label_vol_value.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_vol_value.setObjectName("label_vol_value")
        self.button_next = QtWidgets.QPushButton(self.widget)
        self.button_next.setGeometry(QtCore.QRect(270, 20, 31, 41))
        self.button_next.setStyleSheet("")
        self.button_next.setText("")
        self.button_next.setObjectName("button_next")
        self.button_prev = QtWidgets.QPushButton(self.widget)
        self.button_prev.setGeometry(QtCore.QRect(190, 20, 31, 41))
        self.button_prev.setStyleSheet("")
        self.button_prev.setText("")
        self.button_prev.setObjectName("button_prev")
        self.label_pic_volume = Label(self.widget)
        self.label_pic_volume.setGeometry(QtCore.QRect(350, 30, 25, 25))
        self.label_pic_volume.setObjectName("label_pic_volume")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(50, 30, 47, 13))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_tracklist_info = QtWidgets.QLabel(self.widget)
        self.label_tracklist_info.setGeometry(QtCore.QRect(110, 30, 47, 13))
        self.label_tracklist_info.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_tracklist_info.setText("")
        self.label_tracklist_info.setObjectName("label_tracklist_info")
        self.progress_bar = Slider(self.widget)
        self.progress_bar.setGeometry(QtCore.QRect(10, 5, 481, 12))
        self.progress_bar.setToolTipDuration(-1)
        self.progress_bar.setStyleSheet("image: url(:/stick.png);")
        self.progress_bar.setMaximum(100)
        self.progress_bar.setPageStep(1)
        self.progress_bar.setOrientation(QtCore.Qt.Horizontal)
        self.progress_bar.setInvertedAppearance(False)
        self.progress_bar.setInvertedControls(False)
        self.progress_bar.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.progress_bar.setObjectName("progress_bar")
        self.label_7.raise_()
        self.label_time_up.raise_()
        self.label_total_time.raise_()
        self.slider_volume.raise_()
        self.label_vol_value.raise_()
        self.button_stop.raise_()
        self.button_prev.raise_()
        self.button_play.raise_()
        self.button_next.raise_()
        self.button_open.raise_()
        self.label_pic_volume.raise_()
        self.label_tracklist_info.raise_()
        self.progress_bar.raise_()
        self.label_album_cover = QtWidgets.QLabel(self.centralwidget)
        self.label_album_cover.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.label_album_cover.setObjectName("label_album_cover")
        self.widget.raise_()
        self.label_name_song.raise_()
        self.label_album_cover.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # set text cho các UI
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_name_song.setText(_translate("MainWindow", "TextLabel"))
        self.label_time_up.setText(_translate("MainWindow", "TextLabel"))
        self.label_total_time.setText(_translate("MainWindow", "TextLabel"))
        self.label_vol_value.setText(_translate("MainWindow", "TextLabel"))
        self.label_pic_volume.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "/"))
        self.label_album_cover.setText(_translate("MainWindow", "TextLabel"))
