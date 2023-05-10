# class time:
#     print("Enter the time1 :")
#     h1=int(input("Hours :"))
#     m1=int(input("Minutes :"))
#     s1=int(input("Seconds :"))
#     print("Enter the time2 :")
#     h2=int(input("Hours :"))
#     m2=int(input("Minutes :"))
#     s2=int(input("Seconds :"))
#     h3=h1+h2+(m1+m2+(s1+s2)//60)//60
#     m3=(m1+m2+(s1+s2)//60)%60
#     s3=s1+s2%60
#     print ("t1:",h1,"Hours",m1,"Minutes",s1,"seconds")
#     print ("t2:",h2,"Hours",m2,"Minutes",s2,"seconds")
#     print ("time:",h3,"Hours",m3,"Minutes",s3,"seconds")
# time () 
################################################################   
class time:
    def _init_(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes

    def display(self):
        print("Time: {} hours {} minutes".format(self.hours,self.minutes))    

class AddTime(time):
    def __init__(self,hours,minutes):
        super()._init_(hours,minutes)

    def add (self,other):
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes

        if total_minutes >= 60:     
            total_hours += total_minutes // 60
            total_minutes = total_minutes % 60

        return AddTime(total_hours,total_minutes)    

    
n=int(input("enter hr:"))
m=int(input("enter min:"))
time1 = AddTime(n,m)       
p=int(input("enter hr:"))
q=int(input("enter min:"))
time2 =AddTime(p,q)

time3=time1.add(time2) 

time1.display()
time2.display()
time3.display()







        


        


            
