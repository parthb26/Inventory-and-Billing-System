import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk,messagebox

class SQLITE3:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+40+60")
        self.root.attributes("-fullscreen",False)
        self.root.title("Admin Management")
        self.root.config(bg = "white")
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=10,y=10,width=400,height=475)
        btnCREATE = Button(LeftMenu,text="CREATE",command=self.SWITCH_CASE_CREATE_TABLE,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btnDELETE = Button(LeftMenu,text="DELETE",command=self.SWITCH_CASE_DELETE_TABLE,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btnEXIT = Button(LeftMenu,text="EXIT",command=self.root.destroy,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        #self.First()
        #self.CONN()

    def First(self):
        if(self.whatToDo==1):
            self.query = self.SWITCH_CASE_CREATE_TABLE()
        elif(self.whatToDo==2):
            self.query = self.SWITCH_CASE_DELETE_TABLE()
        else:
            print("Invalid Choice")

    def CONN(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbsTEST.db")
        cur = con.cursor()
        try:
            cur.execute(self.query)
            row = cur.fetchall()
            con.commit()
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)


    def SWITCH_CASE_CREATE_TABLE(self):
        self.whatToDo=1
        self.choice = int(input("Enter which table you want to select \n(1)Salesman\n(2)Supplier\n(3)Category\n(4)Products\n(5)User_credentials\nhere : "))
        print(self.whatToDo)
        if self.choice == 1:
            self.query = "CREATE TABLE IF NOT EXISTS salesman(sm_id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT,gender TEXT NOT NULL,contact TEXT NOT NULL UNIQUE,dob TEXT,doj TEXT,password TEXT,usertype TEXT,address TEXT,salary TEXT)"
            print("Salesman TABLE created successfully")
        elif self.choice == 2:
            self.query = "CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text, contact text, desc text);"
            print("Supplier TABLE created successfully")
        elif self.choice == 3:
            self.query = "CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text);"
            print("Category TABLE created successfully")
        elif self.choice == 4:
            self.query = "CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,name text, cateogry text, supplier text,price real not null, quantity integer, status text);"
            print("Product TABLE created successfully")
        elif self.choice == 5:
            self.query = "CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)"
            print("User_credentials TABLE created successfully")
        else:
            print("Invalid Choice")
        return self.query

    def SWITCH_CASE_DELETE_TABLE(self):
        self.whatToDo=2
        self.choice = int(input("Enter which table you want to select \n(1)Salesman\n(2)Supplier\n(3)Category\n(4)Products\n(5)User_credentials\nhere : "))
        if self.choice == 1:
            self.query = "DROP TABLE IF EXISTS salesman;"
            print("Salesman TABLE DELETED successfully")
        elif self.choice == 2:
            self.query = "DROP TABLE IF EXISTS supplier;"
            print("Supplier TABLE DELETED successfully")
        elif self.choice == 3:
            self.query = "DROP TABLE IF EXISTS category;"
            print("Category TABLE DELETED successfully")
        elif self.choice == 4:
            self.query = "DROP TABLE IF EXISTS product;"
            print("Product TABLE DELETED successfully")
        elif self.choice == 5:
            self.query = "DROP TABLE IF EXISTS users;"
            print("User_credentials TABLE DELETED successfully")
        else:
            print("Invalid Choice")
        return self.query


if __name__ == "__main__":
    '''
    whatToDo = int(input("Enter do you want to create table or delete table\n(1)Create\n(2)Delete\nhere : "))
    choice = int(input("Enter which table you want to select \n(1)Salesman\n(2)Supplier\n(3)Category\n(4)Products\n(5)User_credentials\nhere : "))
    if(whatToDo==1):
        query = SWITCH_CASE_CREATE_TABLE(choice)
    elif(whatToDo==2):
        query = SWITCH_CASE_DELETE_TABLE(choice)
    else:
        print("Invalid Choice")
    '''
    root=Tk()
    obj = SQLITE3(root)
    root.mainloop()