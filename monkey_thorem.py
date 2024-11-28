# printing random letters for monkey theorem
import string
import random


def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]

    return res


def score(goal, teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame = numSame + 1
            return numSame / len(goal)



def main():

    goalstring ='methinks it is a wiesel'
    newstring = generateOne(26)
    while score(goalstring,newstring) < 1:
        newstring = generateOne(26)
        print(newstring)
main()
