# Write a program that asks for a number n, then print 2 upside down triangles
# of asteriks.
# Example: n = 3
# Output:
# 1st triangle
# * * * * * 
#   * * *
#     *
# vẽ hai tam giác chập nhau ngược lại
n = int(input('enter n:'))

for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end=' ')
    for j in range(2 * i - 1):
        print('*', end=' ')
    print()

for i in range(1, n + 1):
    for j in range(i -1):
        print(' ', end=' ')
    for j in range(2 * (n - i) + 1):
        print('*', end=' ')
    print()
# 2nd triangle
# * * *
#   * *
#     *
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()