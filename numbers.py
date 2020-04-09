num1 = 10
num2 = 20
num3 = 30; num4 = 40

num5 = num6 = 50
# 50 <----- num6, num5

num7, num8, name = 60, 70.90, 'Python'

print(num7)
print(num8)
print(name)

name1 = "\"I am also a \"String\"" # '\' is an escape character
name2 = "I'm a string"

with_backslash = "i\'m a\tthing"  #\n - it is a newline character; \t is for tab

print(name1)
print(name2)
print(with_backslash)

str = '''i am a multiline string
And i will be coming in several lines
thank you
'''
print(str)
m_str2 = """
i am a multiline string
And i will be coming in several lines
thank you
"""
#mutable vs immutable

new_name = 'pyth0n'
print(id(new_name))

new_name = 'python'

print(id(new_name))

'''
'pyth0n' <------ 
'python' <------- new_name
'''

print(id('pyth0n'))





