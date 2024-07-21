import PIL
import sqlite3
import time
import shutil

from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

from salesman import salesmanClass
from sup import InvoiceClass
from category import CategoryClass
from product import ProductsClass
from sales import salesClass
from bill import BillClass
from backup import BackUP

class PBS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x760+40+60")
        self.root.attributes("-fullscreen",False)
        self.root.title("Parth Inventory Software")
        self.root.config(bg = "lightblue")
        #CONTENT
        self.count_list = []
        self.COUNT()
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
        LeftMenu.place(x=0,y=102,width=200,height=625)

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
        btn_emp = Button(LeftMenu,text="Salesman",command=self.salesman,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sup = Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category = Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_prod = Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales = Button(LeftMenu,text="Sales",command=self.SALES,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_bill = Button(LeftMenu,text="Billing",command=self.Billing,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit = Button(LeftMenu,text="Exit",image=self.icon_side,command=self.confirm_EXIT,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)


        
        self.label_salesman = Label(self.root,text="Total Salesman\n["+str(self.count_list[0])+"]\n",bd=5,relief= RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.label_salesman.place(x=300,y=120,height=150,width=300)

        self.label_supplier = Label(self.root,text="Total Supplier\n["+str(self.count_list[3])+"]\n",bd=5,relief= RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.label_supplier.place(x=650,y=120,height=150,width=300)

        self.label_category = Label(self.root,text="Total Category\n["+str(self.count_list[2])+"]\n",bd=5,relief= RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.label_category.place(x=1000,y=120,height=150,width=300)

        self.label_product = Label(self.root,text="Total Product\n["+str(self.count_list[1])+"]\n",bd=5,relief= RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.label_product.place(x=300,y=320,height=150,width=300)

        self.label_sales = Label(self.root,text="Total Sales\n["+str(self.count_list[4])+"]\n",bd=5,relief= RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.label_sales.place(x=650,y=320,height=150,width=300)

        #FOOTER
        label_footer = Label(self.root,text = "Parth Inventory System", font=("times new roman", 12),bg="#5d636d",fg="white").pack(side=BOTTOM,fill=X)
        
    def COUNT(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT sm_id from salesman")
            row = cur.fetchall()
            self.count_list.append(len(row))
            cur.execute("SELECT pid from product")
            row = cur.fetchall()
            self.count_list.append(len(row))
            cur.execute("SELECT cid from category")
            row = cur.fetchall()
            self.count_list.append(len(row))
            cur.execute("SELECT invoice from supplier")
            row = cur.fetchall()
            self.count_list.append(len(row))
            cur.execute("SELECT invoiceNumber from billingTable")
            row = cur.fetchall()
            self.count_list.append(len(row))
            
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.roo1)

    def salesman(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = salesmanClass(self.new_window)

    def supplier(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = InvoiceClass(self.new_window)

    def category(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = CategoryClass(self.new_window)

    def product(self):
        self.new_ProductWindow = Toplevel(self.root)
        self.new_ProductObj = ProductsClass(self.new_ProductWindow)
    
    def Billing(self):
        self.new_ProductWindow = Toplevel(self.root)
        self.new_ProductObj = BillClass(self.new_ProductWindow)
    
    def SALES(self):
        self.new_ProductWindow = Toplevel(self.root)
        self.new_ProductObj = salesClass(self.new_ProductWindow)

    def backup(self):
        self.new_obj = BackUP.bckup(self)

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
