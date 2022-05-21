from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
import PyQt5


class AnaEkran(QMainWindow):
    def __init__(self):
        super (AnaEkran, self).__init__()

        #Tarayıcı İskeleti
        self.tarayici = QWebEngineView()
        google = 'www.google.com'
        qurl = QUrl(google)
        self.tarayici.setUrl(qurl)

        self.setCentralWidget(self.tarayici)
        self.showMaximized()

        #Nagivasyon tuşları

        navbar = QToolBar()
        self.addToolBar(navbar)

        #Geri Butonu
        geriButon = QAction('Geri',self)
        geriButon.triggered.connect(self.tarayici.back)
        navbar.addAction(geriButon)

        #İleri Butonu
        ileriButon = QAction('İleri',self)
        ileriButon.triggered.connect(self.tarayici.forward)
        navbar.addAction(ileriButon)

        #Yenile Butonu
        yenileButon = QAction('Yenile',self)
        yenileButon.triggered.connect(self.tarayici.reload)
        navbar.addAction(yenileButon)

        #Ana sayfa Butonu
        anasayfaButon = QAction('Ana Sayfa',self)
        anasayfaButon.triggered.connect(self.AnaEkranaGit)
        navbar.addAction(anasayfaButon)

        #Arama Çubuğu
        self.aramaCubugu = QLineEdit()
        self.aramaCubugu.returnPressed.connect(self.LinkeGit)
        navbar.addWidget(self.aramaCubugu)
        self.tarayici.urlChanged.connect(self.LinkiAra)

    def AnaEkranaGit(self):
        google = 'http://google.com'
        self.tarayici.setUrl(QUrl(google))
    def LinkeGit(self):
        url = self.aramaCubugu.text()
        self.tarayici.setUrl(QUrl(url))
    def LinkiAra(self, link):
        self.aramaCubugu.setText(link.toString())


Tarayıcı = QApplication(sys.argv)
QApplication.setApplicationName("BBEF Tarayıcı")
ekran = AnaEkran()
Tarayıcı.exec_()

