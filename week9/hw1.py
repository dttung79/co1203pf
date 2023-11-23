products = {'pen': 10, 
            'pencil': 5, 
            'eraser': 2,
            'notebook': 15,
            'book': 20}

def add_product():
    name = input('Enter product name: ')
    price = int(input('Enter product price: '))

    if name in products:
        print(f'Product {name} is already in the store')
        return
    
    products[name] = price
    print(f'Product {name} added succesfully')

def edit_price():
    name = input('Enter product name to edit: ')
    price = int(input('Enter product new price: '))

    if name not in products:
        print(f'Product {name} is not in the store')
        return
    
    products[name] = price
    print(f'Product {name} edited succesfully')

def delete_product():
    name = input('Enter product name to delete: ')
    if name not in products:
        print(f'Product {name} is not in the store')
        return
    del products[name] # ~ products.pop(name)
    print(f'Product {name} deleted succesfully')

def show_products():
    for name, price in products.items():
        print(f'Product {name} : ${price}')


def main():
    running = True
    while running:
        print('1. Add product')
        print('2. Edit product')
        print('3. Delete product')
        print('4. Show products')
        print('5. Exit')

        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_product()
        elif choice == 2:
            edit_price()
        elif choice == 3:
            delete_product()
        elif choice == 4:
            show_products()
        elif choice == 5:
            running = False
        else:
            print('Invalid choice!')
        
        print('-----------------')
########
main()