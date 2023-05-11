def bubble_search_full(a_list):
    list_len = len(a_list)-1
    for i in range(list_len):
        for j in range(list_len):
            if a_list[j]>a_list[j+1]:
                a_list[j], a_list[j+1]=a_list[j+1], a_list[j]
    return a_list
def bubble_search_short(a_list):
    list_len = len(a_list)-1
    for i in range(list_len):
        noSwap = True
        for j in range(list_len-i):
            if a_list[j]>a_list[j+1]:
                a_list[j], a_list[j+1]=a_list[j+1], a_list[j]
                noSwap = False
        if noSwap:
            return a_list

    return a_list

print(bubble_search_full([32,1,9,6]))
print()
print(bubble_search_short([32,1,9,6]))