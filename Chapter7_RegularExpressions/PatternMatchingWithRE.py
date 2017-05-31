pmwre = """
Chapter 7 – Pattern Matching with Regular Expressions
=====================================================
Pattern Matching with Regular Expressions
-----------------------------------------
You may be familiar with searching for text by pressing CTRL-F and typing in the words you’re looking for. 

Regular expressions go one step further: 
They allow you to specify a pattern of text to search for. 

You may not know a business’s exact phone number, but if you live in the United States or Canada, you know 
it will be three digits, followed by a hyphen, and then four more digits (and optionally, a three-digit area code at the start).

This is how you, as a human, know a phone number when you see it: 
415-555-1234 is a phone number, but 4,155,551,234 is not.

Regular expressions are helpful, but not many non-programmers know about them even though most modern text editors 
and word processors, such as Microsoft Word or OpenOffice, have find and find-and-replace features that can search 
based on regular expressions. Regular expressions are huge time-savers, not just for software users but also for 
programmers. 

In fact, tech writer Cory Doctorow argues that even before teaching programming, we should be teaching regular expressions:

“Knowing [regular expressions] can mean the difference between solving a problem in 3 steps and solving it in 3,000 steps. 
When you’re a nerd, you forget that the problems you solve with a couple keystrokes can take other people days of tedious, 
error-prone work to slog through.”[1]

In this chapter, you’ll start by writing a program to find text patterns without using regular expressions and then see
how to use regular expressions to make the code much less bloated. I’ll show you basic matching with regular expressions 
and then move on to some more powerful features, such as string substitution and creating your own character classes. 
Finally, at the end of the chapter, you’ll write a program that can automatically extract phone numbers and email 
addresses from a block of text.


Finding Patterns of Text Without Regular Expressions
====================================================
Say you want to find a phone number in a string. 

You know the pattern: three numbers, a hyphen, three numbers, a hyphen, and four numbers. 
Here’s an example: 415-555-4242.

Let’s use a function named isPhoneNumber() to check whether a string matches this pattern, returning either True or False.
 
 
Open a new file editor window and enter the following code; then save the file as isPhoneNumber.py:
   def isPhoneNumber(text):
❶     if len(text) != 12:
           return False
       for i in range(0, 3):
❷         if not text[i].isdecimal():
               return False
❸     if text[3] != '-':
           return False
       for i in range(4, 7):
❹         if not text[i].isdecimal():
               return False
❺     if text[7] != '-':
           return False
       for i in range(8, 12):
❻         if not text[i].isdecimal():
               return False
❼     return True
   print('415-555-4242 is a phone number:')
   print(isPhoneNumber('415-555-4242'))
   print('Moshi moshi is a phone number:')
   print(isPhoneNumber('Moshi moshi'))


When this program is run, the output looks like this:
415-555-4242 is a phone number:
True
Moshi moshi is a phone number:
False


The isPhoneNumber() function has code that does several checks to see whether the string in text is a valid phone number. 
If any of these checks fail, the function returns False. 

❶ First the code checks that the string is exactly 12 characters. 
❷ Then it checks that the area code (that is, the first three characters in text) consists of only numeric characters. 

The rest of the function checks that the string follows the pattern of a phone number: 
❸ The number must have the first hyphen after the area code
❹ three more numeric characters
❺ then another hyphen
❻ and finally four more numbers
❼ If the program execution manages to get past all the checks, it returns True.

Calling isPhoneNumber() with the argument '415-555-4242' will return True. 
Calling isPhoneNumber() with 'Moshi moshi' will return False; the first test fails because 'Moshi moshi' is not 12 characters long.

You would have to add even more code to find this pattern of text in a larger string. 

Replace the last four print() function calls in isPhoneNumber.py with the following:
   message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
   for i in range(len(message)):
❶     chunk = message[i:i+12]
❷     if isPhoneNumber(chunk):
         print('Phone number found: ' + chunk)
   print('Done')
   
When this program is run, the output will look like this:
Phone number found: 415-555-1011
Phone number found: 415-555-9999
Done

On each iteration of the for loop, a new chunk of 12 characters from message is assigned to the variable chunk ❶. 

For example, on the first iteration, i is 0, and chunk is assigned message[0:12] (that is, the string 'Call me at 4'). 

On the next iteration, i is 1, and chunk is assigned message[1:13] (the string 'all me at 41').

You pass chunk to isPhoneNumber() to see whether it matches the phone number pattern ❷, and if so, you print the chunk.

Continue to loop through message, and eventually the 12 characters in chunk will be a phone number. 
The loop goes through the entire string, testing each 12-character piece and printing any chunk it 
finds that satisfies isPhoneNumber(). Once we’re done going through message, we print Done.
While the string in message is short in this example, it could be millions of characters long and 
the program would still run in less than a second. 

A similar program that finds phone numbers using regular expressions would also run in less than a second, 
but regular expressions make it quicker to write these programs.


Finding Patterns of Text with Regular Expressions
=================================================
The previous phone number–finding program works, but it uses a lot of code to do something limited: 

The isPhoneNumber() function is 17 lines but can find only one pattern of phone numbers. 
What about a phone number formatted like 415.555.4242 or (415) 555-4242? 
What if the phone number had an extension, like 415-555-4242 x99?


The isPhoneNumber() function would fail to validate them. 
You could add yet more code for these additional patterns, but there is an easier way.

Regular expressions, called regexes for short, are descriptions for a pattern of text. 
For example, a \d in a regex stands for a digit character—that is, any single numeral 0 to 9.

The regex \d\d\d-\d\d\d-\d\d\d\d is used by Python to match the same text the previous isPhoneNumber() function did: 
a string of three numbers, a hyphen, three more numbers, another hyphen, and four numbers. 
Any other string would not match the \d\d\d-\d\d\d-\d\d \d\d regex.

But regular expressions can be much more sophisticated. 
For example, adding a 3 in curly brackets ({3}) after a pattern is like saying, “Match this pattern three times.” 
So the slightly shorter regex \d{3}-\d{3}-\d{4} also matches the correct phone number format.

Creating Regex Objects
======================
All the regex functions in Python are in the re module. 
Enter the following into the interactive shell to import this module:

>>> import re

Note
====
Most of the examples that follow in this chapter will require the re module, 
so remember to import it at the beginning of any script you write or any time you restart IDLE. 

Otherwise, you’ll get a NameError: name 're' is not defined error message.

Passing a string value representing your regular expression to re.compile() returns a Regex pattern object (or simply, a Regex object).

To create a Regex object that matches the phone number pattern, enter the following into the interactive shell. 
(Remember that \d means “a digit character” and \d\d\d-\d\d\d-\d\d\d\d is the regular expression for the correct phone number pattern.)

>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

Now the phoneNumRegex variable contains a Regex object.

Passing Raw Strings to re.compile( )
------------------------------------
Remember that escape characters in Python use the backslash (\). 
The string value '\\n' represents a single newline character, not a backslash followed by a lowercase n. 
You need to enter the escape character \\\ to print a single backslash. 
So '\\n' is the string that represents a backslash followed by a lowercase n. 
However, by putting an r before the first quote of the string value, you can mark the string as a raw string, which does not escape characters.

Since regular expressions frequently use backslashes in them, it is convenient to pass raw strings to the re.compile() 
function instead of typing extra backslashes. 

Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than typing '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'.

Matching Regex Objects
======================
A Regex object’s search() method searches the string it is passed for any matches to the regex. 
The search() method will return None if the regex pattern is not found in the string. 
If the pattern is found, the search() method returns a Match object. 
Match objects have a group() method that will return the actual matched text from the searched string. 
(I’ll explain groups shortly.) 

For example, enter the following into the interactive shell:

>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> print('Phone number found: ' + mo.group())
Phone number found: 415-555-4242

The mo variable name is just a generic name to use for Match objects. 
This example might seem complicated at first, but it is much shorter than the earlier isPhoneNumber.py program and does the same thing.

Here, we pass our desired pattern to re.compile() and store the resulting Regex object in phoneNumRegex. 
Then we call search() on phoneNumRegex and pass search() the string we want to search for a match. 
The result of the search gets stored in the variable mo. 
In this example, we know that our pattern will be found in the string, so we know that a Match object will be returned. 
Knowing that mo contains a Match object and not the null value None, we can call group() on mo to return the match. 
Writing mo.group() inside our print statement displays the whole match, 415-555-4242.


Review of Regular Expression Matching
======================================
While there are several steps to using regular expressions in Python, each step is fairly simple.

1. Import the regex module with import re.
2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
4. Call the Match object’s group() method to return a string of the actual matched text.

Note
====
While I encourage you to enter the example code into the interactive shell, you should also make use of web-based regular 
expression testers, which can show you exactly how a regex matches a piece of text that you enter. 
I recommend the tester at http://regexpal.com/.

More Pattern Matching with Regular Expressions
===============================================
Now that you know the basic steps for creating and finding regular expression objects with Python, 
you’re ready to try some of their more powerful pattern-matching capabilities.

Grouping with Parentheses
=========================



"""

print(pmwre)