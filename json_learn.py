import json

file = open("data.json","r")

str_1 = file.read()


data = json.loads(str_1)
for i in data['data']:
    print(i['name'])
    print(i['age'])
    print(i['city'])

with open("data.json","r") as fp:
    data = json.load(fp)
    for i in data['data']:
        print(i['name'], i['age'], i['city'])


#dumps wil convert a python data into a json equivalent value - result will be a json string
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas"))) #list
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))   #true
print(json.dumps(False))  #false
print(json.dumps(None))   #null







