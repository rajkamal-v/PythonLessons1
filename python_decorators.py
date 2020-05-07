'''
add functionality to an existing code
also called metaprogramming as a part of the program tries to modify another part of the program at compile time

Functions can be passed as arguments to another function.

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result

operate(inc , 3) or operate(dec , 3)

function that take other functions as arguments are called higher order functions - map, filter, reduce

map(lambda x: x[::-1], ['cat', 'dog', 'cow'])

a function can return another function - closure

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()
new()

a decorator takes in a function, adds some functionality and returns it

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

ordinary()
pretty = make_pretty(ordinary)
pretty()


@make_pretty
def ordinary():
    print("I am ordinary")

Decorating Functions with Parameters
def divide(a, b):
    return a/b

def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b
'''