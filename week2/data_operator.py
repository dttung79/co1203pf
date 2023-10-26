# Basic data types: integer, float, string and boolean
a = 10 # a is an integer
b = 4.5 # b is a float
c = 'hello' # c is a string
d = True # d is a boolean

e = '10' # e is a string
f = 'False' # f is a string

# g = hello # error, hello is not defined

g = a + b # g is a float
# g = a + e # error cannot have a sum of integer and string
g = e * 3 # g is a string: hellohellohello

# Integer (number) operators
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')
# print(f'{a} / {b} = {a / b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} % {b} = {a % b}')

# String operators: +, *
s1 = 'hello'
s2 = 'world'
msg = s1 + ' ' + s2
print(msg)

line = '$' * 10 # but 10 * '$' is error!
print(line)

# Boolean operator: and, or, not
a = True
b = False

print(f'{a} and {b} = {a and b}')
print(f'{a} or {b} = {a or b}')
print(f'not {a} = {not a}')
