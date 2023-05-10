######################################################

#            dotted string
# def python():
#     s="python"
#     x=len(s)
#     for i in range(0,x-4):
#         print(s[i],end=".")   
#     for i in range(4,x):
#         print(s[i],end=".")   
#     print()
# python()    

######################################################

#            dotted string
# def python():
#     s=input("enter the string: ")
#     x=len(s)
#     for i in range(0,2):
#         print(s[i],end=".")   
#     for i in range(x-2,x):
#         print(s[i],end=".")   
#     print()
# python()

#######################################################

# def python():
#     l=input("enter the string:")
#     s=l[:2]+l[-2:]
#     for i in range (len(s)):
#         print(s[i]+".",end=" ")   
#         r='.'.join(s)
# python()        

#########################################################
# def add(p):
#     a=p
#     s=[1,7,5,4,2,9,6]
#     s.append(a)
#     print(s)
# def rep(p,q):
#     a=p
#     s=[1,7,5,4,2,9,6]
#     s[a]=q
#     print(s)
# def dlt(p):
#     a=p
#     s=[1,7,5,4,2,9,6]
#     del(s[a])
#     print(s)         
# def sort():
#     s=[1,7,5,4,2,9,6]
#     s.sort()
#     print(s)    
# print("choice the option:")
# print(" 1.Addition\n 2.Replace\n 3.Delete\n 4.Sort\n 5.Exit")
# while True:
#     n=int(input("enter the choice: "))
#     if n==1:
#        p=int(input("enter the element :"))       
#        add(p)
#     if n==2:
#        p=int(input("enter the element :"))
#        q=int(input("enter the no. :"))
#        rep(p,q)
#     if n==3:
#        p=int(input("enter the element :"))
#        dlt(p)
#     if n==4: 
#        sort()
#     if n==5:
#        print("exit")   
#        break          