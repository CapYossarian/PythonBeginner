#последовательность Коллатца, простейшая из неразрешимых задач математики
#функция принимает целое значение, если оно четное, возвращает number // 2
#если нечетное 3 * number + 1
#рано или поздно вернет 1
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return (number // 2)
    else:
        print(3 * number + 1)
        return (3 * number + 1)


print("Введите число:")
try:
    num = int(input())
except ValueError:
    print("Нужно было ввести целое число!")
    exit()
num = collatz(num)
while num != 1:
    num = collatz(num)
