import random


class Box:
    box = []
    len_of_box = 4
    box_is_edited = 0

    def __init__(self) -> None:
        # 实例初始化
        self.len_of_box = 4
        self.create_new_box(self.len_of_box)
        self.random_generate()
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
        self.print_box()
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
        self.print_box()


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
            pass
        elif com == "s":
            pass
        elif com == "d":
            pass
        elif com == "w":
            pass
        else:
            print("请输入指定指令！")
