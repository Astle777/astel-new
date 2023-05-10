###################################################################
# def bank():   
#     n=input("Account Holder Name :")
#     Ac=int(input("Account number :"))
#     AcBal=500
#     D=int(input("Enter the amount :"))
#     Totalamnt=AcBal+D
#     print(Totalamnt) 
#     W=int(input("Enter the withdrawal amountnt :")) 
#     Total=Totalamnt-W
#     print(Total)
# bank()
####################################################################
# class Bank:
#   def __init__(self, Acno, AcBal):
#     self.Acno = Acno
#     self.AcBal= AcBal
#   def Dpst(self):
#     D=int(input("Deposit amount :"))
#     self.AcBal+=D
#     print(self.AcBal)
#   def Wtdrw(self):
#     W=int(input("Withdrawal amount :"))
#     self.AcBal-=W
#     print(self.AcBal)  
# for i in range (0,3):  
#   print("choice the option:")
#   print(" Steve\n Bruce\n Stark\n Exit")
#   while True:
#       n=input("Enter the name: ")
#       if n=="Steve":
#         b=int(input("acc no:"))
#         c=500
#         i=Bank(b,c)
#         i.Dpst()
#         i.Wtdrw()
#       if n=="Bruce":
#         b=int(input("acc no:"))
#         c=1100
#         i=Bank(b,c)
#         i.Dpst()
#         i.Wtdrw()
#       if n=="Stark":
#         b=int(input("acc no:"))
#         c=300
#         i=Bank(b,c)
#         i.Dpst()
#         i.Wtdrw()
#       if n=="Exit":
#         print("exit")
#         break
#   break
################################################################   
class account:
    def __init__(self,num,name,bal):
        self.num=num
        self.name=name
        self.bal=bal   
    def withdraw(self):
        w=int(input("Withdrawal amount :"))
        self.bal=self.bal-w
    def deposit(self):
        d=int(input("Deposit amount :"))  
        self.bal=self.bal+d
    def balance(self):
        print(self.bal)    
l=[]     
print("choice the option:")
print(" 1.Create account\n 2.Deposit\n 3.Withdrawal\n 4.Showbalance\n 5.Exit")
while True:
    ch=int(input("Enter the choice :"))
    if ch==1:
        n=int(input("Enter the account number :"))
        m=input("Enter the name :")
        c=int(input("Enter the balance :"))
        X=account(n,m,c)
        l.append(X)
    elif ch==2:
        k=int(input("Enter the account number :"))
        for i in l:
            if i.num==k:
                i.deposit()  
                break    
    elif ch==3:
        q=int(input("Enter the account number :"))
        for i in l:
            if i.num==q:
                i.withdraw()
                break  
    elif ch==4:
        j=int(input("Enter the account number :"))
        for i in l:
            if i.num==j:
                i.balance()
                break
##############################################################################

                                                                                    