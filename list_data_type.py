#List is a collection which is ordered and changeable. Allows duplicate members.

#ordered
mark_1 = [97, 85, 76, 99, 68]
print(mark_1)
print(id(mark_1))
mark_2 = [90, 99, 58, 89, 46]

user_data = ["kamal", 34, 2000.00]
'''
for mark in mark_1:
    print(mark)

for i in range(0,len(mark_1)):
    print(mark_1[i])
'''

mark_1[4] = 90
print(mark_1)
print(id(mark_1))


#changeable
list_names = ["kamal","kandan","kumar"]

def func_lst(lst):
    lst[0] = 'kavitha'
    return lst

func_lst(list_names)
print(list_names)

#indexed
print(list_names[0])

#allows duplicate?
list_names = ["kamal","kandan","kumar","kamal"]

print(set(list_names))