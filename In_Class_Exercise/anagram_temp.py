# create a key in a tuple form
# the key needs to contain unique characters

def remove_duplicates(s):
    """
    returns a new string with duplicates removed
    """
    str = ""
    for c in s:
        if c not in str:
            str += c
    return str

'''
print(remove_duplicates("aabbbcccc"))
print(remove_duplicates("abcd"))
print(remove_duplicates("sssstttttttttwssttttt"))
'''

def generate_key(s):
    """
    return a tuple of unique character
    """
    new_str = remove_duplicates(s)
    temp_list = list(new_str)
    temp_list.sort()
    return tuple(list(new_str).sort())

def generate_dict(s):
    """
    return a dictionary whose keys are tuples of
    unique chars and values are lists of words
    comprising those chars
    """
    d = dict()
    for each_word in word_list:
        new_key = generate_key(each_word)
        if new_key not in d:
            d[new_key] = [each_word]
        else:
            d[new_key].append(each_word)
    return d

word_list = ['tea', 'ate', 'aabbcc', 'desalt', 'lasted']
my_dict = generate_dict(word_list)
for key, value in my_dict.items():
    print(key, value)

# '''
# with open('words.txt') as f:
#     word_list = []
#     for line in f:
#         word_list.append(line[0:-1])
# '''

'''
print(generate_key("aabbbcccc"))
print(generate_key("abcd"))
print(generate_key("sssstttttttttwssttttt"))
'''
print(word_list[0:30])
print(word_list[-30:-1])

# 'aahs' => ('a', 'h', 's')
# 'zygote'

# ('a', 'h', 's') => ['aahs']
# ('z', 'y', 'g', 'o', 't', 'e') => ['zygote']

# eat ('e', 'a', 't') tea ('t', 'a', 'e')
# ('a', 'e', 't')