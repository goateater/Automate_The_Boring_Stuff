listStuff = """
The List Data Type
==================
A list is a value that contains multiple values in an ordered sequence.
The term list value refers to the list itself (which is a value that can be stored in a variable or passed to a function
like any other value), not the values inside the list value. A list value looks like this: ['cat', 'bat', 'rat', 'elephant'].
Just as string values are typed with quote characters to mark where the string begins and ends, a list begins with an opening
square bracket and ends with a closing square bracket, []. Values inside the list are also called items.

Items are separated with commas (that is, they are comma-delimited).
For example, enter the following into the interactive shell:


   >>> [1, 2, 3]
   [1, 2, 3]
   >>> ['cat', 'bat', 'rat', 'elephant']
   ['cat', 'bat', 'rat', 'elephant']
   >>> ['hello', 3.1415, True, None, 42]
   ['hello', 3.1415, True, None, 42]
   >>> spam = ['cat', 'bat', 'rat', 'elephant']
   >>> spam
   ['cat', 'bat', 'rat', 'elephant']

The spam variable ❶ is still assigned only one value: the list value. But the list value itself contains other values.
The value [] is an empty list that contains no values, similar to '', the empty string.


Getting Individual Values in a List with Indexes
=================================================
Say you have the list ['cat', 'bat', 'rat', 'elephant'] stored in a variable named spam.
The Python code spam[0] would evaluate to 'cat', and spam[1] would evaluate to 'bat', and so on.
The integer inside the square brackets that follows the list is called an index.
The first value in the list is at index 0, the second value is at index 1, the third value is at index 2, and so on.

For example, type the following expressions into the interactive shell. Start by assigning a list to the variable spam.


>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[0]
'cat'
>>> spam[1]
'bat'
>>> spam[2]
'rat'
>>> spam[3]
'elephant'


print 'Hello ' + spam[0]


print('Below is an example of string slicing with lists')
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0])
print('The ' + spam[1] + ' ate the ' + spam[0] + '.')

spam2 = [['cat', 'bat'], [10,20,30,40,50]]
print(spam2[0])
print(spam2[0][1])
print(spam2[1][0])


The first index dictates which list value to use, and the second indicates the value within the list value.
For example, spam[0][1] prints 'bat', the second value in the first list.
If you only use one index, the program will print the full list value at that index.

"""

print(listStuff)



