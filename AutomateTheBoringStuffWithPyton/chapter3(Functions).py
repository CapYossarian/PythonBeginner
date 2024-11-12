# def hello():
#     print('Привет всем')
#     print('Hello there')
#     print('')
# hello()
# hello()

# #С параметрами
# def hello(name):
#     print('Привет '+name)
# hello('Вася')
# hello('Петя')

# с возвратом
# def checkPassword(pwd):
#     if pwd!= 'елка':
#         return False
#     else:
#         return True
# while True:
#     print('пароль')
#     answer = input()
#     if checkPassword(answer):
#         break
#     print('Сам ты ' + answer)

# import random
# for i in range(10):
#     print(random.randint(1, 10))
#некорректный вызов==>
# for i in range(10):
#     print(random.randint(10, 1))

#end в print() по умолчанию на новой  строке
# print('1)')
# print('Привет')
# print('Мир')
# print('2)')
# print('Привет', end='')
# print('Мир')
# print('3 - sep)')
# print('кот','собака','мышь', sep=', ')

#20241111 локальные и глобальные переменные. использование в локальной области глобальную переменную - проверка
# def spam():
#     print (globalvar)
#
# globalvar=17
# spam()

# #2024112 Инструкция global
# def spam():
#     global eggs
#     eggs ='spam'
# spam()
# print(eggs)

#Обработка исключений
# def spam(devby):
#     try:
#         return 42/devby
#     except ZeroDivisionError:
#         print('Ошибка: Неправильный аргумент')
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

#Угадывание чисел
import random
secretNumber = random.randint(1,20)
print('Задумано число от 1 до 20. Нужно угадать его')
#Всего 6 попыток
for guessesTaken in range(1, 7):
    print('Ваш вариант:')
    try:
        guess = int(input())
    except ValueError:
        print('Фигню ввел')
        continue

    if guess>secretNumber:
        print('Больше задуманного')
    elif guess<secretNumber:
        print('Меньше задуманного')
    else:
        break #соответсвует задуманному
if guess==secretNumber:
    print('Верно. Попыток '+str(guessesTaken))
else:
    print('Не угадал. Было задумано '+ str(secretNumber))

