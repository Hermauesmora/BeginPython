import random

ran_num = []
for i in range(5):
    ran_num.append(random.randint(0, 10))
    print(ran_num[i], end=' ')
num = int(input())
if num in ran_num:
    print(num)
