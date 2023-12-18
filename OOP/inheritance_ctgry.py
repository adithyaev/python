class Category:
    def __init__(self,category):
        self.category = category
    def get_category(self):
        return self.category
    
class Product(Category):
    count = 0
    def __init__(self,name, category,price):
        Category.__init__(self,category)
        self.name = name
        self.price = price
        Product.count = Product.count + 1
    def display_product(self):
        print("name: ",self.name)
        print("category: ",Category.get_category(self))
        print("price:",self.price)
    def product_count(self):
        print("total number of products: %d" %Product.count)

prod1 = (Product('pen','stationary',50))
x=prod1.get_category()
print(x)
print(prod1.get_category())