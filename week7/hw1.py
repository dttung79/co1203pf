def convert_temperature(temp, unit):
    if unit.upper() == 'F':
        return (temp - 32) * (5 / 9)
    elif unit.upper() == 'C':
        return temp * (9 / 5) + 32
    else:
        print("Error: Invalid unit. Please use 'F' for Fahrenheit or 'C' for Celsius.")
        return None
    

temp = int(input('Enter a temperature: '))
unit = input('Enter a unit (F/C): ')

temp_convert = convert_temperature(temp, unit)
if temp_convert != None:
    print(f'{temp} {unit} convert = {temp_convert:.2f}')