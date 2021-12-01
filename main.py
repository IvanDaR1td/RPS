

import random

score = 0
COM1score = 0

while True:
    if score == 3:
        print("YOU WIN THE GAME!")
        break
    elif COM1score == 3:
        print("YOU LOSE THE GAME!!")
        break
    else:
        print("##your score is",score,"COM1 score is",COM1score,"###")

    c = input("R,P,S")
    r=random.randint(1,3)
    if r == 1:
        comC="R"
    elif r == 2:
        comC="P"
    elif r == 3:
        comC="S"

    if c == "R" and comC == "R":
        print("TIE")
    elif c == "R" and comC == "S":
        print("YOU WIN!")
        score += 1
    elif c == "R" and comC == "P":
        print("COM1 WIN!")
        COM1score += 1
    elif c == "S" and comC == "R":
        print("COM1 WIN!")
        COM1score += 1
    elif c == "S" and comC == "S":
        print("TIE")
    elif c == "S" and comC == "P":
        print("YOU WIN!")
        score += 1
    elif c == "P" and comC == "R":
        print("YOU WIN!")
        score += 1
    elif c == "P" and comC == "S":
        print("CON1 WIN!")
        COM1score += 1
    elif c == "P" and comC == "P":
        print("TIE")
