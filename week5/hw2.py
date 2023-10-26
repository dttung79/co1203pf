# C1 range(1, 101, 2)
s = 0
for i in range(2, 101, 2):
    s = s + i

print(f'Sum of even numbers from 1 to 100: {s}')

# C2 range(1, 101)
s = 0
for i in range(1, 101):
    if i % 2 == 0:
        s += i
print(f'Sum of even numbers from 1 to 100: {s}')