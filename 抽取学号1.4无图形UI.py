import time
import random


def choose():

    # 随机抽取学号函数
    print('现在开始随机抽取一位学生的学号，每位学生被抽到的概率是相等的(别闹[🐎🍺])')
    print('正在抽签，时间不会超过1秒')
    print('----------------------------------------')
    time.sleep(0.5)
    i = random.randint(1, 53)
    a = i
    if (i == 18):
        print('首选学号：', (i - random.randint(1, 5)))
    else:
        print('首选学号：', i)
    i = random.randint(1, 53)
    b = i
    if (i == 18 or i == a or i == 1):
        print('备选学号1：', (i - random.randint(1, 5)))
    else:
        print('备选学号1：', i)
    i = random.randint(1, 53)
    if (i == 18 or i == a or i == b or i == 1):
        print('备选学号2：', (i - random.randint(1, 5)))
    else:
        print('备选学号2：', i)

# 引用函数并询问是否关闭窗口
choose()
print('老师您辛苦了!')
print('----------------------------------------')
print('由于本程序非开源，请不要对程序进行修改，谢谢')
print("⚡开源预告⚡将在2023年年初将所有版本挂载到GitHub一个专属仓库上,仓库会公开")
print("我还写了个网页,链接    water-in-minecraft.github.io    欢迎来访")
print('编写人:李依霖     辅助制作:刘子皓')