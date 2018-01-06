practice_questions = """
Practice Questions
==================
Q: 1. What are the two values of the Boolean data type? How do you write them? True and False

Q: 2. What are the three Boolean operators? AND, OR and NOT

Q: 3. Write out the truth tables of each Boolean operator 
(that is, every possible combination of Boolean values for the operator and what they evaluate to).

FlowControl.py contains the truth tables to the AND, OR and NOT operators

Q: 4. What do the following expressions evaluate to?

(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)

Q: 5. What are the six comparison operators?

Q: 6. What is the difference between the equal to operator and the assignment operator?

Q: 7. Explain what a condition is and where you would use one.
 
Q: 8. Identify the three blocks in this code:

spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')

Q: 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

Q: 10. What can you press if your program is stuck in an infinite loop?

Q: 11. What is the difference between break and continue?

Q: 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

Q: 13. Write a short program that prints the numbers 1 to 10 using a for loop. 
      Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

Q: 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?


"""


extracredit = """

Extra credit: Look up the round() and abs() functions on the Internet, and find out what they do.
Experiment with them in the interactive shell.
"""
print(practice_questions)
print(extracredit)

print("ABS Function Explained")
print("======================")
print("abs() -- Return the absolute value of a number."
      " The argument may be an integer or a floating point number. "
      "If the argument is a complex number, its magnitude is returned.")
print()
testnumber = -128374627
print("test number passed to abs() is -128374627, and the result = ",abs(testnumber))

print()


roundfunction = """

ROUND function Explained
========================
round(number[, ndigits])

Return the floating point value number rounded to ndigits digits after the decimal point.
If ndigits is omitted or is None, it returns the nearest integer to its input. Delegates to number.__round__(ndigits).

For the built-in types supporting round(), values are rounded to the closest multiple of 10 to the power minus ndigits;
if two multiples are equally close, rounding is done toward the even choice (so, for example,
both round(0.5) and round(-0.5) are 0, and round(1.5) is 2). The return value is an integer if called with one argument,
otherwise of the same type as number.

Note:
The behavior of round() for floats can be surprising: for example, round(2.675, 2) gives 2.67 instead of the expected 2.68.
This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float.
See Floating Point Arithmetic: Issues and Limitations(https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues) for more information.


"""
print(roundfunction)
num = 128.250324
print(num, "rounded to 4 = ",round(num,4))
print(num, "rounded to 2 = ", round(num,2))