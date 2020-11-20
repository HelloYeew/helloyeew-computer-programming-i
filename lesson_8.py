def word_len(word):
    """Returns the length of word not counting spaces

    >>> word_len("a la carte")
    8
    >>> word_len("hello")
    5
    >>> word_len('')
    0
    >>> word_len("coup d'etat")
    10
    """
    num = len(word)
    for i in range(len(word)):
        if word[i] == " ":
            num = num-1
    return num


def has_no_e(word):
    """Returns True if word contains no e letter

    >>> has_no_e("hello")
    False
    >>> has_no_e("myopia")
    True
    """
    word.split()
    if "e" in word:
        return False
    else:
        return True



def avoids(word, forbidden):
    """Returns True if word does not contain any letter in forbidden string

    >>> avoids('yummy', 'abcdefg')
    True
    >>> avoids('dictionary', 'abcdefg')
    False
    >>> avoids('crypt', 'aeiou')
    True
    >>> avoids('tangible', 'aeiou')
    False
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True

def uses_only(word, available):
    """Returns True if each of the letters in word is contained in string

    >>> uses_only('aloha', 'acefhlo')
    True
    >>> uses_only('flow', 'acefhlo')
    False
    >>> uses_only('pizza', 'enipaz')
    True
    >>> uses_only('pineapple', 'enipaz') 
    False
    >>> uses_only('spine', 'enipaz') 
    False
    """
    ans = 0
    word.split
    available.split
    for i in range(len(word)):
        for j in range(len(available)):
            if word[i] == available[j]:
                ans += 1
                continue
    if ans == len(word):
        return True
    else:
        return False

def uses_all(word, required):
    """Returns True if each of the letters in required is contained in word

    >>> uses_all('resampling', 'aeipn')
    True
    >>> uses_all('plenty', 'aeipn')
    False
    >>> uses_all('penalize', 'enipaz')
    True
    >>> uses_all('penalty', 'enipaz')
    False
    """


def is_abecedarian(word):
    """Returns True if the letters in a word appear in alphabetical order

    >>> is_abecedarian('loop')
    True
    >>> is_abecedarian('almost')
    True
    >>> is_abecedarian('lopsided')
    False
    >>> is_abecedarian('always')
    False
    """
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True
