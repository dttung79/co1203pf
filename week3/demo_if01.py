a = int(input('Enter a: '))
b = int(input('Enter b: '))

op = input('Choose an operator (+, -): ')

if op == '+':
    print(f'{a} + {b} = {a + b}')
if op == '-':
    print(f'{a} - {b} = {a - b}')