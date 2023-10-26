answer = 'y'
while answer == 'y':
    n = int(input('Enter n: '))
    s = 0
    for i in range(n + 1):
        s += i
    print(f'Sum from 1 to {n} = {s}')

    answer = input('Do you want to calculate another sum (y/n)? ')