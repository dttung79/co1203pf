# Ask user to enter product price & quantity
# Calculate total payment and print it out
# If total payment is greater than 1000, print "You get free shipping!"
# If not, print "Shipping fee: 50"

price = int(input('Enter product price: '))
quantity = int(input('Enter quantity: '))

payment = price * quantity

print(f'Payment: {payment}')
if payment > 1000:
    print('You get free shipping!')
else:
    print('Shipping fee: 50')