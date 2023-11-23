products = ['pen', 'pencil', 'eraser', 'notebook', 'book']
prices = [10, 5, 2, 15, 20]

def add_product():
    name = input('Enter product name: ')
    price = int(input('Enter product price: '))

    if name in products:
        print(f'Product {name} is already in the store')
        return
    
    products.append(name)
    prices.append(price)
    print(f'Product {name} added succesfully')

def edit_product():
    name = input('Enter product name to edit: ')
    price = int(input('Enter product price: '))

    pos_found = products.index(name)

    if pos_found == -1:
        print(f'Product {name} is not in the store')
        return
    
    prices[pos_found] = price

def delete_product():
    name = input('Enter product name to delete: ')
    
    pos_found = products.index(name)

    if pos_found == -1:
        print(f'Product {name} is not in the store')
        return
    
    del products[pos_found]
    del prices[pos_found]
    print(f'Product {name} deleted succesfully')

def show_products():
    for i in range(len(products)):
        print(f'Product {products[i]} : ${prices[i]}')