#!/usr/bin/python

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton
#from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView


class OpenPage(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #hbox = QHBoxLayout(self) # organizes widgets horizontally in a window
        vbox = QVBoxLayout(self) # organizes widgets vertically in a window

        self.webEngineView = QWebEngineView()
        self.loadPage()

        vbox.addWidget(self.webEngineView)
        vbox.addWidget(QPushButton('1'))
        vbox.addWidget(QPushButton('2'))
        vbox.addWidget(QPushButton('3'))

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Simple application with Web View')
        self.show()

    def loadPage(self):

        with open('webpage/test.html', 'r') as f:

            html = f.read()
            self.webEngineView.setHtml(html)

def main():

    app = QApplication(sys.argv)
    ex = OpenPage()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()