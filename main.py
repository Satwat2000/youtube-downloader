import sys
from Repo import ComboBox, Func
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout  # Importing base widigts
# Importing aditional widgits
from PyQt5.QtWidgets import QLabel, QPushButton, QComboBox, QFileDialog, QLineEdit, QPushButton


class info():
    Types = {
        'value': ['Types', 'Video', 'Audio']
    }
    Format = {
        'default': ['Format'], 
        'value': ['m4a', 'webm']
    }
    Resolution = {
        'default': ['Resolution'], 
        'Audio': ['webm@160', 'm4a@128', 'webm@128', 'webm@70', 'webm@50'], 
        'Video': ['144p', '240p', '360p', '480p', '720p', '1080p']
    }


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Template")
        self.setGeometry(150, 200, 405, 227)
        self.setFixedSize(405, 227)
        self.mainlayout = QVBoxLayout()
        self.setLayout(self.mainlayout)
        self.addComboBox()
        self.add_opLocationField()

    def addComboBox(self):
        layout = QHBoxLayout()
        print(info.Types['value'])
        self.comboBox1 = ComboBox(info.Types['value'])
        self.comboBox2 = ComboBox(info.Format['default'])
        self.comboBox3 = ComboBox(info.Resolution['default'])
        layout.addWidget(self.comboBox1)
        layout.addWidget(self.comboBox2)
        layout.addWidget(self.comboBox3)
        self.mainlayout.addLayout(layout)
        
    def add_opLocationField(self):
        layout = QHBoxLayout()
        self.op_dir = QLineEdit(Func.getDefaultDownloadDir())
        self.search = QPushButton("...")
        # layout.addStretch(stretch=1)
        layout.addWidget(self.op_dir)
        layout.addWidget(self.search)
        self.mainlayout.addLayout(layout)
        


if __name__ == '__main__':
    app = QApplication([])
    home = UI()
    home.show()
    sys.exit(app.exec_())
