# coding:utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QKeySequence
from PyQt5.QtWidgets import *
from qfluentwidgets import FluentIcon as FIF, PushButton, SpinBox, ComboBox, ExpandSettingCard
from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox)
from qframelesswindow import FramelessWindow, StandardTitleBar
from box import *


# python ./tools/designer.py

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
        # 高亮非0格子

        if num == "0":
            self.setStyleSheet(
                "#h_layout1{border: 2px solid gray;border-color: rgb(180,180,180);border-radius: "
                "10px;background-color: rgb(255, 255, 255);}#h_layout1:hover{background-color: rgb(229,229,229);}"
            )

        elif int(num) >= 64:
            self.setStyleSheet(
                "#h_layout1{border: 5px solid gray;border-color: rgb(255,32,32);border-radius: "
                "10px;background-color: rgb(255, 255, 255);}#h_layout1:hover{background-color: rgb(235,235,235);}"
            )
        else:
            self.setStyleSheet(
                "#h_layout1{border: 5px solid gray;border-color: rgb(58,174,239);border-radius: "
                "10px;background-color: rgb(255, 255, 255);}#h_layout1:hover{background-color: rgb(235,235,235);}"
            )

        self.label.setFont(QFont("Comic Sans MS", 30))
        h_layout.addWidget(self.label)


def delete_all_widgets(layout):
    for i in reversed(range(layout.count())):
        item = layout.itemAt(i)

        if isinstance(item, (QGridLayout, QHBoxLayout, QVBoxLayout)):
            # If the item is another layout, recursively delete its contents.
            layout.delete_all_widgets(item)
        else:
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        layout.removeItem(item)


class Setting_Widget(Widget):
    def __init__(self, text: str, parent=None):
        super().__init__(text)
        # self.hBoxLayout = QHBoxLayout(self)
        # self.settingInterface = SettingInterface(self)
        # self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        # self.hBoxLayout.addWidget(self.settingInterface)


class Home_Widget(Widget):
    def __init__(self, text: str, parent=None):
        super().__init__(text)

        self.is_stop = False

        # 布局
        self.game = Box()
        self.vBoxLayout = QVBoxLayout(self)
        self.grid = QGridLayout()
        self.grid.setSpacing(5)
        self.pushButton1 = PushButton('开始/重新开始', self, FIF.UPDATE)
        self.pushButton1.clicked.connect(self.init_boxw)
        self.vBoxLayout.addLayout(self.grid, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.pushButton1, 0, Qt.AlignBottom)

        # 键盘监听ASDW
        shortcut_a = QShortcut(QKeySequence("A"), self)
        shortcut_a.activated.connect(self.move_a)
        shortcut_a = QShortcut(QKeySequence("S"), self)
        shortcut_a.activated.connect(self.move_s)
        shortcut_a = QShortcut(QKeySequence("D"), self)
        shortcut_a.activated.connect(self.move_d)
        shortcut_a = QShortcut(QKeySequence("W"), self)
        shortcut_a.activated.connect(self.move_w)

        # 初始化宫格
        self.init_boxw()

    def check_if_full(self):
        box = self.game.box
        not_in = True
        for i in box:
            if 0 in i:
                not_in = False
        if not_in:
            self.is_stop = True
            self.game = Box()
            delete_all_widgets(self.grid)
            Window.showMessageBox(
                self,
                "杂鱼,就这？",
                "你就这点实力吗？杂鱼~",
                '确实不行',
                '怎么可能'
            )

            self.is_stop = False
            self.add_box_widget(self.game.box)
            return True

    def check_is_win(self):
        box = self.game.box
        is_win = False
        for i in box:
            if 1024 in i:
                is_win = True
        if is_win:
            self.is_stop = True
            Window.showMessageBox(
                self,
                "杂鱼，居然赢了吗",
                "这游戏本来很简单！杂鱼！",
                '固若金汤！',
                '啊对对对。'
            )

            self.is_stop = False
            return True

    def move_a(self):
        if self.is_stop:
            return False
        if self.check_if_full():
            return False
        for i in range(self.game.len_of_box):
            self.game.move_a()
        self.game.random_generate()
        self.check_is_win()
        self.game.print_box()
        delete_all_widgets(self.grid)
        self.add_box_widget(self.game.box)

    def move_s(self):
        if self.is_stop:
            return False
        if self.check_if_full():
            return False
        for i in range(self.game.len_of_box):
            self.game.move_s()
        self.game.random_generate()
        self.check_is_win()
        self.game.print_box()
        delete_all_widgets(self.grid)
        self.add_box_widget(self.game.box)


    def move_d(self):
        if self.is_stop:
            return False
        if self.check_if_full():
            return False
        for i in range(self.game.len_of_box):
            self.game.move_d()
        self.game.random_generate()
        self.check_is_win()
        self.game.print_box()
        delete_all_widgets(self.grid)
        self.add_box_widget(self.game.box)

    def move_w(self):
        if self.is_stop:
            return False
        if self.check_if_full():
            return False
        for i in range(self.game.len_of_box):
            self.game.move_w()
        self.game.random_generate()
        self.check_is_win()
        self.game.print_box()
        delete_all_widgets(self.grid)
        self.add_box_widget(self.game.box)

    def init_boxw(self):
        # 初始化宫格

        self.game.create_new_box(self.game.len_of_box)
        self.game.random_generate()
        delete_all_widgets(self.grid)
        self.add_box_widget(self.game.box)

    def add_box_widget(self, boxt):
        # 宫格添加格子
        for i in range(len(boxt)):
            for j in range(len(boxt[0])):
                box = Box_Widget(str(boxt[i][j]))
                box.setFixedSize(100, 100)
                self.grid.addWidget(box, i, j)


