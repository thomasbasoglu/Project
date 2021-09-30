class Error(Exception):
    pass

class vergiError(Error):
    pass

def kdv():
    price = float(input('Fiyatı ekle: '))
    kdv = int(input('kdv oranını ekle: '))
    kdvVals = [1,8,10,18]
    try:    
        if kdv in kdvVals:
            kdvVal = price * kdv / 100 
            mat = price - kdvVal 
            print(price)
            print(mat)      
        else:
            raise vergiError
    
    except vergiError:
        print('Vergiyi doğru yazdığınıza emin olun')

        

while True:
    kdv()