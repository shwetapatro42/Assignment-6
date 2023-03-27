class Dog:
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color

    def description(self):
        print(f"\nDog Name : {self.name} \nDog Age : {self.age} years")

    def get_info(self):
        print("Dog Coat color : ",self.coat_color)

class JackRussellTerrier(Dog):
    def pet(self):
        print("He is a Pet dog")

    def non_veg(self):
        print("Non-veg food is favourite")

class Bulldog(Dog):
    def run(self):
        print("Runs very fast")

    def bark(self):
        print("Barks loudly")

#name=input("Enter name of dog : ")
#age=int(input("Enter age of dog : "))
#color=input("enter coat color of dog : ")

jack_obj=JackRussellTerrier('Bruno','8','Black')
jack_obj.description()
jack_obj.get_info()
jack_obj.pet()
jack_obj.non_veg()

bulldog_obj=Bulldog('Rocky','5','Brown')
bulldog_obj.description()
bulldog_obj.get_info()
bulldog_obj.run()
bulldog_obj.bark()