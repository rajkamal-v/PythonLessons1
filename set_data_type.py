#Set is a collection which is unordered and unindexed. No duplicate members. {}

#unordered
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(id(thisset))

#unindexed
#print(thisset[0]) - this will give error

#no duplicate members
thisset.add("apple")
print(len(thisset))
print(thisset)

#add a new value
thisset.add("orange")
print(thisset)
print(id(thisset))

#Set is changeable
def func(newset):
    newset.remove("apple")
    newset.add("watermelon")
    return newset

func(thisset)
print(thisset)
print(id(thisset))

#set() - allows u to add or remove items
list_names = ["kamal","kandan","kamal","kumar"]
set_1 = set(list_names)
print(set_1)
print(id(set_1))
set_1.add("kavitha")
print(set_1)

#frozenset() - does not allows u to add or remove items - no methods itself like add and remove
set_2 = frozenset(list_names)
print(set_2)
print(id(set_2))

#remove an entity
set_1.remove('kumar')  # given item in the set gets removed, if item not found, will give error
print('remove ------ ',set_1)

set_1.pop()  # last item in the set gets removed, cannot determine which item gets removed
print('pop    ------ ',set_1)

set_1.discard("kamal") # given item in the set gets removed, if item not found, will NOT give error
print('discard ----- ',set_1)

set_1.clear() #removes all items in the list
print(set_1)

#del set_1    # if comment removed, line 66 will throw error


#access item:
for item in set_2:
    print(item.upper())

print("kumar" in set_2)

set_1.update(["kamal","kandan","kabilan","krishna"])
print(set_1)


set_3 = {2, 4, 5, 6, 7}
set_4 = {3, 6, 9, 2, 10}
set_5 = {2, 6}

print(set_3.difference(set_4))  # A-B != B-A
print('difference ---',set_3)
print(set_4.difference(set_3))

print(set_3.intersection(set_4))
print('intersection---',set_3)

print(set_3.symmetric_difference(set_4))

print(set_3.union(set_4))

print(set_5.issubset(set_3))
print(set_4.issubset(set_3))
print(set_3.issuperset(set_5))
print(set_3.issuperset(set_4))

#print(set_3.intersection_update(set_4))
#print('intersection update---',set_3)

print('disjoint?---',set_3.isdisjoint(set_4))

print(set_3.difference_update(set_4))
print('difference update---',set_3)
print('disjoint?---',set_3.isdisjoint(set_4))









