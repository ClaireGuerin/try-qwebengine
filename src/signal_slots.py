# Filename: signals_slots.py
"""Signals and slots example."""

import sys
import functools

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

def greeting():
    """Slot function."""
    if msg.text(): # if there's text in the message
        msg.setText("") # clear text
    else: 
        msg.setText("Hello World!") # print "Hello World"
        
def greeting_who(who):
    """Slot function."""
    if msg.text():
        msg.setText('')
    else:
        msg.setText(f'Hello {who}')


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
btn.clicked.connect(greeting)
#btn.clicked.connect(functools.partial(greeting_who, 'Claire!'))  # Connect clicked to greeting()

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())