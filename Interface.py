# coding:utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel, QGridLayout
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox)
from qframelesswindow import FramelessWindow, StandardTitleBar


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(' ', '-'))


class Box_Widget(QFrame):
    def __init__(self, num):
        super().__init__()
        h_layout = QGridLayout(self)
        self.setObjectName("h_layout1")
        self.label = QLabel(str(num), self)
        self.label.setAlignment(Qt.AlignCenter)  # 将文本居中显示
        self.setFixedSize(40, 40)  # 设置控件大小
        if num != "0":
            # self.setStyleSheet("background-color: black;")
            self.setStyleSheet("#h_layout1 {border: 2px solid gray}")

        self.label.setFont(QFont("微软雅黑", 14))
        h_layout.addWidget(self.label)


class Home_Widget(Widget):
    def __init__(self, text: str, parent=None):
        super().__init__(text)
        self.grid = QGridLayout(self)
        self.grid.setSpacing(0)
        self.grid.setAlignment(Qt.AlignCenter)
        boxt = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 2, 0, 0],
            [2, 0, 0, 0]
        ]
        # 页面添加文字
        for i in range(len(boxt)):
            for j in range(len(boxt[0])):
                box = Box_Widget(str(boxt[i][j]))
                self.grid.addWidget(box, i, j)


class Window(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))

        self.hBoxLayout = QHBoxLayout(self)
        self.navigationInterface = NavigationInterface(self, showMenuButton=True)
        self.stackWidget = QStackedWidget(self)

        # create sub interface
        self.homeInterface = Home_Widget('Home Interface', self)
        self.helpInterface = Widget('Help Interface', self)
        self.settingInterface = Widget('Setting Interface', self)

        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()

        self.initWindow()

    def initLayout(self):
        # 初始化最外层布局
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, self.titleBar.height(), 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)

    def initNavigation(self):
        # 初始化侧边栏
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.homeInterface, FIF.HOME, 'Home')
        self.addSubInterface(self.helpInterface, FIF.HELP, 'Help', NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

        # 侧边栏最大展开宽度
        self.navigationInterface.setExpandWidth(150)

        # 翻页事件
        self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        self.stackWidget.setCurrentIndex(0)

    def initWindow(self):
        # 初始化窗口
        self.resize(900, 700)  # 大小
        self.setWindowIcon(QIcon('resource/logo.png'))  # 图标
        self.setWindowTitle('A game：2048')  # 标题
        self.titleBar.setAttribute(Qt.WA_StyledBackground)

        # 窗口打开位置，默认在屏幕中间
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.setQss()

    def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP):
        # 侧边栏添加内容事件
        self.stackWidget.addWidget(interface)
        self.navigationInterface.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position,
            tooltip=text
        )

    def setQss(self):
        # (不)自适应主题
        # color = 'dark' if isDarkTheme() else 'light'
        color = 'light'
        with open(f'resource/{color}/demo.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def switchTo(self, widget):
        # 翻页
        self.stackWidget.setCurrentWidget(widget)

    def onCurrentInterfaceChanged(self, index):
        widget = self.stackWidget.widget(index)
        self.navigationInterface.setCurrentItem(widget.objectName())

    def showMessageBox(self, text):
        # 弹出消息
        w = MessageBox(
            text,
            self
        )
        w.exec()


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
