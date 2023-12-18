class vehicle:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand
    def start_engine(self):
         print('engine start')
    def stop_engine(self):
         print('stop engine')
class car(vehicle):
    def __init__(self, model, brand,no_of_door,year):
        vehicle.__init__(self,model,brand)
        self.no_of_doors = no_of_door
        self.year = year
    def car_details(self):
        print("model:",self.model)
        print("brand: ",self.brand)
        print("number of doors: ",self.no_of_doors)
        print("year",self.year)
car1 =car("suv","benz",5,2022)
car1.start_engine()
car1.stop_engine()
car1.car_details()
        

          
    
