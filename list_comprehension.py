string_1 = 'python'

list_1 = []
for letter in string_1:
    if letter != 'o':
        list_1.append(letter.upper())

print(list_1)

#list comprehension
list_2 = [letter.upper() for letter in string_1]
print(list_2)

# [do some activity for each item in iterable if some condition is satisfied]

list_2 = [letter.upper() for letter in string_1 if letter != 'o']
print(list_2)

tuple_1 = (10,40,56,21,18,72,35,48)
#Output = list of numbers divisible by 3
print(tuple([x for x in tuple_1 if x%3 == 0]))
