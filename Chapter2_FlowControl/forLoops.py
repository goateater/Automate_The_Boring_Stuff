# --------------------------- Intro to For Loops---------------------------

forloopsSplained = """
The while loop keeps looping while its condition is True (which is the reason for its name), but what if you want to
execute a block of code only a certain number of times? You can do this with a for loop statement and the range() function.

In code, a for statement looks something like for i in range(5): and always includes the following:

* The for keyword

* A variable name

* The in keyword

* A call to the range() method with up to three integers passed to it

* A colon

* Starting on the next line, an indented block of code (called the for clause)


"""

print(forloopsSplained)


# --------------------------- End Intro to For Loops---------------------------

print('\n')

# --------------------------- For Loop samples -------------------------------

fornote = """
Note:
You can use break and continue statements inside for loops as well.
The continue statement will continue to the next value of the for loop’s counter, as if the program execution had reached the
 end of the loop and returned to the start. In fact, you can use continue and break statements only inside while and for loops.
If you try to use these statements elsewhere, Python will give you an error.
"""

print(fornote)

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' +str(i) + ')')

print('\n')


answer = """
The result should be 5,050. When the program first starts, the total variable is set to 0.
The for loop then executes total = total + num 100 times. By the time the loop has finished
all of its 100 iterations, every integer from 0 to 100 will have been added to total. At this point,
total is printed to the screen. Even on the slowest computers, this program takes less than a second to complete.
"""

total = 0
for num in range(101):
    total = total + num
print(total)

print(answer)
# --------------------------- End For Loop samples ---------------------------

print('\n')

# --------------------------- For Loop with range samples ---------------------------

print('Range from 12 to 16')
"""
Some functions can be called with multiple arguments separated by a comma, and range() is one of them.
This lets you change the integer passed to range() to follow any sequence of integers, including starting at a number other than zero.
"""
for i in range(12,16):
    print(i)

print('\n')



print('Range from 0 to 12 use 2 steps')
"""
The range() function can also be called with three arguments.
The first two arguments will be the start and stop values, and the third will be the step argument.
The step is the amount that the variable is increased by after each iteration.
"""

for i in range(0,12,2): #start/stop/step
    print(i)

print('\n')

print('Range using negative intgers, goes backwards')

"""
The range() function is flexible in the sequence of numbers it produces for for loops.
For example (I never apologize for my puns), you can even use a negative number for the step argument to make the for loop count down instead of up.
"""

for i in range(5, -1, -1):
    print(i)

# --------------------------- End For Loop with range samples ---------------------------

print('\n')