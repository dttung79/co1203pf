n = int(input('Enter n: '))
for i in range(n):
    for j in range(n - i):
        print('*', end=' ')
    print()

for i in range(n):
    for j in range(n - i):
        print(' ', end=' ')
    for j in range(2 * i + 1):
        print('*', end=' ')
    print()