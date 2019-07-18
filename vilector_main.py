import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_vilector import Ui_MainWindow
from PySide2.QtCore import QUrl
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pBLecture.clicked.connect(self.lecture)
        self.ui.pBPause.clicked.connect(self.pause)
        self.ui.pBStop.clicked.connect (self.stop)
        self.ui.pBPrecedent.clicked.connect (self.precedent)
        self.ui.pBSuivant.clicked.connect (self.suivant)

        self.ui.dBVolume.valueChanged.connect(self.volume)
        self.ui.dBVolume.setRange(0, 100)
        self.ui.suiviVol.setText(f'{str(self.ui.dBVolume.value())} %')

        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setVideoOutput(self.ui.Lecteur)

        mediaContent = QMediaContent(QUrl.fromLocalFile("big_buck_bunny.avi"))
        self.mediaPlayer.setMedia(mediaContent)

    def lecture(self) :
        print("Lecture")
        self.mediaPlayer.play()


    def pause(self):
        print ("Pause")
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState :
            self.mediaPlayer.pause()
        else :
            self.mediaPlayer.play()

    def stop(self):
        print ("Stop")
        self.mediaPlayer.stop()

    def precedent(self):
        print ("Précédent")
    def suivant(self):
        print ("Suivant")

    def volume(self):
        self.mediaPlayer.setVolume(self.ui.dBVolume.value())
        self.ui.suiviVol.setText(f'{str(self.ui.dBVolume.value())} %')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())