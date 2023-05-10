##################################################################################
# import math
# class circle:
#     def __init__(self,r):
#         self.rad=r
#         area=math.pi*(self.rad)**2
#         circumference=2*(math.pi*self.rad)
#         print("Area =",area)
#         print("Circumference =",circumference)
# radii=int(input("enter the radius :"))        
# circle(radii)
###################################################################################
class rectangle:
    def __init__(self,l,b):
        self.len=l
        self.wid=b
        area=self.len*self.wid
        perimeter=2*(self.len+self.wid)
        print("area",area)
        print("perimeter",perimeter)
h=int(input("enter the length="))
w=int(input("enter the width="))        
x=rectangle(h,w)
####################################################################################
