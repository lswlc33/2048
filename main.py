from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget

from box import Box
from Interface import *


def loadwindows():
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()


if __name__ == '__main__':
    loadwindows()

