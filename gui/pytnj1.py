# import tkinter as tk
# from tkinter import *
# root=Tk()
# root.geometry('200x300')
# lab=Label(text="Hello").pack()
# Ent=Entry(text="Hello").pack()
# Btn=Button(text="submit").pack()
# root.mainloop()
######################################################################
# import tkinter as tk
# from tkinter import *
# root=Tk()
# root.geometry('200x100')
# lab=Label(text="Name :").grid(row=0,column=0)
# Ent=Entry(text="Hello").grid(row=0,column=1)
# lab=Label(text="Place :").grid(row=1,column=0)
# Ent=Entry(text="Hello").grid(row=1,column=1)
# Btn=Button(text="submit").grid(row=2,column=1)
# root.mainloop()
######################################################################
import tkinter 
from tkinter import *  
root=Tk()
root.title("GUI")
root.geometry('200x300')  
lab=Label(root,text="Name",fg="yellow",bg="green").pack(fill=X,padx=5,pady=10,ipadx=10,side=LEFT)
lab=Label(root,text="Hello",fg="lightgreen",bg="blue").pack(fill=X,padx=5,pady=20,ipadx=10,side=LEFT)
Btn=Button(text="submit",fg="blue",activebackground="yellow").pack(fill=X,padx=5,pady=20,ipadx=10,side=LEFT)
checkvar1 = IntVar()  
checkvar2 = IntVar()
chkbtn1 = Checkbutton(root, text = "C", variable = checkvar1, onvalue = 2, offvalue = 0, height = 2, width = 10).pack(fill=X,side=LEFT)
chkbtn2 = Checkbutton(root, text = "C++", variable = checkvar2, onvalue = 2, offvalue = 0, height = 2, width = 10).pack(fill=X,side=LEFT)
root.mainloop()
######################################################################
# import tkinter
# from tkinter import *
# from PIL import ImageTk, Image
# root=tkinter.Tk()
# img=ImageTk.PhotoImage(Image.open("artist.jpg"))
# panel=Label(root,image=img)
# panel.pack(side="bottom",fill="both", expand="yes")
# root.mainloop()
# Import required libraries
################################################
# from tkinter import *
# from PIL import ImageTk, Image

# # Create an instance of tkinter window
# win = Tk()

# # Define the geometry of the window
# win.geometry("700x500")

# frame = Frame(win, width=600, height=400)
# frame.pack()
# frame.place(anchor='center', relx=0.5, rely=0.5)

# # Create an object of tkinter ImageTk
# img = ImageTk.PhotoImage(Image.open("sunset-1373171__480.jpg"))

# # Create a Label Widget to display the text or Image
# label = Label(frame, image = img)
# label.pack()

# win.mainloop()
# ######################################################
# from tkinter import*
# import tkinter as tk
# from PIL import Image,ImageTk
# root=Tk()
# img=ImageTk,PhotoImage(Image.open('artist.jpg'))
# p=tk.Label(root,Image=img)
# p.pack()
# root.mainloop()
##########################################################
