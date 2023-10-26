a = int(input('Enter a: '))
b = int(input('Enter b: '))

op = input('Choose an operator (+, -, x, /, ^): ')

if op == '+':
    print(f'{a} + {b} = {a + b}')
elif op == '-':
    print(f'{a} - {b} = {a - b}')
elif op == 'x':
    print(f'{a} x {b} = {a * b}')
elif op == '/':
    print(f'{a} / {b} = {a / b}')
elif op == '^':
    print(f'{a} ^ {b} = {a ** b}')
else:
    print(f'Invalid operator: {op}')