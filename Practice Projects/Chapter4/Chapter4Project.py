project4 = """

Practice Projects

For practice, write programs to do the following tasks.
Comma Code

Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by
a comma and a space, with and inserted before the last item.
For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.

Character Picture Grid

Say you have a list of lists where each value in the inner lists is a one-character string, like this:

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

You can think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters.
The (0, 0) origin will be in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase
going down.

Copy the previous grid value, and write code that uses it to print the image.

..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then grid[2][0], and so on, up to grid[8][0].
This will finish the first row, so then print a newline.
Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on.
The last thing your program will print is grid[8][5].

Also, remember to pass the end keyword argument to print() if you don’t want a newline printed automatically after each print() call.

"""

print(project4)

stringconversion = """

How does one convert a list to a string?
========================================
By using ''.join

list1 = ['1', '2', '3']
str1 = ''.join(list1)

Or if the list is of integers, convert the elements before joining them.

list1 = [1, 2, 3]
str1 = ''.join(str(e) for e in list1)

"""

print(stringconversion)

print('Chapter 4 - Excercise 1')
print('-----------------------')
def comma(mylist):
    newlist = []
    for i in range(len(mylist) -1):
        newlist.append(mylist[i]+',')
        #print(newlist)
    newlist.append('and '+mylist[-1])
    #print(newlist)
    stringconvert = "".join(newlist)
    print(stringconvert)
    print(type(stringconvert))


mylist = ['apples', 'bananas', 'tofu', 'cats']
(comma(mylist))

print()
print('Chapter 4 - Excercise 2')
print('Completed two seperate ways')
print('----------------------------')


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


newstring = ''
newstring1 = '\n'
newstring2 = '\n'
newstring3 = '\n'
newstring4 = '\n'
newstring5  = '\n'
for i in range(len(grid)):
    newstring = newstring + str(grid[i][0])
    newstring1 = newstring1 + str(grid[i][1])
    newstring2 = newstring2 + str(grid[i][2])
    newstring3 = newstring3 + str(grid[i][3])
    newstring4 = newstring4 + str(grid[i][4])
    newstring5 = newstring5 + str(grid[i][5])
heart = newstring + newstring1 +newstring2 + newstring3 + newstring4 + newstring5
print(heart)

print()

for i in range(len(grid[0])):
    print()
    for j in range(len(grid)):
        print(grid[j][i], end='')

