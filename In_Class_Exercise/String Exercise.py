def change_second_char(text,char):
    return text[0] + char + text[2:]

print(change_second_char("bald","o"))

def change_index_char(s, c, i):
    return s[0:c] + c + s[c+1:]

print(change_index_char("bald","m",-3))

def fix_starts(s):
    result = ""
    to_replace = s[0]
    for c in s:
        if c == to_replace:
            result += '*'
        else:
            result += c
    return result

print(fix_starts('babble'))