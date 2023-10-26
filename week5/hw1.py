answer = 'y'

while answer == 'y' or answer == 'yes':
    usd_amount = int(input('Enter USD amount to convert: '))
    vnd_amount = usd_amount * 25000
    print(f'${usd_amount} = {vnd_amount} VND')

    answer = input('Do you want to continue (y/n)?')