##################################################################################
#write a program that asks the user for a password and checks if it meets the following criteria:
# atleast 8 characters long,contains atleast 1 upper case letter,and contains at least one digit.
#  Print "Valid Password" if the password meets the criteria,and "Invalid Password" if it doesnot.
# def password():
#     s=input("enter the keyword:")
#     n=len(s)
#     up=False
#     dig=False
#     if n>8:
#         for i in s:
#             if i.isupper():
#                 up=True
#             if i.isdigit():
#                 dig=True
#         if up==True and dig==True:
#             print("Valid")
#         else:
#             print("Invalid")    
#     else:
#         print("Invalid")
# password()
###################################################################################
#write a program that simulates a game of rock-paper-scissors.The program should ask the user for their
# choice(Rock,Paper,Scissors)and then randomly gererated choice for the computer.The program should then
#  printout the winner of the game(either the user or the computer)Based on the following rules:
#  Rock beats scissors
#  Scissors beats paper
#  Paper beats rock
# If both the user and the computer choose the same option,the game is a tie
# import random
# s=["rock","paper","scissor"]
# u=input("enter the choice:")
# c=(random.choice(s))
# print(c)
# if u.lower()==c:
#     print("Tie")
# elif u.lower()=="rock" and c=="scissor":
#     print("user win")
# elif u.lower()=="scissor" and c=="paper": 
#     print("user win")   
# elif u.lower()=="paper" and c=="rock":
#     print("user win")
# else:
#     print("computer win")    
##########################################################################################