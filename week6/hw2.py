# A woman calculates payment for groceries for a week (7 days).
# For each day, she will enter the grocery name and price.
# The program will ask if she wants to continue other groceries.
# When finish for a day, the program will print the total price for that day 
# then moving on to the next day.
# Hints: using for loop for 7 days, using while loop for each day.
tong_tien = 0

for i in range(1, 8):
    answer = 'y'
    print(f'hom nay la ngay:{i} ')
    tien_ngay = 0
    while answer == 'y':
        san_pham = input("nhap ten hang hom nay: ")
        gia_tien = float(input("hay nhap gia tien: "))
        tien_ngay += gia_tien
        
        answer = input('ban co muon tiep tuc mua k (y/n): ')
        if answer == 'n':
            print(f'Tong tien ngay thu {i}: {tien_ngay} ')
    tong_tien += tien_ngay
print(f'so tien bana mua ca tuan: {tong_tien}')