################################################################
#      factorial
# n=int(input("enter the number:"))
# sum=1
# for i in range(n):    
#        sum=sum*n 
#        n=n-1   
# print(sum)
################################################################
#      fabanoci
# n=0
# sum=1
# a=0
# b=1
# print(a,b)
# for i in range(5):
#     sum=a+b
#     a=b
#     b=sum
#     print(sum)
################################################################
#         palindrome
# s=input("Enter the string:")
# n=len(s)
# m=s[n::-1]
# if(s==m):
#    print(s,"is palidrome")
# else:
#     print(s,"is not palidrome")
################################################################
# s=input("Enter the string:")
# m=s[::-1]
# if(s==m):
#    print(s,"is palidrome")
# else:
#     print(s,"is not palidrome")
################################################################
# s=input("Enter the string:")
# m=''.join(reversed(s))
# if(s==m):
#    print(s,"is palidrome")
# else:
#     print(s,"is not palidrome")
################################################################
#     amstrong
# s=int(input("enter the number:"))
# sum=0
# t=s
# m=str(s)
# k=len(m)
# while t>0:
#     digit=t %10
#     sum +=digit**k
#     t //=10
# if s==sum:
#     print(s,"is an amstrong")
# else:
#     print("not a amstrong")       
################################################################