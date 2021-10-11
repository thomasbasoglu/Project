from tabulate import tabulate

class Product:
    def __init__(self, price, kdv):
        self.price = price
        self.kdv = kdv      
        self.kdvVal = price * int(kdv) / 100 
        self.mat = price - self.kdvVal 
    

        
    
        
    def toString(self):
        print('Fiyatı ' + str(self.price) + ' olan ve ' + str(self.kdv)
            + ' kdv ye tabi tutulan ürünün \n' + 'matrahı: ' + str(self.mat) + 
                'TL\nkesilen kdv tutarı ' + str(self.kdvVal) + 'TL')    

    def KKEG(self):
        mat30 = self.mat*30/100
        mat70 = self.mat*70/100
        kdv30 = self.kdvVal*30/100
        kdv70 = self.kdvVal*70/100
        
        KKEG = mat30 + kdv30
        table = [['Toplam', self.price*70/100, self.price*30/100], ['Matrah', mat70, mat30], ['KDV', kdv70, kdv30]]
    
        print(tabulate(table, tablefmt='fancy_grid'))  
        print('Matrah70: ' + str(mat70))
        print('KDV70: ' + str(kdv70))
        print('KKEG: ' + str(KKEG))
        print('Toplamı: ' + str(self.price))
        print('Mat30: ' + str(mat30))
        print('KDV30: ' + str(kdv30))
        

price = float(input('Fiyatı ekle: '))
kdv = input('kdv oranını ekle: ')
product = Product(price, kdv)    
product.toString()
type = input('\nBinek araç ise 1e, ticari araç ise 2ye, hiçbiri değil ise 3e basınız: ')

if int(type) == 1:
    product.KKEG()

if type == 2:
    print(2)

if type == 3:
    print(3)
                




