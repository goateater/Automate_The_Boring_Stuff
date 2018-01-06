import random


def getAnswer(answernumber):
    if answernumber == 1:
        return "It is certain."
    elif answernumber == 2:
        return "It is decidedly so!"
    elif answernumber == 3:
        return "Yes"
    elif answernumber == 4:
        return "Reply hazy try again."
    elif answernumber == 5:
        return "Ask again later."
    elif answernumber == 6:
        return "Concentrate and ask again"
    elif answernumber == 7:
        return "My reply is no."
    elif answernumber == 8:
        return "Outlook not so good"
    elif answernumber == 9:
        return "Very Doubtful"

# r = random.randint(1,9)
# fortune = getAnswer(r)
# print(fortune)

print("Think of a yes/no question, and press enter to see the answer: ")
input()
print(getAnswer(random.randint(1,9)))