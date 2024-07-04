class Vechile:
    def general_usage(self):
        print("genral usage : transportatiaon")

#derived car subclass from vechile class 
class Car(Vechile):
    def __init__(self):
        print("i am car")
        self.wheel=4
        self.roof=True
    def specific_usage(self):
        self.general_usage()
        print("specific usage: family,trip,hosipatl")

#derived bike subclass from vechile class 
class Bike(Vechile):
    def __init__(self):
        print("i am bike")
        self.wheel=2
        self.roof=False
    def specific_usage(self):
        self.general_usage()
        print("specific usage:road traffic ,racing")

c=Car()
c.specific_usage()
b=Bike()
b.specific_usage()

#isinstance is in  built function which find is this obj is related with this class 

if isinstance(c,Car)==True:
    print("C is object of Car")
else:
    print("C is not obj of Car")


if isinstance(c,Bike)==True:
   print("C is object of bike")
else:
    print("C is not obj of bike")

#issubclass used for derived class
if issubclass(Car,Vechile)==False:
    print("car is not subclass of vechile")
else:
    print("car is  subclass of vechile")