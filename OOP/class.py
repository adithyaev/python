class Product:
    count = 0
    def __init__(self,name,category,price):
        self.name = name
        self.category = category
        self.__price = price
        Product.count = Product.count + 1
        print('init work')

    def display_product(self):
        print("name: ",self.name)
        print("category: ",self.category) 
        print("price: ",self.__price)
    
    def product_count(self):
        print("Total number of product: %d" % Product.count)
    
    def calculate_price(self):
        price = self.__price * (100/50)
        return price
    def set_price(self,price):
        self.__price = price
    def get_price(self):
        return self.__price

    

prod1 = Product('pen','stationary',20)
# print(prod1.name)
# print(prod1.category)
# print(prod1.__price)
prod2 = Product('orange','food',45)
# print(prod2.name)
# print(prod2.category)
# print(prod2.__price)

# prod1.display_product()
# prod2.display_product()
# print(prod2.__price)
print(prod1.get_price())
prod1.set_price(48)
print(prod1.get_price())


