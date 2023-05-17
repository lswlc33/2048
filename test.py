box = [
    [2, 0, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],

]
len_of_box = 4


def print_box():
    for i in box:
        print(i)


for i in range(len_of_box):
    for j in range(len_of_box):
        if box[i][j] != 0 and j + 1 <= len_of_box - 1:
            print("动值box[{}][{}] = {}".format(i, j, box[i][j]))
            a = j
            # 开始移动
            while a + 1 <= len_of_box - 1:
                now_key = box[i][a]
                if box[i][a + 1] == now_key:
                    box[i][a + 1] = now_key * 2
                elif box[i][a + 1] == 0:
                    box[i][a + 1] = now_key
                box[i][a] = 0
                a += 1
            print_box()
            # 移动完成
