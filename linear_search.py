#линейный поиск
def linear_search(a_list, n):
    for i in a_list:
        if i==n:
            return True
    return False

a_list = [1, 16, 8, 91, 1971]
print(linear_search(a_list,90))