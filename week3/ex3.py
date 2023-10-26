# Enter 3 sides of a triangle
# Check if it is a valid triangle then calculate its area
# If they are not valid, print "Invalid triangle"

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))

if a <= 0 or b <= 0 or c <= 0:
    print('Sides must be greater than 0')
elif a + b <= c or b + c <= a or c + a <= b:
    print('Sum of 2 sides must be greater than the other side')
else:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f'Area of the triangle ({a}, {b}, {c}) = {s}')