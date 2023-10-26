# using while loop with counter (but for loop will be better)
counter = 0
while counter < 10:
    print('Hello')
    counter += 1
print()

# using while to validate input
a = int(input('Enter a positive number: '))
while a <= 0:
    a = int(input('Invalid. Enter a positive number again: '))

print(2 * a)

# using while to ask user to continue or not
payment = 0
answer = 'y'
while answer == 'y':
    price = int(input('Enter price: '))
    payment += price
    answer = input('Continue (y/n)? ')

print(f'Payment = {payment}')