class Window(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))
        self.titleBar.setDoubleClickEnabled(False)
        self.titleBar.maxBtn.deleteLater()  # 删除最大化按钮
        self.setResizeEnabled(False)  # 禁止手动拉伸

        self.hBoxLayout = QHBoxLayout(self)
        self.navigationInterface = NavigationInterface(self, showMenuButton=True)
        self.stackWidget = QStackedWidget(self)

        # create sub interface
        self.homeInterface = Home_Widget('Home Interface', self)
        self.helpInterface = Widget('Help Interface', self)
        self.settingInterface = Setting_Widget('Setting Interface', self)

        # 帮助--box
        self.vBoxLayout = QVBoxLayout(self.helpInterface)
        self.help_card = ExpandSettingCard(
            FIF.INFO,
            "点击查看游戏指南"
        )
        self.help_text = QLabel(
            "2048 是一款数字益智游戏，游戏规则如下：\n\n游戏开始时，棋盘上有两个数字方块，数字为 2  "
            "。\n\n玩家可以通过ASDW四个方向的滑动来移动数字方块，相同数字的方块在移动时会合并成一个数字方块，数字为原来两个数字方块的数字之和。\n\n每次移动后，系统会在空白的方格上随机生成一个数字方块，数字为 "
            "2 或 4。\n\n当棋盘上的数字方块无法再移动时，游戏结束。\n\n玩家的目标是在棋盘上不断合并数字方块，直到得到一个数字为 2048 的方块。\n\n玩家可以选择继续游戏，或者重新开始游戏。"
        )

        self.help_text.setWordWrap(True)
        self.help_card.viewLayout.addWidget(self.help_text)
        self.help_card.view.setMinimumHeight(350)
        self.vBoxLayout.addWidget(self.help_card)

        self.init_setting_page()

        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()

        self.initWindow()

    def init_setting_page(self):
        self.vBoxLayout = QVBoxLayout(self.settingInterface)

        self.hb = QHBoxLayout()
        # self.setStyleSheet(
        #     "#h_layout1{border: 2px solid gray;border-color: rgb(180,180,180);border-radius: "
        #     "10px;background-color: rgb(255, 255, 255);}#h_layout1:hover{background-color: rgb(229,229,229);}"
        # )
        self.vBoxLayout.addLayout(self.hb)

        # 设置--宫格大小--text
        self.spin_text = QLabel("调整宫格边长:")

        # 设置--宫格大小--spinbox
        self.spinBox = SpinBox(self)
        self.spinBox.setMaximum(7)
        self.spinBox.setMinimum(4)
        self.spinBox.setValue(self.homeInterface.game.len_of_box)
        self.spinBox.valueChanged.connect(self.change_box_len)

        self.hb.addWidget(self.spin_text, 1)
        self.hb.addWidget(self.spinBox, 0)

    def change_box_len(self):
        len_value = self.spinBox.value()
        self.homeInterface.game.len_of_box = len_value
        self.homeInterface.init_boxw()
        print("边长变更为" + str(len_value))

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
        self.adjustSize()  # 自适应大小
        # self.resize(900, 700)  # 大小
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
        # 主题
        self.setStyleSheet(
            "Widget > QLabel {font: 24px 'Segoe UI', 'Microsoft YaHei';}Widget {border: 1px solid rgb(229, 229, "
            "229);border-right: none;border-bottom: none;border-top-left-radius: 10px;background-color: rgb(249, 249, "
            "249);}Window {background-color: rgb(243, 243, 243);}"
        )

    def switchTo(self, widget):
        # 翻页
        self.stackWidget.setCurrentWidget(widget)
        self.adjustSize()

    def onCurrentInterfaceChanged(self, index):
        widget = self.stackWidget.widget(index)
        self.navigationInterface.setCurrentItem(widget.objectName())

    def showMessageBox(self, text1, text2, bt1, bt2):
        # 弹出消息
        w = MessageBox(
            text1,
            text2,
            self
        )
        w.yesButton.setText(bt1)
        w.cancelButton.setText(bt2)
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
