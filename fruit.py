

class Fruit:
    category = "Vegetables"

    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.price = taste

    def buy (self):
        print(f"You have bought a {self.name}.")

    def eat (self):
        print(f"You have eaten the {self.name}.")

    def wash (self):
        print (f"The {self.color} {self.name} is sour" )


fruit1=Fruit("Banana","yellow","sweet")        
fruit2=Fruit("Apple","green","bitter")

fruit1.buy()
fruit1.eat()
fruit2.wash()
