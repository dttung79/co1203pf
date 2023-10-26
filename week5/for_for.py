n = int(input('Enter n: '))

# Draw a square * using nested for loop
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

m = int(input('Enter m: '))
for i in range(n):
    for j in range(m):
        print('*', end=' ')
    print()


for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()


for i in range(n):
    for j in range(n):
        print('*', end=' ')
        if j == i:
            break
    print()