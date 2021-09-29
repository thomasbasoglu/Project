from decimal import Decimal
import decimal
def kdv():
    price = float(input('Fiyatı ekle: '))
    kdv = int(input('kdv oranını ekle: '))
    kdvVals = [1,8,10,18]
    
    if kdv in kdvVals:
        kdvVal = price * kdv / 100 
        mat = price - kdvVal 
        print(price)
        print(mat)      
    else:
        print('Vergiyi doğru yazdığınıza emin olun')

while True:
    kdv()