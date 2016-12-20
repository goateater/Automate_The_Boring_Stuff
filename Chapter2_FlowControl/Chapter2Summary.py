summary = """
Summary
-------
By using expressions that evaluate to True or False (also called conditions), you can write programs that make decisions
on what code to execute and what code to skip. You can also execute code over and over again in a loop while a certain
condition evaluates to True. The break and continue statements are useful if you need to exit a loop or jump back to the start.

These flow control statements will let you write much more intelligent programs. There’s another type of flow control
that you can achieve by writing your own functions, which is the topic of the next chapter.


Practice Questions
------------------
Question 1: What are the two values of the Boolean data type? How do you write them?
Question 2: What are the three Boolean operators?
Question 3: Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
Question 4: What do the following expressions evaluate to?

(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)

Question 5: What are the six comparison operators?
Question 6: What is the difference between the equal to operator and the assignment operator?
Question 7: Explain what a condition is and where you would use one.
Question 8: Identify the three blocks in this code:

spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')

Question 9: Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
Question 10: What can you press if your program is stuck in an infinite loop?
Question 11: What is the difference between break and continue?
Question 12: What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
Question 13: Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
Question 14: If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

Extra credit: Look up the round() and abs() functions on the Internet, and find out what they do. Experiment with them in the interactive shell.
"""

print(summary)