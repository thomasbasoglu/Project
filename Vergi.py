class Error(Exception):
    pass

class vergiError(Error):
    pass

class Product:
    def __init__(self, price, kdv):
        self.price = price
        self.kdv = kdv


    def kdv(price, kdv):
        try:    
            kdvVals = [1,8,10,18]    
            if kdv in kdvVals:
                kdvVal = price * kdv / 100 
                mat = price - kdvVal 
                return mat,kdvVal              
            else:
                raise vergiError
        except vergiError:
            print('Vergiyi doğru yazdığınıza emin olun')
    def toString(self):
        print('Fiyatı ' + str(self.price) + ' olan ve ' + str(self.kdv) 
    + ' kdv ye tabi tutulan ürünün \n' + 'matrahı: ' + str(kdv(self.price,self.kdv)))


price = float(input('Fiyatı ekle: '))
kdv = int(input('kdv oranını ekle: '))

Product(price, kdv).toString()




