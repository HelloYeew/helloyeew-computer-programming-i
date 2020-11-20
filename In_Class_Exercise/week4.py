def change_second_char(s, c):
    return s[0] + c + s[2:]

print(change_second_char("bald", "o"))
print(change_second_char("stitch", "w"))
print(change_second_char("shell","m"))
print()

def change_index_char(s, c, i):
    if i >= len(s) or i < -len(s):
        return "Error: index out of range"
    return s[0:i] + c + s[i+1:]

print(change_index_char("bald","m",3))
print(change_index_char("bald","o",-3))
print(change_index_char("bald","m",4))
print(change_index_char("bald","m",-5))
print()

def fix_start(s):
    result = ""
    to_replace = s[0]
    for c in s[1:]:
        if c == to_replace:
            result += '*'
        else:
            result += c
    return to_replace + result

print(fix_start('babble'))
print(fix_start("electrotelethermometer"))
print()

def verbings(s):
    if len(s) < 3:
        return s
    else:
        if s[-3:] == 'ing':
            return s + 'ly'
        else:
            return s + 'ing'

print(verbings('mix'))
print(verbings('mixing'))
print(verbings('is'))
print(verbings('screen'))
print(verbings('screening'))
print(verbings('to'))
print()

def ll_sum(l_of_l):
    acc = 0
    for element in l_of_l:
        acc += sum(element)
    return acc

print(ll_sum([[1, 2], [3], [4, 5, 6]]))
print()

def middle(input_list):
    new_list = []
    for element in input_list[1:-1]:
        new_list += [element]
    return new_list

print(middle([1, 2, 3, 4]))
print(middle(["hello", 2, "sawasdee", 76.5, 4, True]))
print()

def even_only(int_list):
    result_list = []
    for element in int_list:
        if element % 2 == 0:
            result_list += [element]
    return result_list

print(even_only([3, 1, 4, 1, 5, 9, 2, 6, 5]))
print()

def has_duplicates(input_list):
    for ind in range(len(input_list) - 1):
        if input_list[ind] in input_list[ind+1:]:
            return True
    return False

print(has_duplicates([1, 2, 3, 4, 5]))
print(has_duplicates([1, 2, 3, 4, 5, 2]))