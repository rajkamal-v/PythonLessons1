def sum1():
    num1, num2, num3 = 3, 6, 8
    print(num1+num2+num3)

sum1()
sum1()

def sum2(num2,num3,num1):
    print(num3+num2+num1)

sum2(3, 7, 35)
sum2(467, 87 , 100)

def sum3(num2,num3,num1=50):
    print(num1+num2+num3)

sum3(3, 7)
sum3(467, 87 , 100)

def sum4(num2,num3,num1):
    return num1+num2+num3

print(sum4(3, 7, 20))
print(sum4(467, 87 , 100)-sum4(20,10,13))

def sum5(*args):
    sum = 0
    for i in args:
       sum +=i
    return sum

print(sum5(3))
print(sum5())
print(sum5(2,4))
print(sum5(4,5,6,7,8,9,10))

def full_name(lname,fname):
    return fname+lname

print(full_name('gandhi','mohandas'))
print(full_name(fname="raj",lname="kamal"))

def fullname2(**names):
    print(names['fname']+names['lname'])

fullname2(fname='Arjun',lname='arjya')

def fullname3(**names):
    name = ""
    for v in names.values():
        name += v
    print(name)

fullname3(fname='Arjitt',lname='arjya')


def print_everything(*args):
    for count, thing in enumerate(args):
        print('{0}. {1}'.format(count, thing))

print_everything('apple', 'banana', 'cabbage')

def table_things(**kwargs):
    for name, value in kwargs.items():
        print( '{0} = {1}'.format(name, value))

table_things(apple = 'fruit', cabbage = 'vegetable')

def table_things1(name, *args, **kwargs):
    dinner = ""
    for key, value in kwargs.items():
        dinner += ( '{0}'.format(key, value))

    print (args[0]+name,"who is of age" , args[1], "has these items for dinner", dinner)

table_things1('kamal','raj',36, apple = 'fruit', cabbage = 'vegetable')


def sum3(list_dummy):
    print('line no 80')
    result = sum(list_dummy)
    print('inside sum3',result)
    return result


def calc():
    print('line no 87')
    list_1 = [10,34,56,70]
    sum3(list_1)



print('line no 91')
print('ia m calling calc()',calc())