'''
Anonymous functions

'''

def area(l,b):
    return l*b

print(area(2,3))

#syntax , f(x):x*4
#lambda arguments: expression
a = lambda l,b: l*b
print(a(4,2))

lambda_1 = lambda a: a + a
print(lambda_1(2))
print(lambda_1("mam"))
print(lambda_1([1, 2, 3, 4]))

lambda_2 = lambda a,b=10: a+b
print(lambda_2(2))
print(lambda_2(2,20))

print((lambda x, y, z: x + y + z)(1, 2, 3))
print((lambda x, y, z=3: x + y + z)(1, 2))
print((lambda x, y, z=3: x + y + z)(1, y=2))
print((lambda *args: sum(args))(1,2,3))
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))
print((lambda x, *arg, y=0, z=0: x + y + z)(1, y=2, z=3))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)  # ====>   lambda a: a * 2
mytripler = myfunc(3)  # ====>   lambda a: a * 3

print(mydoubler(10))   # =====> lambda 10: 10 * 2   = 20
print(mytripler(10))   # =====> lambda 10: 10 * 3   = 30

#The built-in function map() takes a function as a first argument and applies it to each of the elements of its second argument, an iterable.
result = list(map(lambda x: x[::-1], ['cat', 'dog', 'cow']))

print(result)
#list comprehension:
[x.capitalize() for x in ['cat', 'dog', 'cow']]


'''
The built-in function filter(), another classic functional construct, 
can be converted into a list comprehension. It takes a predicate as a 
first argument and an iterable as a second argument. 
It builds an iterator containing all the elements of the initial 
collection that satisfies the predicate function.
'''
print(list(filter(lambda x: 'o' not in x, ['cat', 'dog', 'cow'])))

even = lambda x: x%2 == 0
print(list(filter(even, range(11))))

#list comprehension:
[x for x in range(11) if x%2 == 0]

from functools import reduce
print(reduce(lambda a, x: f'{a} | {x}', ['cat', 'dog', 'cow', 'fox']))
print(reduce(lambda a , b: str(a)+str(b), [1,10,20]))



