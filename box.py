import random


# open qt_designer
# python "D:\Downloads\PyQt-Fluent-Widgets-master\tools\designer.py"
class Box:
    box = []
    len_of_box = 4
    box_is_edited = 0

    def __init__(self) -> None:
        # 实例初始化
        self.create_new_box(self.len_of_box)
        self.random_generate()
        self.print_box()
        print("矩阵初始化完成")

    def create_new_box(self, len_of_box):
        # 创建一个边长为len_of_box的二维数组
        the_box = []
        for i in range(self.len_of_box):
            tem = []
            for j in range(self.len_of_box):
                tem.append(0)
            the_box.append(tem)
        # 更新变量
        self.box_is_edited = False
        self.box = the_box
        print("已创建{}x{}的正方形".format(len_of_box, len_of_box))
        return the_box

    def print_box(self):
        for i in self.box:
            print(i)

    def edit_box(self, x, y, num):
        # 将数组的X行Y列的数值修改为num
        self.box[x][y] = num
        print("已将数组的[{}][{}]修改为{}".format(x, y, num))

    def random_generate(self):
        # 随机把空位(0)的位置变成2或4或8
        edited = 1
        while edited:
            # 如果数组才创建，就随机加俩2进去
            if self.box_is_edited < 2:
                while self.box_is_edited < 2:
                    x = random.randint(0, self.len_of_box - 1)
                    y = random.randint(0, self.len_of_box - 1)
                    if self.box[x][y] == 0:
                        self.edit_box(x, y, 2)
                        self.box_is_edited += 1
                edited = 0
                print("矩阵初次数字生成完成")

            # 如果不是初建，就[2, 4, 8]选一个加进去
            elif edited:
                x = random.randint(0, self.len_of_box - 1)
                y = random.randint(0, self.len_of_box - 1)
                if self.box[x][y] == 0:
                    self.edit_box(x, y, random.choice([2, 4]))
                    edited = 0
                    print("矩阵随机生成完成")

    def move_a(self):
        box = self.box
        len_of_box = self.len_of_box
        for i in range(len_of_box):
            for j in range(len_of_box):
                if box[i][j] != 0 and j - 1 >= 0:
                    a = j
                    while a - 1 >= 0:
                        now_key = box[i][a]
                        if box[i][a - 1] == now_key:
                            box[i][a - 1] = now_key * 2
                        elif box[i][a - 1] == 0:
                            box[i][a - 1] = now_key
                        else:
                            break
                        box[i][a] = 0
                        a -= 1
        self.box = box

    def move_d(self):
        box = self.box
        len_of_box = self.len_of_box
        for i in range(len_of_box):
            for j in range(len_of_box):
                if box[i][j] != 0 and j + 1 <= len_of_box - 1:
                    a = j
                    # 开始移动
                    while a + 1 <= len_of_box - 1:
                        now_key = box[i][a]
                        if box[i][a + 1] == now_key:
                            box[i][a + 1] = now_key * 2
                        elif box[i][a + 1] == 0:
                            box[i][a + 1] = now_key
                        else:
                            break
                        box[i][a] = 0
                        a += 1
                    # 移动完成
        self.box = box

    def move_w(self):
        box = self.box
        len_of_box = self.len_of_box
        for i in range(len_of_box):
            for j in range(len_of_box):
                if box[j][i] != 0 and j - 1 >= 0:
                    a = j
                    # 开始移动
                    while a - 1 >= 0:
                        now_key = box[a][i]
                        if box[a - 1][i] == now_key:
                            box[a - 1][i] = now_key * 2
                        elif box[a - 1][i] == 0:
                            box[a - 1][i] = now_key
                        else:
                            break
                        box[a][i] = 0
                        a -= 1
                    # 移动完成
        self.box = box

    def move_s(self):
        box = self.box
        len_of_box = self.len_of_box
        for i in range(len_of_box):
            for j in range(len_of_box):
                if box[j][i] != 0 and j + 1 <= len_of_box - 1:
                    a = j
                    # 开始移动
                    while a + 1 <= len_of_box - 1:
                        now_key = box[a][i]
                        if box[a + 1][i] == now_key:
                            box[a + 1][i] = now_key * 2
                        elif box[a + 1][i] == 0:
                            box[a + 1][i] = now_key
                        else:
                            break
                        box[a][i] = 0
                        a += 1
                    # 移动完成
        self.box = box


if __name__ == '__main__':
    b1 = Box()
    while True:
        print("——" * 10)
        print("ASDW控制移动,R重置游戏,E退出游戏")
        com = input("请输入指令：")
        print("——" * 10)

        if com == "r":
            b1 = Box()
        elif com == "e":
            break
        elif com == "a":
            for i in range(b1.len_of_box):
                b1.move_a()
            b1.random_generate()
            b1.print_box()
        elif com == "s":
            for i in range(b1.len_of_box):
                b1.move_s()
            b1.random_generate()
            b1.print_box()
        elif com == "d":
            for i in range(b1.len_of_box):
                b1.move_d()
            b1.random_generate()
            b1.print_box()
        elif com == "w":
            for i in range(b1.len_of_box):
                b1.move_w()
            b1.random_generate()
            b1.print_box()
        else:
            print("请输入指定指令！")
