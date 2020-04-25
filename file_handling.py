'''
open
read
write
close
create
delete
'''
# opening a file in default read mode + text mode
f = open('input.txt')
# reading the first line using readline method
print(f.readline(),end='')
# reading the second line using readline method
print(f.readline(),end='')
# reading the second line using readline method
print(f.readline(),end='')
# closing the file after reading
f.close()

#
#
# with open('input.txt', mode = 'w') as f2:
#     f2.write('python\n')
#     f2.write('java\n')
#
#
with open('input2.txt', mode = 'x') as f3:
    f3.write('python\n')
    f3.write('java\n')

def func(str_1):
    return str_1.upper()

with open('input2.txt') as inp_file:
    for data in inp_file:
        print(func(data),end='')



import os

print(os.getcwd())
#os.mkdir('../newDir')
#os.rmdir('./newDir') #rmdir will only delete an empty dir
os.remove('input2.txt') #delete a file
print(os.getenv('os'))
print(os.sys.platform)


