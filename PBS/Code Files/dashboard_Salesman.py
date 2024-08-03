import PIL
import sqlite3
import time

import matplotlib.pyplot as plt 
import pandas as pd

from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

from sales import salesClass
from bill import BillClass
from backup import BackUP

from currentsession import User

class PBS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x600+40+60")
        self.root.attributes("-fullscreen",False)
        self.root.title("Parth Inventory Software")
        self.root.config(bg = "lightblue")
        
        #CONTENT
        #TITLE
        self.icon_title=PhotoImage(file="images/logo1.png")
        title = Label(self.root,text = "Parth Inventory Software",image=self.icon_title,compound=LEFT, font=("times new roman", 40, "bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #LOGOUT BUTTON
        btn_logout = Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",command=self.backup,cursor="hand2").place(x=1200,y=10,height = 50,width = 150)

        #CLOCK
        self.label_clock = Label(self.root,text = "Welcome\t\t Date : "+str(time.strftime("%d"))+"-"+str(time.strftime("%m"))+"-"+str(time.strftime("%y")), font=("times new roman", 15),bg="#5d636d",fg="white")
        self.label_clock.place(x=0,y=70,relwidth=1,height=30)

        #LEFT MENU
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=460)

        self.MenuLogo = Image.open("images/menu_im.png")
        #self.MenuLogo = self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo = self.MenuLogo.resize((200,200),PIL.Image.Resampling.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        label_menu_logo = Label(LeftMenu,image=self.MenuLogo)
        label_menu_logo.pack(side=TOP,fill=X)

        #Menu Label for Menu Buttons
        self.icon_side=PhotoImage(file="images/side.png")

        label_Menu = Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)

        #Buttons
        btn_sales = Button(LeftMenu,text="Sales",command=self.SALES,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_bill = Button(LeftMenu,text="Billing",command=self.Billing,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_view_stock = Button(LeftMenu,text="View Stock",image=self.icon_side,command=self.view_stock,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit = Button(LeftMenu,text="Exit",image=self.icon_side,command=self.confirm_EXIT,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        RightFrame = Frame(self.root,bd=2,relief=RIDGE,bg="black")
        RightFrame.place(x=205,y=102,width=1190,height=460)

        self.RightMenuLogo = Image.open("images/bg.png")
        #self.RightMenuLogo = self.RightMenuLogo.resize((200,200),Image.ANTIALIAS)
        self.RightMenuLogo = self.RightMenuLogo.resize((300,300),PIL.Image.Resampling.LANCZOS)
        self.RightMenuLogo = ImageTk.PhotoImage(self.RightMenuLogo)

        label_rmenu_logo = Label(RightFrame,image=self.RightMenuLogo)
        label_rmenu_logo.place(x=5,y=5,height=445,width=1175)

        
        #FOOTER
        label_footer = Label(self.root,text = "Parth Inventory System", font=("times new roman", 12),bg="#5d636d",fg="white").pack(side=BOTTOM,fill=X)
        
    def Billing(self):
        self.new_ProductWindow = Toplevel(self.root)
        self.new_ProductObj = BillClass(self.new_ProductWindow)
    
    def SALES(self):
        self.new_ProductWindow = Toplevel(self.root)
        self.new_ProductObj = salesClass(self.new_ProductWindow)

    def view_stock(self):
        try:
            conn = sqlite3.connect("pbs.db")
            cursor = conn.cursor()
            cursor.execute("Select name,quantity from product where quantity > 0")
            product = cursor.fetchall()
            df = pd.DataFrame(product)
            df.columns=['Name', 'Quantity']
            plt.plot(df['Name'],df['Quantity'],'r^-',linewidth=2,markersize=12)
            plt.title("Current active stock report")
            plt.xlabel("Name")
            plt.ylabel("Quantity")
            plt.grid()
            plt.show()

        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)

    def backup(self):
        self.new_obj = BackUP.bckup()

    def confirm_EXIT(self):
        root1=Tk()
        self.root1=root1
        self.root1.title("EXIT")
        root1.geometry("500x200")
        self.label_exit = Label(self.root1,text="Do you want to exit without backup?",bd=5,relief= RIDGE,bg="white",fg="black",font=("times new roman",16,"bold")).pack(fill=X)
        btn_exit_yes = Button(self.root1,text = "YES",command=quit,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").place(x=50,y=100,width=100,height=50)
        btn_exit_no = Button(self.root1,text = "NO",command=root1.destroy,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").place(x=150,y=100,width=100,height=50)
        


if __name__ == "__main__":
    root=Tk()
    obj = PBS(root)
    root.mainloop()