import random

def getAnswer(answeNumber):
    if answeNumber == 1:
        return "It is certain."
    elif answeNumber == 2:
        return "It is decidedly so!"
    elif answeNumber == 3:
        return "Yes"
    elif answeNumber == 4:
        return "Reply hazy try again."
    elif answeNumber == 5:
        return "Ask again later."
    elif answeNumber == 6:
        return "Concentrate and ask again"
    elif answeNumber == 7:
        return "My reply is no."
    elif answeNumber == 8:
        return "Outlook not so good"
    elif answeNumber == 9:
        return "Very Doubtful"

print("Think of a yes/no question, and press enter to see the answer: ")
input()

print(getAnswer(random.randint(1,9)))