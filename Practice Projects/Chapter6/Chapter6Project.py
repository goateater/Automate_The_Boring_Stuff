project6 = """

Project: Password Locker
========================
You probably have accounts on many different websites. 
It’s a bad habit to use the same password for each of them because if any of those sites has a security breach, 
the hackers will learn the password to all of your other accounts. 

It’s best to use password manager software on your computer that uses one master password to unlock the password manager. 
Then you can copy any account password to the clipboard and paste it into the website’s Password field.

The password manager program you’ll create in this example isn’t secure, but it offers a basic demonstration of how such programs work.

The Chapter Projects

This is the first “chapter project” of the book. 

From here on, each chapter will have projects that demonstrate the concepts covered in the chapter. 

The projects are written in a style that takes you from a blank file editor window to a full, working program. 
Just like with the interactive shell examples, don’t only read the project sections—follow along on your computer!


Step 1: Program Design and Data Structures
==========================================
You want to be able to run this program with a command line argument that is the account’s name—for instance, email or blog. 
That account’s password will be copied to the clipboard so that the user can paste it into a Password field. 
This way, the user can have long, complicated passwords without having to memorize them.

Open a new file editor window and save the program as pw.py. 
You need to start the program with a #! (shebang) line (see Appendix B) and should also write a comment that briefly 
describes the program. 

Since you want to associate each account’s name with its password, you can store these as strings in a dictionary. 
The dictionary will be the data structure that organizes your account and password data. 

Make your program look like the following:

#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}


Step 2: Handle Command Line Arguments
=====================================
The command line arguments will be stored in the variable sys.argv. 
(See Appendix B for more information on how to use command line arguments in your programs.) 

The first item in the sys.argv list should always be a string containing the program’s filename ('pw.py'), 
and the second item should be the first command line argument. 

For this program, this argument is the name of the account whose password you want. 
Since the command line argument is mandatory, you display a usage message to the user if they forget to add it 
(that is, if the sys.argv list has fewer than two values in it). 

Make your program look like the following:
------------------------------------------

#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name

Step 3: Copy the Right Password
===============================
Now that the account name is stored as a string in the variable account, 
you need to see whether it exists in the PASSWORDS dictionary as a key. 

If so, you want to copy the key’s value to the clipboard using pyperclip.copy(). 
(Since you’re using the pyperclip module, you need to import it.) 

Note that you don’t actually need the account variable; you could just use sys.argv[1] 
everywhere account is used in this program. But a variable named account is much more 
readable than something cryptic like sys.argv[1].

Make your program look like the following:
------------------------------------------

#! python3
# pw.py - An insecure password locker program.
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    

This new code looks in the PASSWORDS dictionary for the account name. 
If the account name is a key in the dictionary, we get the value corresponding to that key, 
copy it to the clipboard, and print a message saying that we copied the value. 

Otherwise, we print a message saying there’s no account with that name.
That’s the complete script. 

Using the instructions in Appendix B for launching command line programs easily, 
you now have a fast way to copy your account passwords to the clipboard. 

You will have to modify the PASSWORDS dictionary value in the source whenever 
you want to update the program with a new password.

Of course, you probably don’t want to keep all your passwords in one place where anyone 
could easily copy them. 

But you can modify this program and use it to quickly copy regular text to the clipboard. 
Say you are sending out several emails that have many of the same stock paragraphs in common. 

You could put each paragraph as a value in the PASSWORDS dictionary 
(you’d probably want to rename the dictionary at this point), and then 
you would have a way to quickly select and copy one of many standard pieces 
of text to the clipboard.

On Windows, you can create a batch file to run this program with the WIN-R Run window. 
(For more about batch files, see Appendix B.) 
Type the following into the file editor and save the file as pw.bat in the C:\Windows folder:

@py.exe C:\Python34\pw.py %*
@pause

With this batch file created, running the password-safe program on Windows is just a matter of pressing WIN-R and typing pw <account name>.

Project: Adding Bullets to Wiki Markup
=======================================
When editing a Wikipedia article, you can create a bulleted list by putting each list item on its own line and placing a 
star in front. But say you have a really large list that you want to add bullet points to. You could just type those 
stars at the beginning of each line, one by one. Or you could automate this task with a short Python script.

The bulletPointAdder.py script will get the text from the clipboard, add a star and space to the beginning of each line, 
and then paste this new text to the clipboard. For example, if I copied the following text (for the Wikipedia article 
“List of Lists of Lists”) to the clipboard:


Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
and then ran the bulletPointAdder.py program, the clipboard would then contain the following:


* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars

This star-prefixed text is ready to be pasted into a Wikipedia article as a bulleted list.

Step 1: Copy and Paste from the Clipboard
==========================================
You want the bulletPointAdder.py program to do the following:

Paste text from the clipboard

Do something to it

Copy the new text to the clipboard

That second step is a little tricky, but steps 1 and 3 are pretty straightforward: 
They just involve the pyperclip.copy() and pyperclip.paste() functions. 
For now, let’s just write the part of the program that covers steps 1 and 3. 
Enter the following, saving the program as bulletPointAdder.py:

#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars.

pyperclip.copy(text)


The TODO comment is a reminder that you should complete this part of the program eventually. 
The next step is to actually implement that piece of the program

Step 2: Separate the Lines of Text and Add the Star
===================================================
The call to pyperclip.paste() returns all the text on the clipboard as one big string. 
If we used the “List of Lists of Lists” example, the string stored in text would look like this:


'Lists of animals\nLists of aquarium life\\nLists of biologists by author
abbreviation\nLists of cultivars'
The \\n newline characters in this string cause it to be displayed with multiple lines when it is 
printed or pasted from the clipboard. There are many “lines” in this one string value. 
You want to add a star to the start of each of these lines.

You could write code that searches for each \\n newline character in the string and then adds the star 
just after that. But it would be easier to use the split() method to return a list of strings, one for 
each line in the original string, and then add the star to the front of each string in the list.

Make your program look like the following:


#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

pyperclip.copy(text)


We split the text along its newlines to get a list in which each item is one line of the text. 
We store the list in lines and then loop through the items in lines. 
For each line, we add a star and a space to the start of the line.
Now each string in lines begins with a star.

Step 3: Join the Modified Lines
===============================
The lines list now contains modified lines that start with stars. 
But pyperclip.copy() is expecting a single string value, not a list of string values. 
To make this single string value, pass lines into the join() method to get a single string joined from the list’s strings. 
Make your program look like the following:


#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)


When this program is run, it replaces the text on the clipboard with text that has stars at the start of each line. 
Now the program is complete, and you can try running it with text copied to the clipboard.

Even if you don’t need to automate this specific task, you might want to automate some other kind of text manipulation, 
such as removing trailing spaces from the end of lines or converting text to uppercase or lowercase. 

Whatever your needs, you can use the clipboard for input and output.

Summary
=======
Text is a common form of data, and Python comes with many helpful string methods to process the text stored in string values. 
You will make use of indexing, slicing, and string methods in almost every Python program you write.

The programs you are writing now don’t seem too sophisticated—they don’t have graphical user interfaces with images and colorful text. 
So far, you’re displaying text with print() and letting the user enter text with input(). 
However, the user can quickly enter large amounts of text through the clipboard. 
This ability provides a useful avenue for writing programs that manipulate massive amounts of text. 
These text-based programs might not have flashy windows or graphics, but they can get a lot of useful work done quickly.

Another way to manipulate large amounts of text is reading and writing files directly off the hard drive. 
You’ll learn how to do this with Python in the next chapter.

That just about covers all the basic concepts of Python programming! 
You’ll continue to learn new concepts throughout the rest of this book, 
but you now know enough to start writing some useful programs that can automate tasks. 

You might not think you have enough Python knowledge to do things such as download web pages, 
update spreadsheets, or send text messages, but that’s where Python modules come in! 

These modules, written by other programmers, provide functions that make it easy for you to do all these things. 
So let’s learn how to write real programs to do useful automated tasks.

"""

import sys

print(project6)
print()
print("The below output is testing out sys.argv[0] to see what gets displayed")
print("This is sys.argv[0] - script name and path: " ,sys.argv[0])
