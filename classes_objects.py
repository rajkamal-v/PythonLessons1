'''
class is the template
object is the instance created from the template
class: attributes and behaviours
--- attributes / fields/ data / properties
--- behaviours/ methods
string = 'hello'.upper()

custom class: Person - name, gender, ID, height, weight, age, species = 'homosapiens'
                       speak_mothertoungue, dance, eat, sleep, grow, speak
object or instance: p1 = Person()
 p1.name = 'raj' p1.gender ='m'
p1.ID = 345678902345 p1.height = 173cm
p2 = person()
p2.name ='arjun'

parent class called Object
'''

name = str()
print(type(name))


#syntax
class Snake:
    pass

python = Snake()
print(python)

class Snake:
    #class property
    name = 'Python'

print('class attribute - ',Snake.name)
python1 = Snake()
python2 = Snake()

print(python1.name)
print(python2.name)


#object = Class(attributes)

#constructor - a constructor is used to create an object from the class

list_1 = list()
print(list_1)


class Snake:
    #instance properties
    def __init__(self,name):
       self.name = name



python  = Snake('Python')
print(python.name)
python.name = 'cobra'
print(python.name)
cobra = Snake('Cobra')
print(cobra.name)

class Snake:
    #class attriutes/property
    species = "reptiles"
    def __init__(self,name,isPoisonous):
       # instance attriutes/properties
       self.name = name
       self.isPoisonous = isPoisonous
    # Instance method
    def bite(self):
        if self.isPoisonous:
            print(self.name,'bite is poisonous')
        else:
            print(self.name, 'bite is not poisonous')
    # Class Method
    @classmethod
    def layEggs(cls):
        print(cls.species,'can lay eggs')

    @staticmethod
    def isOld(age):
        if age > 10:
            print('Snake is old')
        else:
            print('Snake is young')

#Instance/Object properties(name) require an object/instance to be created
#by calling the constuctor and passing arguments, it can be directly called using ObjectName (python)
python  = Snake('Python',False)
print(python.name)
python.bite()
cobra = Snake('Cobra',True)
print(cobra.name)
cobra.bite()
print(cobra.species)
#del cobra.length
#print(python.length)
#print(cobra.length)

#del Snake.species
#print(cobra.species)
#print(python.species)


#class properties(species) doesnt require an object/instance to be created, it can be directly called using ClassName (Snake)
print('class call- ',Snake.species)
Snake.layEggs()


print('kamal'.upper())

print(str.maketrans({'k':24}))

Snake.isOld(20)


class Person:
    #class attriutes/property
    species = "homosapiens"
    def __init__(self, name, birtYear, gender = 'F'):
       # instance attriutes/properties
       self.name = name
       self.gender = gender
       self.birthYear = birtYear

   # Instance method
    def calculateAge(self):
        return 2020 - self.birthYear

    # Class Method
    @classmethod
    def whatSpecies(cls):
        print('all humans are ',cls.species)

    @staticmethod
    def isAdult(age):
        if age > 18:
            print('Pesron with age',age,'is an Adult')
        else:
            print('Pesron with age',age,'is not an Adult')


p1 = Person('Arjun', 2013, 'M')
age = p1.calculateAge()
print(age)
p1.whatSpecies()
p1.isAdult(age)

