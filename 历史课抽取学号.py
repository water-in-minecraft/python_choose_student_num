import random


number = 10
class_size = 55
random_list = []
while (len(random_list) < number):
    rand_num = random.randint(1, class_size)
    if ((rand_num not in [47, 18]) and (rand_num not in random_list)):
        random_list.append(rand_num)
print('今天的十位学生的学号是:', random_list)
