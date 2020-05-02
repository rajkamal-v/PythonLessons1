#import oops_principles as op

from oops_principles import Shape
from oops_principles import Circle
from oops_principles import Triangle

obj = Shape('Triangle', 3 , '2 D')
print(obj.dimension)
print(obj.area(10, 20))

cir = Circle(10)
print(cir.howManySides())
print(cir.area())
print(cir.whatShape())

tri = Triangle([30,45,90])
print(tri.area(12, 4)/2)
print(tri.whatShape())




