dicts_explained = """

The Dictionary Data Type
========================
Like a list, a dictionary is a collection of many values. But unlike indexes for lists,
indexes for dictionaries can use many different data types, not just integers. Indexes for
dictionaries are called keys, and a key with its associated value is called a key-value pair.

In code, a dictionary is typed with braces, {}.
Enter the following into the interactive shell:

>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

This assigns a dictionary to the myCat variable. This dictionary’s keys are 'size', 'color', and 'disposition'.
The values for these keys are 'fat', 'gray', and 'loud', respectively. You can access these values through their keys:

>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur.'
'My cat has gray fur.

Dictionaries can still use integer values as keys, just like lists use integers for indexes,
but they do not have to start at 0 and can be any number.

>>> spam = {12345: 'Luggage Combination', 42: 'The Answer'}



Dictionaries vs. Lists
======================
Unlike lists, items in dictionaries are unordered.
The first item in a list named spam would be spam[0].
But there is no “first” item in a dictionary.
While the order of items matters for determining whether two lists are the same,
it does not matter in what order the key-value pairs are typed in a dictionary.
Enter the following into the interactive shell:

>>> spam = ['cats', 'dogs', 'moose']
>>> bacon = ['dogs', 'moose', 'cats']
>>> spam == bacon
False
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
>>> eggs == ham
True

Because dictionaries are not ordered, they can’t be sliced like lists.

Trying to access a key that does not exist in a dictionary will result in a KeyError error message,
much like a list’s “out-of-range” IndexError error message.
Enter the following into the interactive shell, and notice the error message that shows up because there is no 'color' key:

>>> spam = {'name': 'Zophie', 'age': 7}
>>> spam['color']
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    spam['color']
KeyError: 'color'

Though dictionaries are not ordered, the fact that you can have arbitrary values for the keys allows you to organize your data in powerful ways.
Say you wanted your program to store data about your friends’ birthdays.
You can use a dictionary with the names as keys and the birthdays as values.
Open a new file editor window and enter the following code.
Save it as birthdays.py.

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

You create an initial dictionary and store it in birthdays.
You can see if the entered name exists as a key in the dictionary with the in keyword,
just as you did for lists.
If the name is in the dictionary, you access the associated value using square brackets;
if not, you can add it using the same square bracket syntax combined with the assignment operator.

When you run this program, it will look like this:
-------------------------------------------------
Enter a name: (blank to quit)
Alice
Apr 1 is the birthday of Alice
Enter a name: (blank to quit)
Eve
I do not have birthday information for Eve
What is their birthday?
Dec 5
Birthday database updated.
Enter a name: (blank to quit)
Eve
Dec 5 is the birthday of Eve
Enter a name: (blank to quit)

Of course, all the data you enter in this program is forgotten when the program terminates.
You’ll learn how to save data to files on the hard drive in Chapter 8.


The keys(), values(), and items() Methods
=========================================
There are three dictionary methods that will return list-like values of the dictionary’s keys, values, or both keys and values: keys(), values(), and items().
The values returned by these methods are not true lists: They cannot be modified and do not have an append() method.
But these data types (dict_keys, dict_values, and dict_items, respectively) can be used in for loops.
To see how these methods work, enter the following into the interactive shell:


>>> spam = {'color': 'red', 'age': 42}
>>> for v in spam.values():
        print(v)

red
42

Here, a for loop iterates over each of the values in the spam dictionary.
A for loop can also iterate over the keys or both keys and values:


>>> for k in spam.keys():
        print(k)

color
age


>>> for i in spam.items():
        print(i)

('color', 'red')
('age', 42)


Using the keys(), values(), and items() methods, a for loop can iterate over the keys, values, or key-value pairs in a dictionary, respectively.
Notice that the values in the dict_items value returned by the items() method are tuples of the key and value.

If you want a true list from one of these methods, pass its list-like return value to the list() function.
Enter the following into the interactive shell:

>>> spam = {'color': 'red', 'age': 42}
>>> spam.keys()
dict_keys(['color', 'age'])
>>> list(spam.keys())
['color', 'age']


The list(spam.keys()) line takes the dict_keys value returned from keys() and passes it to list(), which then returns a list value of ['color', 'age'].


You can also use the multiple assignment trick in a for loop to assign the key and value to separate variables.
Enter the following into the interactive shell:

>>> spam = {'color': 'red', 'age': 42}
>>> for k, v in spam.items():
        print('Key: ' + k + ' Value: ' + str(v))

Key: age Value: 42
Key: color Value: red

Checking Whether a Key or Value Exists in a Dictionary
======================================================
Recall from the previous chapter that the in and not in operators can check whether a value exists in a list.
You can also use these operators to see whether a certain key or value exists in a dictionary.
Enter the following into the interactive shell:

>>> spam = {'name': 'Zophie', 'age': 7}
>>> 'name' in spam.keys()
True
>>> 'Zophie' in spam.values()
True
>>> 'color' in spam.keys()
False
>>> 'color' not in spam.keys()
True
>>> 'color' in spam
False

In the previous example, notice that 'color' in spam is essentially a shorter version of writing 'color' in spam.keys().
This is always the case:
If you ever want to check whether a value is (or isn’t) a key in the dictionary, you can simply use the in (or not in)
keyword with the dictionary value itself.

The get() Method
================
It’s tedious to check whether a key exists in a dictionary before accessing that key’s value.
Fortunately, dictionaries have a get() method that takes two arguments:
the key of the value to retrieve and a fallback value to return if that key does not exist.

Enter the following into the interactive shell:

>>> picnicItems = {'apples': 5, 'cups': 2}
>>> 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing 2 cups.'
>>> 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
'I am bringing 0 eggs.'

Because there is no 'eggs' key in the picnicItems dictionary, the default value 0 is returned by the get() method.
Without using get(), the code would have caused an error message, such as in the following example:

>>> picnicItems = {'apples': 5, 'cups': 2}
>>> 'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
KeyError: 'eggs'


The setdefault() Method
=======================
You’ll often have to set a value in a dictionary for a certain key only if that key does not already have a value.
The code looks something like this:

spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

The setdefault() method offers a way to do this in one line of code.
The first argument passed to the method is the key to check for, and
the second argument is the value to set at that key if the key does not exist.
If the key does exist, the setdefault() method returns the key’s value.
Enter the following into the interactive shell:

>>> spam = {'name': 'Pooka', 'age': 5}
>>> spam.setdefault('color', 'black')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
>>> spam.setdefault('color', 'white')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}


The first time setdefault() is called, the dictionary in spam changes to {'color': 'black', 'age': 5, 'name': 'Pooka'}.
The method returns the value 'black' because this is now the value set for the key 'color'.
When spam.setdefault('color', 'white') is called next, the value for that key is not changed to 'white' because spam already has a key named 'color'.

The setdefault() method is a nice shortcut to ensure that a key exists.
Here is a short program that counts the number of occurrences of each letter in a string.
Open the file editor window and enter the following code, saving it as characterCount.py:

Details and code are in characterCount.py

Pretty Printing
===============
If you import the pprint module into your programs, you’ll have access to the
pprint() and pformat() functions that will “pretty print” a dictionary’s values.

This is helpful when you want a cleaner display of the items in a dictionary than what print() provides.
Modify the previous characterCount.py program and save it as prettyCharacterCount.py.

This time, when the program is run, the output looks much cleaner, with the keys sorted.

{' ': 13,
 ',': 1,
 '.': 1,
 'A': 1,
 'I': 1,
 'a': 4,
 'b': 1,
 'c': 3,
 'd': 3,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 6,
 'k': 2,
 'l': 3,
 'n': 4,
 'o': 2,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 2,
 'y': 1}

The pprint.pprint() function is especially helpful when the dictionary itself contains nested lists or dictionaries.

If you want to obtain the prettified text as a string value instead of displaying it on the screen,
call pprint.pformat() instead. These two lines are equivalent to each other:

pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))


Using Data Structures to Model Real-World Things
================================================
Even before the Internet, it was possible to play a game of chess with someone on the other side of the world.
Each player would set up a chessboard at their home and then take turns mailing a postcard to each other describing each move.
To do this, the players needed a way to unambiguously describe the state of the board and their moves.

In algebraic chess notation, the spaces on the chessboard are identified by a number and letter coordinate, as in Figure 5-1.

Figure 5-1. The coordinates of a chessboard in algebraic chess notation
-----------------------------------------------------------------------
https://automatetheboringstuff.com/images/000002.jpg

The chess pieces are identified by letters: K for king, Q for queen, R for rook, B for bishop, and N for knight.
Describing a move uses the letter of the piece and the coordinates of its destination.
A pair of these moves describes what happens in a single turn (with white going first); for instance, the notation 2.
Nf3 Nc6 indicates that white moved a knight to f3 and black moved a knight to c6 on the second turn of the game.


There’s a bit more to algebraic notation than this, but the point is that you can use it to unambiguously describe
a game of chess without needing to be in front of a chessboard. Your opponent can even be on the other side of the
world! In fact, you don’t even need a physical chess set if you have a good memory: You can just read the mailed
chess moves and update boards you have in your imagination.

Computers have good memories.
A program on a modern computer can easily store billions of strings like '2. Nf3 Nc6'.
This is how computers can play chess without having a physical chessboard.
They model data to represent a chessboard, and you can write code to work with this model.

This is where lists and dictionaries can come in.
You can use them to model real-world things, like chessboards.
For the first example, you’ll use a game that’s a little simpler than chess: tic-tac-toe.

A Tic-Tac-Toe Board
====================
A Tic-Tac-Toe Board

A tic-tac-toe board looks like a large hash symbol (#) with nine slots that can each contain an X, an O, or a blank.
To represent the board with a dictionary, you can assign each slot a string-value key, as shown in Figure 5-2.

You can use string values to represent what’s in each slot on the board: 'X', 'O', or ' ' (a space character).
Thus, you’ll need to store nine strings.
You can use a dictionary of values for this.
The string value with the key 'top-R' can represent the top-right corner, the string value with the key
'low-L' can represent the bottom-left corner, the string value with the key 'mid-M' can represent the middle, and so on.

Figure 5-2. The slots of a tic-tactoe board with their corresponding keys
-------------------------------------------------------------------------
https://automatetheboringstuff.com/images/000003.png


This dictionary is a data structure that represents a tic-tac-toe board.
Store this board-as-a-dictionary in a variable named theBoard.
Open a new file editor window, and enter the following source code, saving it as ticTacToe.py:

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

The data structure stored in the theBoard variable represents the tic-tactoe board in Figure 5-3.

Figure 5-3. An empty tic-tac-toe board
--------------------------------------
https://automatetheboringstuff.com/images/000006.png


Since the value for every key in theBoard is a single-space string, this dictionary represents a completely clear board.
If player X went first and chose the middle space, you could represent that board with this dictionary:

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

The data structure in theBoard now represents the tic-tac-toe board in Figure 5-4.

Figure 5-4. The first move
--------------------------
https://automatetheboringstuff.com/images/000008.png

A board where player O has won by placing Os across the top might look like this:

theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}


The data structure in theBoard now represents the tic-tac-toe board in Figure 5-5.

Figure 5-5. Player O wins.
--------------------------
https://automatetheboringstuff.com/images/000010.png

Of course, the player sees only what is printed to the screen, not the contents of variables.
Let’s create a function to print the board dictionary onto the screen.
Make the following addition to ticTacToe.py (new code is in bold):

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

When you run this program, printBoard() will print out a blank tic-tactoe board.

| |
-+-+-
| |
-+-+-
| |


The printBoard() function can handle any tic-tac-toe data structure you pass it.
Try changing the code to the following:

theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)


Now when you run this program, the new board will be printed to the screen.

O|O|O
-+-+-
X|X|
-+-+-
| |X

Because you created a data structure to represent a tic-tac-toe board and wrote code in printBoard()
to interpret that data structure, you now have a program that “models” the tic-tac-toe board. You
could have organized your data structure differently (for example, using keys like 'TOP-LEFT' instead of 'top-L'),
but as long as the code works with your data structures, you will have a correctly working program.

For example, the printBoard() function expects the tic-tac-toe data structure to be a dictionary with keys
for all nine slots. If the dictionary you passed was missing, say, the 'mid-L' key, your program would no longer work.

O|O|O
-+-+-
Traceback (most recent call last):
  File "ticTacToe.py", line 10, in <module>
    printBoard(theBoard)
  File "ticTacToe.py", line 6, in printBoard
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
KeyError: 'mid-L'

Now let’s add code that allows the players to enter their moves.
Modify the ticTacToe.py program to look like this:

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': '
   ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

   def printBoard(board):
       print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
       print('-+-+-')
       print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
       print('-+-+-')
       print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
   turn = 'X'
   for i in range(9):
       printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
       theBoard[move] = turn
       if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
   printBoard(theBoard)

The new code prints out the board at the start of each new turn, gets the active player’s move, updates the game board
accordingly, and then swaps the active player before moving on to the next turn.

When you run this program, it will look something like this:

 | |
-+-+-
 | |
-+-+-
 | |
Turn for X. Move on which space?
mid-M
 | |
-+-+-
 |X|
-+-+-
 | |
Turn for O. Move on which space?
low-L
 | |
-+-+-
 |X|
-+-+-
O| |

--snip--

O|O|X
-+-+-
X|X|O
-+-+-
O| |X
Turn for X. Move on which space?
low-M
O|O|X
-+-+-
X|X|O
-+-+-
O|X|X

This isn’t a complete tic-tac-toe game—for instance, it doesn’t ever check whether a player has won—but
it’s enough to see how data structures can be used in programs.


Note
====
If you are curious, the source code for a complete tic-tac-toe program is described
in the resources available from http://nostarch.com/automatestuff/.


"""

print(dicts_explained)
