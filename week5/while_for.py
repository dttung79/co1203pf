n_customers = 5

for i in range(n_customers):
    total_payment = 0
    customer = input('Enter customer name: ')
    has_product = True

    while has_product:
        product_name = input("Enter product name: ")
        product_price = int(input('Enter product price: '))
        total_payment += product_price

        answer = input('Is there any product left (y/n)?')
        has_product = answer == 'y' or answer == 'yes'
    
    print(f'Total payment for customer {customer}: {total_payment}')