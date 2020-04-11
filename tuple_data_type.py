#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

tuple_data = ('str',)

print(type(tuple_data))

tuple_data_list = tuple(['python','java','c','c++'])
print(tuple_data_list)
tuple_data_list = tuple('p')
print(tuple_data_list)
tuple_data_list = tuple('python')
print(tuple_data_list)
#ordered
tuple_ordered = ('python',23,3.00,8j,'java',23)
print(id(tuple_ordered))

for item in tuple_ordered:
    print(item)

#unchangeable/indexed
#tuple_ordered[0] = 'jython' # this is not possible in tuple, it will give TypeError

list_ordered = list(tuple_ordered)
print(list_ordered)

list_ordered[0] = 'C#'
print(list_ordered)

tuple_ordered = tuple(list_ordered)
print(tuple_ordered)
print(id(tuple_ordered))
print(id(tuple(('python',23,3.00,8j,'java',23))))
print(tuple_ordered.count(23))
print(tuple_ordered.index('java'))


