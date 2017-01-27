"""
The program loops over each character in the message variable’s string, counting how often each character appears.
The setdefault() method call ensures that the key is in the count dictionary (with a default value of 0) so the program
doesn’t throw a KeyError error when count[character] = count[character] + 1 is executed. When you run this program,
the output will look like this:

{' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5, 'd': 3, 'g': 2, 'i':
6, 'h': 3, 'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p': 1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1}

From the output, you can see that the lowercase letter c appears 3 times, the space character appears 13 times,
and the uppercase letter A appears 1 time. This program will work no matter what string is inside the message
variable, even if the string is millions of characters long!

"""



message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    print(character, count[character] + 1) #print the character string and add a 1 to it's count if the string comes up.
    count[character] = count[character] + 1

print(count)