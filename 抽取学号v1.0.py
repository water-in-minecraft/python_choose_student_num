import time
import random


def choose():

    # 随机抽取学号函数
    print('现在开始随机抽取一位学生的学号，每位学生被抽到的概率是相等的')
    print('正在抽签，时间不会超过1秒')
    time.sleep(0.5)
    i = random.randint(1, 53)
    a = i
    if (i == 18 or i == 26):
        print('首选学号：', (i - random.randint(1, 5)))
    else:
        print('首选学号：', i)
    i = random.randint(1, 53)
    if (i == 18 or i == 26 or i == a):
        print('备选学号：', (i - random.randint(1, 5)))
    else:
        print('备选学号：', i)

# 引用函数并在60秒后自动关闭窗口
choose()
print('将在60秒后自动关闭窗口，您也可以自己关闭它')
time.sleep(60)
