passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
typedPassword = (input('Enter your password: '))

if typedPassword == secretPassword:
    print('Access Granted')
elif typedPassword != secretPassword:
     print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')