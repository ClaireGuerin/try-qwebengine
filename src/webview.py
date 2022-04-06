#!/usr/bin/python

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton
#from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView


class OpenPage(QWidget):

    def __init__(self, htmlfile):
        super().__init__()

        self.initUI(htmlfile)

    def initUI(self, htmlfile):

        #hbox = QHBoxLayout(self) # organizes widgets horizontally in a window
        vbox = QVBoxLayout(self) # organizes widgets vertically in a window

        self.webEngineView = QWebEngineView() # create the webview widget
        self.loadPage(htmlfile)

        vbox.addWidget(self.webEngineView)
        vbox.addWidget(QPushButton('Model 1'))
        # self.buttonObjectName.clicked.
        vbox.addWidget(QPushButton('Model 2'))
        vbox.addWidget(QPushButton('Model 3'))

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Simple application with Web View')
        self.show()

    def loadPage(self, htmlfile):

        with open(htmlfile, 'r') as f:

            html = f.read()
            self.webEngineView.setHtml(html) # set html to webview widget

def main():

    app = QApplication(sys.argv)
    ex = OpenPage('webpage/test.html')
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()