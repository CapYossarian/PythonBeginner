import math
def is_even(n):
    return not n & 1
def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print(i,'FizzBuzz')
        elif i%3 == 0:
            print(i,"Fizz")
        elif i%5 == 0:
            print(i,"Buzz")
        else:
            print(i)


def is_prime(n):
#простые числа
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def find_primes(n):
    return [i for i in range(2,n+1) if(is_prime(i))]

#Вывод всех простых чисел в диапозоне
print(find_primes(100))


#Делится ли на 3, 5, 3 и 5
#fizzbuzz(10)

# Четное?
# for i in range(1,11):
 #    print(i,"even?",is_even(i))

#print(0b1111&0b1)
