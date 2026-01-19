from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QVBoxLayout
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt, QTime, QTimer
import sys
import os

class Digitalclock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer()
    
        self.initUI()

    
    def initUI(self):
        self.setGeometry(1100, 0 , 600, 300)


        vbox = QVBoxLayout()

        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        vbox.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("font-size:100px; background-color:black; color:#39FF14;")
        # font_id = QFontDatabase.addApplicationFont("DS-DIGIB.TTF")



        # font_id = QFontDatabase.addApplicationFont(
        # os.path.join(os.path.dirname(__file__), "DS-DIGIB.TTF")
        #            )
        # self.time_label.setFont(QFont(
        #  QFontDatabase.applicationFontFamilies(font_id)[0], 150
        #           ))

        # font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        # print(font_id)
        # font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        # my_font = QFont(font_family, 150)
        # self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)



def main():
    app = QApplication(sys.argv)
    clock = Digitalclock()
    clock.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
