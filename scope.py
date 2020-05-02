'''
 a varible is global when it is outside of all the blocks, u can access anywhere

 u shouldn't assign a value to a global variable inside a block, it will become local

 u cannot use a global as well as a local variable of same name in a block

 a varible is local to a block, if it is declared inside the block, u cannot access it outside of the block

 don't use the same variable name unnecessarily

 when u want to assign value to a global variable inside a block , declare it as 'global'
                                        , else it will be treated as a new local variable

 when u want to assign value to a local variable inside a child block of local, declare it as 'nonlocal'


'''


x = 20  # this is global

#-------------
def printNum():
    print(x)

printNum()
print(x)
print('-----------------------')

#--------------
def printNum():
    #print(x)        - cannot use global and local in same block
    x = 10            #local
    print(x)            #local
    
printNum()
print(x)
print('-----------------------')

#------------------

def printNum():
    global x      #this will be treated as global
    x = 40        #global x
    print(x)

printNum()
print(x)
print('-----------------------')

#----------------------------
def printNum():
    x=10
    def anotherFunc():
        x = 50
        print(x)

    anotherFunc()
    print(x)

printNum()
print(x)
print('-----------------------')

#----------------------------
def printNum():
    x=10
    def anotherFunc():
        nonlocal x    #this x is not global also not local to anotherfunc(), this represent local variable of printNum()
        x = 50
        print(x)

    anotherFunc()
    print(x)

printNum()
print(x)
print('-----------------------')

