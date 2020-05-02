import sys

class CustomExcept(Exception):
    pass

try:
    raise CustomExcept("This is user defined exception")
except:
    print(sys.exc_info()[1])


class ValueIsSmallExcept(Exception):
    pass

num1 = int(input("Enter a number greater than 1000:"))

if(num1 <1000):
    try:
        raise ValueIsSmallExcept('please enter a value greater than 1000')
    except:
        print(sys.exc_info()[1])
    finally:
        num1 = input("Enter a number greater than 1000:")

print(num1)


# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()

print("Congratulations! You guessed it correctly.")