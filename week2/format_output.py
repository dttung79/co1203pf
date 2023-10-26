# Align output: left, right or center
s = 'hello'
a = 4
f = 5.5

print(f'|{s:20}|') # string is left-aligned by default
print(f'|{a:20}|') # integer is right-algined by default
print(f'|{f:20}|') # float is right-aligned by default

# Specific output alignment
print(f'|{s:>20}|') # Print s align on the right
print(f'|{a:<20}|') # print a align on the left
print(f'|{f:^20}|') # print f align on the center