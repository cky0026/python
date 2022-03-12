import random
import sys
import threading
import os
import time


def init():
    global hours, hunger, happiness, health, status
    # todo:初始化打印，创造或读取文件
    print("我的名字叫Tommy，一只可爱的猫咪....\n你可以和我一起散步，玩耍，你也需要给我吃好吃的东西，带我去看病，也可以让我发呆....")
    print("Commands:")
    print("1.walk：散步\n2.play：玩耍\n3.feed：喂我\n4.seedoctor：看医生\n5.letalone：让我独自一人\n6.status：查看我的状态\n7.bye：不想看到我")

    s = os.getcwd() + "\\Tommy.txt"
    exist = os.path.exists(s)
    if exist:
        f = open('Tommy.txt', encoding='UTF-8')
        temp = f.read().split()
        f.close()
        hours = int(temp[0])
        happiness = int(temp[1])
        hunger = int(temp[2])
        health = int(temp[3])
        status = temp[4]
        fun_print()  # 为了体现保存了文件会在第二次读取的时候在计时器开始之前率先打印一次状态

    else:
        hours = random.randint(0, 23)
        happiness = random.randint(0, 100)
        hunger = random.randint(0, 100)
        health = random.randint(0, 100)
        if hours > 8:
            status = "醒着但是很无聊"
        else:
            status = "在睡觉"
        temp = str(hours) + " " + str(happiness) + " " + str(hunger) + " " + str(health) + " " + status
        # r模式默认，只读，w+打开一个文件用于读写。如果该文件已存在则打开文件，原有内容会被删除。否则创建新文件。
        f = open('Tommy.txt', 'w+', encoding='UTF-8')
        f.write(temp)
        f.close()


# 打印状态
def fun_print():
    global timer, hours, hunger, happiness, health, status
    print("当前时间：%-2d 点" % hours)
    print("我当前的状态：我" + status + "......")
    print("Happiness:   Sad", end=" ")
    print((happiness // 2) * '*' + (50 - (happiness // 2)) * '-' + ' Happy(%.3d)' % happiness)
    print("Hunger:     Full", end=" ")
    print((hunger // 2) * '*' + (50 - (hunger // 2)) * '-' + ' Hunger(%.3d)' % hunger)
    print("Health:     Sick", end=" ")
    print((health // 2) * '*' + (50 - (health // 2)) * '-' + ' Health(%.3d)' % health)
    print()


# 处理指令
def command_handler():
    global timer, hours, status, flag
    command = input("你想：")
    if command == "walk":
        if alert():
            print("我在散步......")
            status = "在散步"
        else:
            print("我在散步......")
            status = "在散步"

    elif command == "play":
        if alert():
            print("我在玩耍......")
            status = "在玩耍"
        else:
            print("我在玩耍......")
            status = "在玩耍"

    elif command == "feed":
        if alert():
            print("我在吃饭.....")
            status = "在吃饭"
        else:
            print("我在吃饭.....")
            status = "在吃饭"

    elif command == "seedoctor":
        if alert():
            print("我在看医生.....")
            status = "在看医生"
        else:
            print("我在看医生.....")
            status = "在看医生"

    elif command == "letalone":
        # 根据时间判断状态
        if 0 <= hours <= 8:
            print("我在睡觉.....")
            status = "在睡觉"
        else:
            print("我醒着但是很无聊.....")
            status = "醒着但是很无聊"

    elif command == "status":
        # 当Tommy醒着没有事干时需要根据时间改变状态
        if status == "醒着但是很无聊":
            if 0 <= hours <= 8:
                status = "在睡觉"
        elif status == "在睡觉":
            if not 0 <= hours <= 8:
                status = "醒着但是很无聊"
        print("我" + status + ".....")

    elif command == "bye":
        print("记得来找我！Bye.....")
        # todo：把现有的状态保存到文件里
        temp = str(hours) + ' ' + str(happiness) + ' ' + str(hunger) + ' ' + str(health) + ' ' + status
        # r模式默认，只读，w+打开一个文件用于读写。如果该文件已存在则打开文件，原有内容会被删除。否则创建新文件。
        f = open('Tommy.txt', 'w+', encoding='UTF-8')
        f.write(temp)
        f.close()
        sys.exit(0)
    else:
        print("我不懂你在说什么..")

    print()


def alert():
    global hours, hunger, happiness, health, status
    insist = False
    if status == "在睡觉":
        if input("你确认要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的!(y表示是/其他表示不是)") == 'y':
            insist = True
    if insist:
        happiness -= 4
        return insist
    return insist


def fun_timer():
    # todo：tick时间，根据状态改变各个指数的值
    global hours, hunger, happiness, health, status
    # 滴答
    hours += 1
    if hours > 23:
        hours = 0

    # 除开状态变化，还有可叠加状态
    # 根据状态判断各指数变化的情况
    if status == "在睡觉":
        hunger += 1
    elif status == "醒着但是很无聊":
        hunger += 2
        happiness -= 1
    elif status == "在散步":
        hunger += 3
        health += 1
    elif status == "在玩耍":
        hunger += 3
        happiness += 1
    elif status == "在吃饭":
        hunger -= 3
    elif status == "在看医生":
        health += 4

    # 可以叠加的指数变化情况：在Tommy过饱或过饿的时候
    if hunger > 80 or hunger < 20:
        health -= 2

    # 可以叠加的指数变化情况：在Tommy不幸福的时候
    if happiness < 20:
        health -= 1

    # 保持各个指数在0~100之内
    happiness = limit(happiness)
    hunger = limit(hunger)
    health = limit(health)
    timer = threading.Timer(5.0, fun_timer)  # 5s执行一次fun_timer
    timer.start()


def limit(value):
    if value < 0:
        value = 0
    elif value > 100:
        value = 100
    return value


def main():
    # global变量：时间，饥饿指数，幸福指数，健康指数
    global hours, hunger, happiness, health, status
    init()  # 初始化Tommy，包括指南，读取文件内容，如果没有文件则创建文件并对状态等内容进行随机赋值
    fun_timer()  # 启动定时器，定时器会在每次tick的时候改变时间以及根据状态改变指数
    while True:
        fun_print()
        command_handler()  # 处理输入的指令，根据指令改变状态


if __name__ == "__main__":
    main()
