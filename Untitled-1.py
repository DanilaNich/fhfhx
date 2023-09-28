import random
a = random.randint(1,10)
b = int(input("угадай число от 1 до 10:"))
if b == a:
    print("вы угадали")
else:
    print ("вы не угадали")
