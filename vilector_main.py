import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from ui_vilector import Ui_MainWindow
from PySide2.QtCore import QUrl, QTime , QFileInfo
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

        self.ui.pBAjout.clicked.connect(self.ajoutListe)
        self.ui.pBSupp.clicked.connect(self.suppListe)
        self.ui.listWidget.itemDoubleClicked.connect(self.mediaSelected)

        self.ui.dBVolume.valueChanged.connect(self.volume)
        self.ui.dBVolume.setRange(0, 100)
        self.ui.suiviVol.setText(f'{str(self.ui.dBVolume.value())} %')
        self.ui.sTpsCourant.valueChanged.connect(self.avanceSlider)

        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setVideoOutput(self.ui.Lecteur)

        self.mediaPlayer.durationChanged.connect(self.duree)
        self.mediaPlayer.positionChanged.connect(self.avancee)

        # mediaContent = QMediaContent(QUrl.fromLocalFile("big_buck_bunny.avi"))
        # self.mediaPlayer.setMedia(mediaContent)

    def lecture(self) :
        print("Lecture")
        if self.mediaPlayer.state() == QMediaPlayer.StoppedState :
            self.mediaSelected()
        else :
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
        currentItemRow = self.ui.listWidget.currentRow()
        if currentItemRow == -1 :
            return
        totalItems = self.ui.listWidget.count()
        self.ui.listWidget.setCurrentRow((currentItemRow-1)%totalItems)
        self.mediaSelected()
        print ("Précédent")

    def suivant(self):
        currentItemRow = self.ui.listWidget.currentRow()
        if currentItemRow == -1 :
            return
        totalItems = self.ui.listWidget.count()
        self.ui.listWidget.setCurrentRow((currentItemRow+1)%totalItems)
        self.mediaSelected()
        print ("Suivant")

    # def ajoutListe (self):
    #     print("Ajout dans playlist")
    #     newFile=QFileDialog.getOpenFileName(self, "Choix Film", "/home", "Movie Files (*.avi, *.mp4)")
    #     newMovie=QListWidgetItem(newFile[0])
    #     self.ui.listWidget.addItem(newMovie)

    def ajoutListe (self):
        print("Ajout dans playlist")
        newFile=QFileDialog.getOpenFileName(self, "Choix Film", "/home", "Movie Files (*.avi, *.mp4)")
        fInfo=QFileInfo(newFile[0])
        fShortName=fInfo.baseName()
        newMovie=QListWidgetItem(fShortName)
        newMovie.setToolTip(newFile[0])
        self.ui.listWidget.addItem(newMovie)

    def suppListe (self):
        print ("Supprimer de playList")
        rowItem = self.ui.listWidget.currentRow()
        if rowItem != -1 :
            self.ui.listWidget.takeItem(rowItem)

    # def mediaSelected (self):
    #     currentItem = self.ui.listWidget.currentItem()
    #     mediaContent = QMediaContent(QUrl.fromLocalFile(currentItem.text()))
    #     self.mediaPlayer.setMedia(mediaContent)
    #     self.lecture()

    def mediaSelected (self):
        currentItem = self.ui.listWidget.currentItem()
        mediaContent = QMediaContent(QUrl.fromLocalFile(currentItem.toolTip()))
        self.mediaPlayer.setMedia(mediaContent)
        self.mediaPlayer.play()

    def volume(self):
        self.mediaPlayer.setVolume(self.ui.dBVolume.value())
        self.ui.suiviVol.setText(f'{str(self.ui.dBVolume.value())} %')

    def duree(self):
        mediaDuration=self.mediaPlayer.duration()
        self.ui.sTpsCourant.setRange(0, mediaDuration)
        totalTimeMedia = QTime(0,0,0)
        totalTimeMedia = totalTimeMedia.addMSecs(mediaDuration)
        self.ui.lRestantTps.setText(totalTimeMedia.toString("HH:mm:ss"))

    def avancee(self):
        self.ui.sTpsCourant.valueChanged.disconnect(self.avanceSlider)
        mediaPosition = self.mediaPlayer.position()
        currentTimeMedia = QTime(0,0,0)
        currentTimeMedia = currentTimeMedia.addMSecs(mediaPosition)
        self.ui.lAvanceeTps.setText(currentTimeMedia.toString("HH:mm:ss"))
        self.ui.sTpsCourant.setValue(mediaPosition)
        self.ui.sTpsCourant.valueChanged.connect(self.avanceSlider)

    def avanceSlider (self):
        self.mediaPlayer.positionChanged.disconnect(self.avancee)
        self.mediaPlayer.setPosition(self.ui.sTpsCourant.sliderPosition())
        self.mediaPlayer.positionChanged.connect(self.avancee)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())