extracredit = """

Extra credit: Look up the round() and abs() functions on the Internet, and find out what they do.
Experiment with them in the interactive shell.
"""

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