magic8ballNotes = """
Example Program: Magic 8 Ball with a List

Using lists, you can write a much more elegant version of the previous chapter’s 
Magic 8 Ball program. Instead of several lines of nearly identical elif statements, 
you can create a single list that the code works with.  Open a new file editor window 
and enter the following code.  Save it as magic8Ball2.py.

#### magic8Ball2.py code start ####

import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])

#### magic8Ball2.py code end ####

Exceptions to Indentation Rules in Python
=========================================
In most cases, the amount of indentation for a line of code tells Python what block 
it is in. There are some exceptions to this rule, however. For example, lists can 
actually span several lines in the source code file. The indentation of these lines do 
not matter; Python knows that until it sees the ending square bracket, the list is 
not finished. For example, you can have code that looks like this:

spam = ['apples',
    'oranges',
                     'bananas',
'cats']
print(spam)


Of course, practically speaking, most people use Python’s behavior to make their 
lists look pretty and readable, like the messages list in the Magic 8 Ball program.

You can also split up a single instruction across multiple lines using the \ line 
continuation character at the end. Think of \ as saying, “This instruction continues 
on the next line.” The indentation on the line after a \ line continuation is not 
significant. For example, the following is valid Python code:

print('Four score and seven ' + \
      'years ago...')

These tricks are useful when you want to rearrange long lines of Python code to be 
a bit more readable.

When you run this program, you’ll see that it works the same as the previous 
magic8Ball.py program.

Notice the expression you use as the index into messages: random.randint(0, 
len(messages) - 1). This produces a random number to use for the index, 
regardless of the size of messages. That is, you’ll get a random number between 0 
and the value of len(messages) - 1. The benefit of this approach is that you can 
easily add and remove strings to the messages list without changing other lines of 
code. If you later update your code, there will be fewer lines you have to change 
and fewer chances for you to introduce bugs.


List-like Types: Strings and Tuples
===================================
Lists aren’t the only data types that represent ordered sequences of values. For 
example, strings and lists are actually similar, if you consider a string to be a “list” 
of single text characters. Many of the things you can do with lists can also be done 
with strings: indexing; slicing; and using them with for loops, with len(), and with 
the in and not in operators. To see this, enter the following into the interactive shell:

>>> name = 'Zophie'
>>> name[0]
'Z'
>>> name[-2]
'i'
>>> name[0:4]
'Zoph'
>>> 'Zo' in name
True
>>> 'z' in name
False
>>> 'p' not in name
False
>>> for i in name:
        print('* * * ' + i + ' * * *')

* * * Z * * *
* * * o * * *
* * * p * * *
* * * h * * *
* * * i * * *
* * * e * * *

Mutable and Immutable Data Types
================================
But lists and strings are different in an important way. A list value is a mutable 
data type: It can have values added, removed, or changed. However, a string is 
immutable: It cannot be changed. Trying to reassign a single character in a string 
results in a TypeError error, as you can see by entering the following into the 
interactive shell:

>>> name = 'Zophie a cat'
>>> name[7] = 'the'
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    name[7] = 'the'
TypeError: 'str' object does not support item assignment

The proper way to “mutate” a string is to use slicing and concatenation to build a 
new string by copying from parts of the old string. Enter the following into the 
interactive shell:

>>> name = 'Zophie a cat'
>>> newName = name[0:7] + 'the' + name[8:12]
>>> name
'Zophie a cat'
>>> newName
'Zophie the cat'

We used [0:7] and [8:12] to refer to the characters that we don’t wish to replace.
Notice that the original 'Zophie a cat' string is not modified because strings are 
immutable.

Although a list value is mutable, the second line in the following code does not 
modify the list eggs:

>>> eggs = [1, 2, 3]
>>> eggs = [4, 5, 6]
>>> eggs
[4, 5, 6]

The list value in eggs isn’t being changed here; rather, an entirely new and 
different list value ([4, 5, 6]) is overwriting the old list value ([1, 2, 3]).
This is depicted in Figure 4-2.

If you wanted to actually modify the original list in eggs to contain [4, 5, 6], you 
would have to do something like this:

>>> eggs = [1, 2, 3]
>>> del eggs[2]
>>> del eggs[1]
>>> del eggs[0]
>>> eggs.append(4)
>>> eggs.append(5)
>>> eggs.append(6)
>>> eggs
[4, 5, 6]


Figure 4-2. - https://automatetheboringstuff.com/images/000076.jpg
When eggs = [4, 5, 6] is executed, the contents of eggs are replaced 
with a new list value.

In the first example, the list value that eggs ends up with is the same list value it 
started with. It’s just that this list has been changed, rather than overwritten.
Figure 4-3 depicts the seven changes made by the first seven lines in the previous 
interactive shell example.

Figure 4-3. - https://automatetheboringstuff.com/images/000078.jpg
The del statement and the append() method modify the same list value 
in place.

Changing a value of a mutable data type (like what the del statement and append() 
method do in the previous example) changes the value in place, since the variable’s 
value is not replaced with a new list value.

Mutable versus immutable types may seem like a meaningless distinction, but 
Passing References will explain the different behavior when calling functions with 
mutable arguments versus immutable arguments. But first, let’s find out about the 
tuple data type, which is an immutable form of the list data type.

Passing References - https://automatetheboringstuff.com/chapter4/#calibre_link-128

The Tuple Data Type
==================
The tuple data type is almost identical to the list data type, except in two ways.
First, tuples are typed with parentheses, ( and ), instead of square brackets, [ and ].
For example, enter the following into the interactive shell:

>>> eggs = ('hello', 42, 0.5)
>>> eggs[0]
'hello'
>>> eggs[1:3]
(42, 0.5)
>>> len(eggs)
3

But the main way that tuples are different from lists is that tuples, like strings, are 
immutable. Tuples cannot have their values modified, appended, or removed.
Enter the following into the interactive shell, and look at the TypeError error 
message:

>>> eggs = ('hello', 42, 0.5)
>>> eggs[1] = 99
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    eggs[1] = 99
TypeError: 'tuple' object does not support item assignment

If you have only one value in your tuple, you can indicate this by placing a trailing 
comma after the value inside the parentheses. Otherwise, Python will think you’ve 
just typed a value inside regular parentheses. The comma is what lets Python know 
this is a tuple value. (Unlike some other programming languages, in Python it’s 
fine to have a trailing comma after the last item in a list or tuple.) Enter the 
following type() function calls into the interactive shell to see the distinction:

>>> type(('hello',))
<class 'tuple'>
>>> type(('hello'))
<class 'str'>

You can use tuples to convey to anyone reading your code that you don’t intend for 
that sequence of values to change. If you need an ordered sequence of values that 
never changes, use a tuple. A second benefit of using tuples instead of lists is that, 
because they are immutable and their contents don’t change, Python can 
implement some optimizations that make code using tuples slightly faster than 
code using lists.


Converting Types with the list() and tuple() Functions
======================================================
Just like how str(42) will return '42', the string representation of the integer 42, 
the functions list() and tuple() will return list and tuple versions of the values 
passed to them. Enter the following into the interactive shell, and notice that the 
return value is of a different data type than the value passed:

>>> tuple(['cat', 'dog', 5])
('cat', 'dog', 5)
>>> list(('cat', 'dog', 5))
['cat', 'dog', 5]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']

Converting a tuple to a list is handy if you need a mutable version of a tuple value.

References
==========
As you’ve seen, variables store strings and integer values. Enter the following into 
the interactive shell:

>>> spam = 42
>>> cheese = spam
>>> spam = 100
>>> spam
100
>>> cheese
42

You assign 42 to the spam variable, and then you copy the value in spam and assign 
it to the variable cheese. When you later change the value in spam to 100, this 
doesn’t affect the value in cheese. This is because spam and cheese are different 
variables that store different values.

But lists don’t work this way. When you assign a list to a variable, you are actually 
assigning a list reference to the variable. A reference is a value that points to some 
bit of data, and a list reference is a value that points to a list. Here is some code 
that will make this distinction easier to understand. Enter this into the interactive 
shell:

❶ >>> spam = [0, 1, 2, 3, 4, 5]
❷ >>> cheese = spam
❸ >>> cheese[1] = 'Hello!'
   >>> spam
   [0, 'Hello!', 2, 3, 4, 5]
   >>> cheese
   [0, 'Hello!', 2, 3, 4, 5]

This might look odd to you. The code changed only the cheese list, but it seems 
that both the cheese and spam lists have changed.

When you create the list ❶, you assign a reference to it in the spam variable. But 
the next line ❷ copies only the list reference in spam to cheese, not the list value 
itself. This means the values stored in spam and cheese now both refer to the same 
list. There is only one underlying list because the list itself was never actually 
copied. So when you modify the first element of cheese ❸, you are modifying the 
same list that spam refers to.

Remember that variables are like boxes that contain values. The previous figures 
in this chapter show that lists in boxes aren’t exactly accurate because list variables 
don’t actually contain lists—they contain references to lists. (These references will 
have ID numbers that Python uses internally, but you can ignore them.) Using 
boxes as a metaphor for variables, Figure 4-4 shows what happens when a list is 
assigned to the spam variable.

Figure 4-4 - https://automatetheboringstuff.com/images/000081.jpg
spam = [0, 1, 2, 3, 4, 5] stores a reference to a list, not the actual list.

Then, in Figure 4-5, the reference in spam is copied to cheese. Only a new reference 
was created and stored in cheese, not a new list. Note how both references refer to 
the same list.


Figure 4-5 - https://automatetheboringstuff.com/images/000082.jpg
spam = cheese copies the reference, not the list.

When you alter the list that cheese refers to, the list that spam refers to is also 
changed, because both cheese and spam refer to the same list. You can see this in 
Figure 4-6.

Figure 4-6 - https://automatetheboringstuff.com/images/000071.jpg
cheese[1] = 'Hello!' modifies the list that both variables refer to.

Variables will contain references to list values rather than list values themselves.
But for strings and integer values, variables simply contain the string or integer 
value. Python uses references whenever variables must store values of mutable 
data types, such as lists or dictionaries. For values of immutable data types such as 
strings, integers, or tuples, Python variables will store the value itself.

Although Python variables technically contain references to list or dictionary 
values, people often casually say that the variable contains the list or dictionary.

Passing References
==================
References are particularly important for understanding how arguments get 
passed to functions. When a function is called, the values of the arguments are 
copied to the parameter variables. For lists (and dictionaries, which I’ll describe in 
the next chapter), this means a copy of the reference is used for the parameter. To 
see the consequences of this, open a new file editor window, enter the following 
code, and save it as passingReference.py:

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

Notice that when eggs() is called, a return value is not used to assign a new value 
to spam. Instead, it modifies the list in place, directly. When run, this program 
produces the following output: 

[1, 2, 3, 'Hello']

Even though spam and someParameter contain separate references, they both refer 
to the same list. This is why the append('Hello') method call inside the function 
affects the list even after the function call has returned.

Keep this behavior in mind: Forgetting that Python handles list and dictionary variables this way can lead to confusing bugs.

The copy Module’s copy() and deepcopy() Functions
=================================================
Although passing around references is often the handiest way to deal with lists and dictionaries,
if the function modifies the list or dictionary that is passed, you may not want these changes in the original list or dictionary value.

For this, Python provides a module named copy that provides both the copy() and deepcopy() functions.
The first of these, copy.copy(), can be used to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference.
Enter the following into the interactive shell:

>>> import copy
>>> spam = ['A', 'B', 'C', 'D']
>>> cheese = copy.copy(spam)
>>> cheese[1] = 42
>>> spam
['A', 'B', 'C', 'D']
>>> cheese
['A', 42, 'C', 'D']

Now the spam and cheese variables refer to separate lists, which is why only the list in cheese is modified when you assign 42 at index 1.
The reference ID numbers are no longer the same for both variables because the variables refer to independent lists.

cheese = copy.copy(spam) creates a second list that can be modified independently of the first.

If the list you need to copy contains lists, then use the copy.deepcopy() function instead of copy.copy().
The deepcopy() function will copy these inner lists as well.

Summary
========
Lists are useful data types since they allow you to write code that works on a modifiable number of values in a single variable.
Later in this book, you will see programs using lists to do things that would be difficult or impossible to do without them.

Lists are mutable, meaning that their contents can change.
Tuples and strings, although list-like in some respects, are immutable and cannot be changed.
A variable that contains a tuple or string value can be overwritten with a new tuple or string value,
but this is not the same thing as modifying the existing value in place—like, say, the append() or remove() methods do on lists.

Variables do not store list values directly; they store references to lists.
This is an important distinction when copying variables or passing lists as arguments in function calls.
Because the value that is being copied is the list reference, be aware that any changes you make to the list might impact another variable in your program.

You can use copy() or deepcopy() if you want to make changes to a list in one variable without modifying the original list.


Practice Questions

Q: 1. What is []?

Q: 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

Q: 3. What does spam[int(int('3' * 2) // 11)] evaluate to?

Q: 4. What does spam[-1] evaluate to?

Q: 5. What does spam[:2] evaluate to?

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

Q: 6. What does bacon.index('cat') evaluate to?

Q: 7. What does bacon.append(99) make the list value in bacon look like?

Q: 8. What does bacon.remove('cat') make the list value in bacon look like?

Q: 9. What are the operators for list concatenation and list replication?

Q: 10. What is the difference between the append() and insert() list methods?

Q: 11. What are two ways to remove values from a list?

Q: 12. Name a few ways that list values are similar to string values.

Q: 13. What is the difference between lists and tuples?

Q: 14. How do you type the tuple value that has just the integer value 42 in it?

Q: 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

Q: 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

Q: 17. What is the difference between copy.copy() and copy.deepcopy()?
"""

import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])

print(magic8ballNotes)

test = [1,2,2,3,4,5,6,2]
