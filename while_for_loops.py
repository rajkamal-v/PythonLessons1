#while - indetermined no of iteration, condition - until some condition is satisfied
#for - determined no of iteration , condition - until the determined no is reached
#  i += 1   this is same as this i = i+1
i = 1
while i < 6:
    print(i)
    i += 1


'''
it      |  i    | i< 6      | print i      | i += 1

a         1      True          1             2
b         2      True          2             3
c         3      True          3             4
d         4      True          4             5
e         5      True          5             6
f         6      False



'''

print('aaaa', i)


i = 1
while i < 6:
  print(i)
  if i == 3: break
  i += 1

'''
it      |  i    | i< 6      | print i       |  i == 3   (break)       | i += 1

a         1      True          1                   False               2
b         2      True           2                   False               3
c         3      True            3                  True



'''

print('bbbb',i)   #=== 3  #==== 6

i = 0
while i < 6:
    i += 1
    if i == 3: continue
    print(i)

print(i)
'''
it      |  i    | i< 6  | i += 1  |  i == 3   (continue)  | print i       

a           0     True         1        False                 1              
b           1     True         2        False                 2                  
c           2     True         3        True                
d           3     True         4        False                 4
e           4     True         5        False                 5
f           5     True         6        False                 6
g           6     False

'''

#for loop
#range(stop)
#range(start,stop,step) step default = 1, start default = 0

print(range(10))

print(range(1,10))

print(range(0,11,2))

for num in range(0,41,4): #0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(num)

for char in "python":
    print(char)

for char in ["python","Java", 23, 8.0]:
    print(char)

for num in range(1,11): #1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print('0'*(num))

for x in range(6):
  if x+1 == 3:
      break
  print((x+1)*6)
else:
    print("Finally finished!")

for i in range(1,5): # 2
    for j in range(1,11): #1...10
        print(i,'X',j,'=',i*j)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj: # big
  for y in fruits: # apple
     print(x, y)
     # red apple
     # red banana
     # red cherry
     # big apple
     # big banana
     # big cherry
     # tasty apple
     # tasty banana
     # tasty cherry







