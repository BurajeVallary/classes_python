

class Car:
    make = "BMW" 
    def __init__(self,model,color,mileage):
          self.model=model
          self.color=color
          self.mileage=mileage


    def start(self):
         print(f"{self.model} has bought")  


    def stop(self):
         print(f"{self.model} with {self.color} has been serviced")

    def drive(self):
         print(f"The {self.model } with {self.color} is been driven at {self.mileage} km/hr")


car1 = Car("BMW","green",5000)
car2 = Car("BMW","blue",15000)


car1.start()
car1.stop()
car2.drive()








        


       