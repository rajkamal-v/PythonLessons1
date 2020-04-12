#List is a collection which is ordered and changeable. Allows duplicate members. []

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

print(id(list_names))

print(list_names[0])
print(list_names[0:1])
print(list_names[-2])
print(list_names[::-1])

print(list_names.count("kamal"))
list_names.append("kabilan")
print(list_names)
list_names.append(['kannan', 'karthik'])
print(list_names)
list_names.append(23)
print(list_names)
list_names.append({"name":"kadhir"})
list_names.append("uma")
print(list_names)
list_names.insert(1,"keshav")
print(list_names)
list_names.remove(['kannan', 'karthik'])
print(list_names)
list_names.pop()
print(list_names)
list_names.pop()
print(list_names)
list_names.pop()
list_names.sort()
print(list_names)
list_names.reverse()
print(list_names)
print(id(list_names))

list_copy = list_names.copy()
list_copy_2 = list(list_names)
print(list_copy)
print(id(list_copy))
print(id(list_copy_2))
list_names_2 = list_names
print(id(list_names_2))
print(list_copy == list_names)
print(list_copy is list_names)
print(list_copy is list_copy_2)
print(list_names is list_names_2)

list_names.extend(['kavitha','krishna'])
print(list_names)
list_names.append(['kannan', 'karthik'])
print(list_names)

# list_names.clear()
# print(list_names)
# del(list_names)
#print(list_names)

# list_names = []
# list_names.append('kamal')
# print(list_names)

print(type(list_names))

#if else
for name in list_names:
    if 'list' in str(type(name)):
        for i in name:
            print(i)
    else:
        print(name)

#continue
for name in list_names:
    if 'list' in str(type(name)):
        for i in name:
            print(i)
        continue
    print(name)

