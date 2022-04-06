# Filename: hello.py

"""Simple Hello World example with PyQt5."""

import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# 2. Create an instance of QApplication
app = QApplication(sys.argv)

# 3. Create an instance of your application's GUI
window = QWidget()
window.setWindowTitle('PyQt5 App') # text in the top bar of the window
window.setGeometry(100, 100, 280, 80) # position and size of the window: x, y, width, height
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window) # text in html
helloMsg.move(60, 15) # place helloMsg at the coordinates (60, 15)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())
