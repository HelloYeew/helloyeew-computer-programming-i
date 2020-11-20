def even_only(int_list):
    result_list = []
    for element in int_list:
        if element % 2 == 0:
            result_list += [element]
    return result_list
print(even_only([3,1,4,1,5,9,2,6,5]))

def called_middle(list):
    