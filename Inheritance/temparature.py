class temparature:
    def __init__(self,l,b):
        self.far=l
        self.cel=b
        Cels=(self.far-32)/1.8
        Farh=(self.cel*1.8)+32
        print("Celcius",Cels)
        print("Fahrenheit",Farh)
h=int(input("enter the Fahrenheit= "))
w=int(input("enter the Celcius= "))        
temparature(h,w)