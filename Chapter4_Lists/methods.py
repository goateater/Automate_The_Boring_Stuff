introtomethods = """

Methods  
========
Lesson 15 - Methods and the index(), append(), insert(), remove(), sort() List Methods


A method is the same thing as a function, except it is “called on” a value. For 
example, if a list value were stored in spam, you would call the index() list method 
(which I’ll explain next) on that list like so: spam.index('hello'). The method part 
comes after the value, separated by a period.

Each data type has its own set of methods. The list data type, for example, has 
several useful methods for finding, adding, removing, and otherwise manipulating 
values in a list.

Finding a Value in a List with the index() Method
==================================================
List values have an index() method that can be passed a value, and if that value 
exists in the list, the index of the value is returned. If the value isn’t in the list, then 
Python produces a ValueError error. Enter the following into the interactive shell:

>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hello')
0
>>> spam.index('heyas')
3
>>> spam.index('howdy howdy howdy')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    spam.index('howdy howdy howdy')
ValueError: 'howdy howdy howdy' is not in list

When there are duplicates of the value in the list, the index of its first appearance 
is returned. Enter the following into the interactive shell, and notice that index() 
returns 1, not 3:

>>> spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
>>> spam.index('Pooka')
1


Adding Values to Lists with the append() and insert() Methods
=============================================================
To add new values to a list, use the append() and insert() methods. Enter the 
following into the interactive shell to call the append() method on a list value 
stored in the variable spam:

>>> spam = ['cat', 'dog', 'bat']
>>> spam.append('moose')
>>> spam
['cat', 'dog', 'bat', 'moose']

The previous append() method call adds the argument to the end of the list. The 
insert() method can insert a value at any index in the list. The first argument to 
insert() is the index for the new value, and the second argument is the new value 
to be inserted. Enter the following into the interactive shell:

>>> spam = ['cat', 'dog', 'bat']
>>> spam.insert(1, 'chicken')
>>> spam
['cat', 'chicken', 'dog', 'bat']

Notice that the code is spam.append('moose') and spam.insert(1, 'chicken'), not 
spam = spam.append('moose') and spam = spam.insert(1, 'chicken'). Neither 
append() nor insert() gives the new value of spam as its return value. (In fact, the 
return value of append() and insert() is None, so you definitely wouldn’t want to 
store this as the new variable value.) Rather, the list is modified in place.
Modifying a list in place is covered in more detail later in Mutable and Immutable 
Data Types.

Methods belong to a single data type. The append() and insert() methods are list 
methods and can be called only on list values, not on other values such as strings 
or integers. Enter the following into the interactive shell, and note the 
AttributeError error messages that show up:

>>> eggs = 'hello'
>>> eggs.append('world')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    eggs.append('world')
AttributeError: 'str' object has no attribute 'append'
>>> bacon = 42
>>> bacon.insert(1, 'world')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    bacon.insert(1, 'world')
AttributeError: 'int' object has no attribute 'insert'

Removing Values from Lists with remove()
========================================
The remove() method is passed the value to be removed from the list it is called on.
Enter the following into the interactive shell:

>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('bat')
>>> spam
['cat', 'rat', 'elephant']

Attempting to delete a value that does not exist in the list will result in a 
ValueError error. For example, enter the following into the interactive shell and 
notice the error that is displayed:

>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('chicken')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    spam.remove('chicken')
ValueError: list.remove(x): x not in list


If the value appears multiple times in the list, only the first instance of the value 
will be removed. Enter the following into the interactive shell:

>>> spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
>>> spam.remove('cat')
>>> spam
['bat', 'rat', 'cat', 'hat', 'cat']


The del statement is good to use when you know the index of the value you want to remove from the list. 

The remove() method is good when you know the value you want to remove from the list.

del statement example
=====================
spam
['cat', 'chicken', 'dog', 'bear', 'moose', 'bat']
del spam[3]
spam
['cat', 'chicken', 'dog', 'moose', 'bat']

https://stackoverflow.com/questions/6146963/when-is-del-useful-in-python


Sorting the Values in a List with the sort() Method
===================================================
Lists of number values or lists of strings can be sorted with the sort() method. For 
example, enter the following into the interactive shell:

>>> spam = [2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]
>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']

You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order.
Enter the following into the interactive shell:

>>> spam.sort(reverse=True)
>>> spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']

There are three things you should note about the sort() method. First, the sort() 
method sorts the list in place; don’t try to capture the return value by writing code 
like spam = spam.sort().

Second, you cannot sort lists that have both number values and string values in 
them, since Python doesn’t know how to compare these values. Type the following 
into the interactive shell and notice the TypeError error:

>>> spam = [1, 3, 2, 4, 'Alice', 'Bob']
>>> spam.sort()
Traceback (most recent call last):
 File "<pyshell#70>", line 1, in <module>
   spam.sort()
TypeError: unorderable types: str() < int()

Third, sort() uses “ASCIIbetical order” rather than actual alphabetical order for 
sorting strings. This means uppercase letters come before lowercase letters.
Therefore, the lowercase a is sorted so that it comes after the uppercase Z. For an 
example, enter the following into the interactive shell:

>>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

If you need to sort the values in regular alphabetical order, pass str.lower for the 
key keyword argument in the sort() method call.

>>> spam = ['a', 'z', 'A', 'Z']
>>> spam.sort(key=str.lower)
>>> spam
['a', 'A', 'z', 'Z']

This causes the sort() function to treat all the items in the list as if they were 
lowercase without actually changing the values in the list.
"""

print(introtomethods)
print('\n')
print('Below is a sample output of displaying the index and value in the index')
spam = ['hello', 'hi', 'howdy', 'heyas']

for i in spam:
    print(spam.index(i), str(i)) #spam is the value while index is a method

print('\n')
print('Using the append and insert methods, which are list methods only, as displayed in the above traceback')

spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam.insert(1,'chicken') #first parameter is the index location, second is the value being inserted
print(spam)
print('\n')

print('Utilizing the remove() method')
spam = ['cat', 'bat', 'rat', 'elephant']
print('The current values in the list spam, prior to using the remove() method')
print(spam)
print('\n')

spam.remove('bat')
print('The values of spam, after using the remove() method - bat is now gone.')
print(spam)

print('\n')

print('Sorting items in a list')
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

print('\n')
print('sorting in reverse order')
spam.sort(reverse=True)
print(spam)

print('\n')
print('ASCIIbetical order sorting, which means that strings that start with a Capital letter will be listed first')
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

print('\n')
print('If there are strings with capital letters and the strings need to be passed alhpabetically, use the lower method')
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)
