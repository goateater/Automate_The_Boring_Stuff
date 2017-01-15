print ("Local and Global Variables")
print("===========================")

reasons = """
1) Code in the global scope cannot use any local variables.
2) Code in a local scope can access global variables.
3) Code in one functions local scope cannot use variables in another local scope.
4) Code in one function's local scope cannot use variables in any other local scope.

If there is an assignment statement within a function, it is considered a local variable.
Assignment Statement = Local Variable
No Assignment Statement = Global Variable

"""

print(reasons)

print('\n')

spam = 42 # global variable

def eggs():
    spam = 42 # local variable
    print(spam, "from eggs function")

print("some code here")
print("some more code")
print(spam)
eggs()

print('Example of local versus global variables')
print('\n')

def spam():
    global eggs
    eggs = 'Hello this is now a global variable' #Since the statememt 'global eggs' is defined in the function, it will only use the global variable
    print(eggs)

eggs = 43
spam()
print(eggs)
