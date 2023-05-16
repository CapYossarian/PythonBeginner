# рекурсия Глава 2
def numrecurs(n):
    if n==1:
        return 1
    return str(numrecurs(n-1))+' '+ str(n)


print(numrecurs(10))
