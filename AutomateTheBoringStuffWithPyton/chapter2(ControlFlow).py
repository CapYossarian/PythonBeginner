#цикл for  и функция range
# name = input('Введите имя ')
# print(name)
# for i in range(5):
#     print(name + ' ' + str(i) + ' раз')

#Аргументы начала и конца. Конец не входит.

# for i in range(2,5):
#     print('От 2 до 5==>'+str(i) )

# сумма чисел от 1 до 100. У Гауса 50 пар 1+99, 2 +98 .... +50 5050
# summ100 = 0
# for i in range(101):
#     summ100+=i
# print(summ100)

#Начало конец шаг 10 20 ... 100
# for i in range(10,101,10):
#     print(i)
#

#импортирование функций
# import random
# for i in range(5):
#     print(random.randint(1,10))

#Альтернативная форма import
# from random import *
# print(randint(1,100))

#sys.exit
import sys
while True:
    print('Введите выход для выхода. ')
    response = input()
    if response == 'выход':
         sys.exit()
    print('Вы ввели ' + response + '.')