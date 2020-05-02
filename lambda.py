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





