myPets = ['Zophie', 'Pooka', 'Fat-tail']
#print('Enter a pet name:')
name = input('Enter a pet name: ')
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')