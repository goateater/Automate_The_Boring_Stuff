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



"""

print(dicts_explained)