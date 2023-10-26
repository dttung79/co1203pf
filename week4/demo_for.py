# print Hello 10 times using for loop

for i in range(10):
    print(i, 'Hello')


s = 0
for i in range(1, 11):
    s = s + i

print(f'Sum for 1-10: {s}')

# Ex1: print numbers from 1 to 100
for i in range(1, 101):
    print(i, end=' ')

print('\n====================')   
# Ex2: print numbers from 1 to 100, but only even numbers
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=' ')

# Ex3: print numbers from 1 to 100, 10 numbers per line
for i in range(1, 101):
    print(i, end=' ')
    if i % 10 == 0:
        print()

import turtle as t
# Ex4: draw a square using for loop
# for i in range(4):
#     t.forward(100)
#     t.left(90)

# t.exitonclick()

n = int(input('Enter n: '))
# for i in range(n):
#     t.forward(100)
#     t.left(360 / n)

# t.exitonclick()

for i in range(1, 11):
    print(f'{i:2} x {n:2} = {i * n:2}')