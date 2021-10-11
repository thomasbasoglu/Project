from tabulate import tabulate

class Product:
    def __init__(self, price, kdv):
        self.price = price
        self.kdv = kdv      
        self.mat = price / (1 + int(kdv)/100) #1.18 çarp 
        self.kdvVal = price - self.mat 
          
    def toString(self):
        print('Fiyatı ' + str(self.price) + ' olan ve ' + str(self.kdv)
            + ' kdv ye tabi tutulan ürünün \n' + 'matrahı: ' + str(round(self.mat*100)/100) + 
                'TL\nkesilen kdv tutarı ' + str(round(self.kdvVal*100)/100) + 'TL')    

    def KKEG(self):
        mat30 = round(self.mat*30/100*100)/100
        mat70 = round(self.mat*70/100*100)/100
        kdv30 = round(self.kdvVal*30/100*100)/100
        kdv70 = round(self.kdvVal*70/100*100)/100
        
        KKEG = mat30 + kdv30
        table = [[' ', 'Toplam', '%70', '%30'],['Toplam', price, self.price*70/100, self.price*30/100], 
                      ['Matrah', round(self.mat*100)/100, mat70, mat30], 
                      ['KDV',round(self.kdvVal*100)/100, kdv70, kdv30]]
    
        print(tabulate(table, tablefmt='fancy_grid'))  
        print('Matrah70: ' + str(mat70))
        print('KDV70: ' + str(kdv70))
        print('KKEG: ' + str(KKEG))
        print('Toplamı: ' + str(self.price))
        print('Mat30: ' + str(mat30))
        print('KDV30: ' + str(kdv30))
        
while True:
        
    price = float(input('Fiyatı ekle: '))
    kdv = input('kdv oranını ekle: ')
    product = Product(price, kdv)    

    type = input('\nBinek araç ise 1e, ticari araç ise 2ye, hiçbiri değil ise 3e basınız: ')

    if int(type) == 1:
        product.KKEG()

    if type == 2:
        product.toString()

    if type == 3:
        print(3)
                    




