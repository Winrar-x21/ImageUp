from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap

from back import blur_image, unmask_image
file_path = 'jenny.png'

app = QApplication([])
window = Qwidget()
layout = QVBoxLayout()

save_open_buttons = QHBoxLayout()
open_button = QPushButton("Open")
save_open_buttons.addWidget(open_button)
layout.addLayout(save_open_buttons)

tools_layout = QHBoxLayout()
blur_button = QPushButton("Blur")
unmask_button = QPushButton("Unblur")
tools_layout
def openFileButtonHandler():
    global file_path

layout = QVBoxLayout()
picture = QLabel()
pixmap = Qpixmap('jenny.png').scaledToWidth(500)
picture = setPixmap(pixmap)
layout.addWidget(picture)
window.setLayout(layout)

window.show


def openFile

app.exec()