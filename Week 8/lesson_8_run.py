import lesson_8

fin = open('words.txt')
word_list = []
for line in fin:
    word = line.strip()
    word_list.append(word)
fin.close()

# P1
for word in word_list:
    if lesson_8.word_len(word)
        print(word)

# P2
num_no_e = 0
for word in word_list:
    if lesson_8.has_no_e(word):
        num_no_e += 1
        print(word)
print("Number of no e words:", num_no_e)
print("Number of word:" ,len(word_list))
print("Percentage of no e words: ", num_no_e/len(word_list))

# P3
forbidden_letters = input("Provide a string of forbidden letters: ")
num_no_forbidden_letters = 0
forbidden_word_list = []
for word in word_list:
    if lesson_8.avoids(word, forbidden_letters):
        num_no_forbidden_letters += 1
        forbidden_word_list.append(word)
print("Number of such words: ", num_no_forbidden_letters)
print(forbidden_word_list[:5])

# P4
num_all_vowels = 0
all_vowels_word_list = []
for word in word_list:
    if lesson_8.uses_all(word, 'aeiou'):
        num_all_vowels += 1
        all_vowels_word_list.append(word)
print("Number of such words:", num_all_vowels)
print(all_vowels_word_list[:10])

# P5
num_all_abcedarian = 0
all_abcedarian_word_list = []
for word in word_list:
    if lesson_8.is_abecedarian(word):
        if lesson_8.word_len(word) > 10:
            num_all_abcedarian += 1
            all_abcedarian_word_list.append(word)
print("Number of such words:", num_all_abcedarian)
print(all_abcedarian_word_list[:10])

