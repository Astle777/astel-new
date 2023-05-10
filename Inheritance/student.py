############################################################
class student:
    def stud(self):
        n=input("Enter name:")
        m=int(input("Enter age:"))
        p=input("Enter the cource:")
        print(n,m,p)
class cource(student):
    def Dept(self):
        super().stud()
        print("Cource details")
        print("Syllabus")
st=cource()       
st.Dept()
##############################################################
# l=[]
# class company:
#     def cmp(self):
#         n=input("enter the company name :")
#         return n
# class dep(company):
#     def dept(self):
#         l.append(super().cmp())
#         k=input("enter department :")   
#         return k
# class person(company):
#     def per(self):
#         l.append(super().cmp())
#         self.p=input("enter the name :")
#         l.append(self.p)
#         self.s=int(input("enter the salary :"))
#         l.append(self.s)
#         print(l)
# ob=person()
# ob.per()     
