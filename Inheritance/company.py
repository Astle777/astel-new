l=[]
class company:
    def cmp(self):
        n=input("enter the company name :")
        return n
class dep(company):
    def dept(self):
        l.append(super().cmp())
        k=input("enter department :")   
        return k
class person(dep):
    def per(self):
        l.append(super().dept())
        self.p=input("enter the name :")
        l.append(self.p)
        self.s=int(input("enter the salary :"))
        l.append(self.s)
        print(l)
ob=person()
ob.per()             