for i in range(1, 11):
    print(i, end=' ')
print()

for i in range(1, 11):
    if i == 5:
        break
    print(i, end=' ')
print()

for i in range(1, 11):
    print(i, end=' ')
    if i == 5:
        break
print()

for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=' ')
print()

for i in range(1, 11):
    print(i, end=' ')
    if i == 5:
        continue
print()