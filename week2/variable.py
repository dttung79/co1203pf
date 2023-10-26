a = 10 # a variable named a, its value is 10
print(a)

a = 20
print(a)

b = a + 50 # b is another variable, its value is a + 50
print(b)

name = input('Enter your name: ')
print('Hello', name)

# a is a number (integer), same as b
print(type(a), type(b))
# name is a string (a collection of characters)
print(type(name))

a = int(input('Enter number a: ')) # convert string to integer
b = int(input('Enter number b: '))
c = a + b
print(c)