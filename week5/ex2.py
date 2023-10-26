n_total_coins = int(input('Enter number of coins you buy: '))
leave = 'n'
while n_total_coins > 0 and leave == 'n':
    answer = 'y'
    game = input('Choose your game: ')
    n_coins = int(input(f'Enter cois for {game}: '))
    
    while answer == 'y':
        print(f'Playing {game}, cost {n_coins}')
        n_total_coins -= n_coins
        print(f'Current coins: {n_total_coins}')
        answer = input(f'Do you want to play {game} again (y/n): ')
    
    leave = input('Do you want to leave the game center? (y/n): ')
    if n_total_coins == 0:
        print('Not enough coins to play any game!')

print('Goodbye see you again!')