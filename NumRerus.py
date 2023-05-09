# рекурсия Глава 2
def NumRecurs(n):
    if n==1:
        return 1
    return str(NumRecurs(n-1))+' '+ str(n)


print(NumRecurs(10))
