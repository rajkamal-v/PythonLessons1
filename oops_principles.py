'''
Abstraction   --  handle complexity by hiding unnecessary details from the user
Encapsulation -- Encapsulation Means:- Binding a Data and methods together in single unit.
                                Which cannot be accessible for outside world directly.
                Data Hiding:- Data can't access for outside world. make ur data private or protected

https://www.geeksforgeeks.org/polymorphism-in-python/?ref=lbp
Polymorphism - many forms (Overloading , Overriding)
            Constructor Overloading - not supported in python
            Method Overloading - methods with same name but can handle different no of parameters, or different data types
            operator Overloading - perform diff op based on the data e.g: + - *
            Method Overriding - if the child class has same method as that of the parent,
                                the child class will override the super class method
Inheritance - A class can can access all the methods and attributes of the parent class when inherited ( except private members)
'''

class Shape:

    def __init__(self, name, sides, dimension):
        self.__name = name    # private property  - can be accessed only inside the class
        self._sides = sides   # protected property - can be accessed from a child class or inside the file
        self.dimension = dimension   # public property - can be accessed from anywhere

    def area(self,l,b):
         return l*b


    def whatShape(self):
        return self.__name

class Circle(Shape):
    def __init__(self,radius):
       super().__init__('Circle',0,'2-D')
       self.__radius = radius
       self.__pi = 3.14

    def area(self):
        return self.__pi * (self.__radius ** 2)

    def howManySides(self):
        return self._sides


class Triangle(Shape):

    def __init__(self, angle):
        super().__init__('Triangle', 3, '2-D')
        self.__angle = angle




