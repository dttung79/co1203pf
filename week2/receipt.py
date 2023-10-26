name = input('Enter product name: ')
price = int(input('Enter price: '))
number = int(input('Enter product number: '))
payment = price * number

header = '-' * 9 + 'Receipt' + '-' * 9
print(header)
print('Product name:', f'{name:>11}')
print('Price:', f'{price:>18}')
print('Number:', f'{number:>17}')
print('Payment:', f'{payment:>16}')