class Error(Exception):
    pass

class vergiError(Error):
    pass

def kdv():
    price = float(input('Fiyatı ekle: '))
    kdv = int(input('kdv oranını ekle: '))
    kdvVals = [1,8,10,18]
    try:    
        if int(kdv) in kdvVals:
            kdvVal = price * kdv / 100 
            mat = price - kdvVal
            
                  
        else:
            raise vergiError
    
    except vergiError:
        print('Vergiyi doğru yazdığınıza emin olun')

def toString():
    kdv.price
 

        


