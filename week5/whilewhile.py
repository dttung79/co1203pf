has_customer = True

while has_customer:
    has_product = True
    total_payment = 0
    customer = input('Enter customer name: ')

    while has_product:
        product_name = input("Enter product name: ")
        product_price = int(input('Enter product price: '))
        total_payment += product_price

        answer = input('Is there any product left (y/n)?')
        has_product = answer == 'y' or answer == 'yes'

    print(f'Total payment for customer {customer}: {total_payment}')
    answer = input('Is there any customer left (y/n)?')
    has_customer = answer == 'y' or answer == 'yes'
