import sys

#
# num1 = input('Enter num 1:')
# num2 = input('Enter num 2:')

# try:
#     print(int(num1)/int(num2))
#     print("I am inside try block")
# except ValueError:
#     print('You have not entered an integer value')
# except (ZeroDivisionError,NameError):
#     print('Either Divisor cannot be zero or NameError')
# except:
#     print(sys.exc_info())
#
# print('program ends')

# try:
#     print(int(num1) / int(num2))
#     print("I am inside try block")
# finally:
#     print('I must get executed irrespective of exception or not')
#
# print('program ends')

# try:
#     print(int(num1) / int(num2))
#     print("I am inside try block")
# except:
#      print(sys.exc_info())
# finally:
#     print('I must get executed irrespective of exception or not')
#
# print('program ends')
a = 'j'
b = 6

try:
    if a > b:
        try:
            print(int(a))
        except ValueError:
            print('a should be an integer')
except:
    print(sys.exc_info())
finally:
    print('Outer block')

num2 = input('enter an integer: ')

if int(num2):
    print(num2)
else:
    raise ZeroDivisionError("number cannot be 0, give some other integer")