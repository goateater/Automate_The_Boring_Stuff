def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # print 'bacon local'
    spam()
    print(eggs) # print 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'

