import random
import sys


# function zone
def append_char_from_ans(answer):
    global gamelist, right_answer
    for a in range(len(right_answer)):
        if answer == right_answer[a]:
            gamelist[a] = answer


# shuffle the answer
shuffle = random.choice(["python", "java", "kotlin", "javascript"])
right_answer = list(shuffle)

# build blank list
gamelist = []
for i in range(len(shuffle)):
    gamelist.append("-")

# main zone
print("H A N G M A N")
live = 8
while live > 0:
    print()
    for i in range(len(shuffle)):
        print(gamelist[i], end='')
    print()
    if gamelist == right_answer:
        print("You guessed the word!")
        print("You survived!")
        sys.exit()
    ans = str(input("Input a letter: "))
    if ans in right_answer:
        if ans in gamelist:
            print("No improvements")
            live -= 1
        else:
            append_char_from_ans(ans)
    elif ans not in right_answer:
        print("No such letter in the word")
        live -= 1
print("You are hanged!")
