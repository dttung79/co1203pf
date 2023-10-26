import random as rd

answer = 'y'
while answer == 'y':
    n_corrects = 0
    n_wrongs = 0

    for i in range(5):
        comp_number = rd.randint(1, 5)
        user_number = int(input('Enter your number: '))

        if comp_number == user_number:
            print('Correct!')
            n_corrects += 1
        else:
            print(f'Incorrect! The correct number is {comp_number}')
            n_wrongs += 1

    print(f'You have {n_corrects} corrects and {n_wrongs} wrongs')

    answer = input('Do you want to play again? (y/n) ')