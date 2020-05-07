'''

my name is is khan khhan  - Input

is is khan khhan my name

Khan Is Name My  - Output

India is beautiful - I
Beautiful Is India - O


1. split the words in the string -- list
2. reverse the list -- words will be reversed    sort the list
3. i need to join the words in the list with space
4. i want to capitalize each word

'''


def reverseWords(input):
    output = ""
    list_1 = input.split(' ')
    list_1.reverse()
    for word in list_1:
        output = output + word + " "
    print(output.title().rstrip())

def arrangeWords(input):
    output = ""
    list_1 = input.split(' ')
    list_1.sort()
    for word in list_1:
        output = output + word + " "
    print(output.rstrip())


reverseWords("my name is khan")

arrangeWords("my name is is khan khhan")

#All functions belong to a class called 'function' - the function created is an object to that class
#when u want to call a function u need to give functionName()
#when u want to get the reference of the function object, just give the functionName without brackets

def outer():
    print('Python')

num = 1
print(id(1))
a = outer  # function reference
print(id(outer))

a() # calling the function outer using function reference passed to the variable a

def outer(msg):
    def inner():
        print(msg)

    return inner

b = outer("hello")

num = 1
print(id(1))
a = outer  # function reference
print(id(outer))

print(b.__closure__[0].cell_contents)


#a function can be passed as a argument to another function

def lowerFunc():
    return "ordinary"

def higherFunc(func):
    print("Extra"+func())

higherFunc(lowerFunc)
print(lowerFunc())

