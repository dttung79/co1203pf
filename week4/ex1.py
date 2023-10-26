import random as rd
answer = 'y'

while answer == 'y':
    comp_number = rd.randint(1, 5)
    user_number = int(input('Enter your number: '))

    if user_number == comp_number:
        print('Correct')
    else:
        print(f'Incorrect, my number is {comp_number}')
    
    answer = input('Continue (y/n)? ')