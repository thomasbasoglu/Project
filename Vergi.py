class Error(Exception):
    pass

class vergiError(Error):
    pass

def kdv(price, kdv):
    
    kdvVals = [1,8,10,18]
    try:    
        if int(kdv) in kdvVals:
            kdvVal = price * kdv / 100 
            mat = price - kdvVal
            return mat      
        else:
            raise vergiError
    
    except vergiError:
        return 'Vergiyi doğru yazdığınıza emin olun'

        

while True:
    price = float(input('Fiyatı ekle: '))
    kdv = input('kdv oranını ekle: ')
    kdv(price, kdv)
