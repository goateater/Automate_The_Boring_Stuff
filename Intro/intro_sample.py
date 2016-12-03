passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
typedPassword = (raw_input('Enter your password: '))

if typedPassword == secretPassword:
    print('Access Granted')
    if typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')