# --------------------------- Intro to If Statements ---------------------------
name = 'Alice'
if name == 'Alice':
    print('Hi Alice')
print('done')

print('\n')

password = 'swordfish'
if password == 'swordfish':
    print('Access Granted')
else:
    print('Wrong Password!')

print('\n')

name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo')
elif age > 2000:
    print('Unlike you, Alice is not an unded, immportal vampire.')
elif age > 100:
    print('You are no Alice, grannie.')


print("\n")


print('Enter a name.')
name = input()
if name != '':
    print('Thank you for entering a name.')
else:
    print('You did not enter a name', name)

print("\n")

another_name = (input('Enter another name: '))
if another_name != '':
    print('Thank you for entering your name.')
else:
    print('You did not enter a name')

print('\n')
# --------------------------- End Intro to If Statements ---------------------------