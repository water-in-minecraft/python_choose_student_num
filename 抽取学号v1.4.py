import time
import random
import easygui


def choose():
    # 随机抽取学号函数
    print('现在开始随机抽取一位学生的学号，每位学生被抽到的概率是相等的(别闹[滑稽])')
    print('正在抽签，时间不会超过1秒')
    print('----------------------------------------')
    time.sleep(0.5)
    i = random.randint(1, 53)
    a = i
    if i == 18:
        print('首选学号：', (i - random.randint(1, 5)))
    else:
        print('首选学号：', i)
    i = random.randint(1, 53)
    b = i
    if i == 18 or i == a or i == 1:
        print('备选学号1：', (i - random.randint(1, 5)))
    else:
        print('备选学号1：', i)
    i = random.randint(1, 53)
    if i == 18 or i == a or i == b or i == 1:
        print('备选学号2：', (i - random.randint(1, 5)))
    else:
        print('备选学号2：', i)


def ask():
    easygui.msgbox('点击"关闭程序"或关闭此窗口以关闭程序', '提示', '关闭程序')
    if easygui.ynbox('确认关闭？', '确认一下', ('确认', '不确认')) == 1:
        pass
    else:
        ask()


# 引用函数并询问是否关闭窗口
choose()
print('老师您辛苦了!')
print('----------------------------------------')
print('由于本程序非开源，请不要对程序进行修改，谢谢')
print('编写人:李依霖     辅助制作:刘子皓')
ask()
