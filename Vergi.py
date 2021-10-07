class Error(Exception):
    pass

class vergiError(Error):
    pass

class Product:
    def __init__(self, price, kdv):
        self.price = price
        self.kdv = kdv 
        
        try:    
            kdvVals = [1,8,10,18]    
            if kdv in kdvVals:
                kdvVal = price * kdv / 100 
                mat = price - kdvVal 
                self.mat = mat
                self.kdvVal = kdvVal

            else:
                mat = None
                self.mat = mat
        
        except vergiError:
            print('Vergiyi doğru yazdığınıza emin olun')
        
    def toString(self):
        print('Fiyatı ' + str(self.price) + ' olan ve ' + str(self.kdv)
            + ' kdv ye tabi tutulan ürünün \n' + 'matrahı: ' + str(self.mat) + 
                'TL\nkesilen kdv tutarı ' + str(self.kdvVal) + 'TL')    

def KKEG():
    print(Product.mat)


price = float(input('Fiyatı ekle: '))
kdv = input('kdv oranını ekle: ')

Product(price, kdv).toString()

type = input('\nBinek araç ise 1e, ticari araç ise 2ye, hiçbiri değil ise 3e basınız: ')

if type == 1:
    KKEG()

if type == 2:
    print(2)

if type == 3:
    print(3)
    




