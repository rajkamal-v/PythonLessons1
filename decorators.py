'''
https://www.programiz.com/python-programming/decorator

Functions can be passed as arguments to another function.
function that take other functions as arguments are called higher order functions - e.g: map, filter, reduce

a function can return another function - closure

a decorator takes in a function, adds some functionality and returns it
add functionality to an existing code
also called metaprogramming as a part of the program tries to modify another part of the program at compile time
'''

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def toupper(x):
    return x.upper()

print(inc(10))
print(dec(10))
print(toupper('python'))

def operate(func,x):
     result = func(x)
     return result

a = operate(inc, 4)
b = operate(dec, 4)
c = operate(toupper,"python")

print(a)
print(b)
print(c)

def outer(msg):
    def inner():
        print(msg)

    print('óuter')
    return inner


a = outer("kamal")
a()
print(a.__closure__[0].cell_contents)


def exclam(func):
    def dec(str_1):
        print("%" * 15)
        return func(str_1)+"!"
    return dec

def title_dec(func):
    def dec(str_1):
        print("*"*15)
        return func(str_1).title()
    return dec

@title_dec
@exclam
def greetings(msg):
    return msg


print(greetings("hi"))







