#A dictionary is a collection which is unordered, changeable and indexed.
#In Python dictionaries are written with curly brackets, and they have keys and values.
#{1,3,4} - set
#doesnt take duplicate keys, if duplicate is given, it will take the latest
dict_1 = {"name":"kamal","age":36}
print(len(dict_1))
print(dict_1)
print(dict_1["name"])
print(dict_1["age"])

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child3"]["name"])

print(myfamily.get("child3"))
print(myfamily.get("child3").get("year"))

dict_1["age"] = 20
print(dict_1)

for k in dict_1:
    print(dict_1.get(k))

for key in dict_1:
    print(key)

for key in dict_1:
    print(key,":",dict_1.get(key))

for value in dict_1.values():
    print(value)

for key in dict_1.keys():
    print(key)

print(dict_1.items())

for key,value in dict_1.items():
    print(key,value)

dict_1.pop('age')
print(dict_1)

tuple_1 = ('name','age','sal')
values = 0
dict_2 = dict.fromkeys(tuple_1,values)
print(dict_2)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

print(id(1964))
print(id("year"))

print(id({
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}))

a =1964
print(id(a))