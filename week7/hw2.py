customers = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Mike', 'John']
tickets = [15, 23, 7, 12, 6, 10, 20]

def find_customer(name):
    for i in range(len(customers)):
        if customers[i] == name:
            print(f'Customer {name} has bought {tickets[i]} tickets.')
            return
    
    print(f'Customer {name} not found.')

def find_most_rich_customer():
    max_ticket = 0
    i_max = 0
    for i in range(1, len(customers)):
        if tickets[i] > max_ticket:
            i_max = i
            max_ticket = tickets[i]
    
    print(f'Customer {customers[i_max]} has bought the most tickets ({max_ticket}).')

def avg_tickets():
    sum_tickets = 0
    for t in tickets:
        sum_tickets += t
    
    return sum_tickets / len(tickets)

def find_customer_above():
    avg = avg_tickets()
    print(f'Average tickets = {avg:.2f}')

    for i in range(len(tickets)):
        if tickets[i] > avg:
            print(f'Customer {customers[i]} has bought {tickets[i]} tickets)')

# Main program
name = input('Enter customer name: ')
find_customer(name)
find_most_rich_customer()
find_customer_above()