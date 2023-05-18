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

fizzbuzz(10)


# for i in range(1,11):
 #    print(i,"even?",is_even(i))

#print(0b1111&0b1)
