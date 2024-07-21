import sqlite3
from sqlite3CON import SQLITE3
import shutil
import os

from backup import BackUP
class admin:
    def __init__(self):
        pass
    def backup(self):
        new_obj = BackUP.bckup(self)

    def SQLITE(self):
        print("Enter what do you want to do\n(1)Create\n(2)Delete\n(3)Add Distributor or Salesman or Manager\n(4)Restore Database\n(5)Backup Database\n(6)Exit")
        self.whatToDO = int(input("here : "))
        if self.whatToDO <= 6:
            if (self.whatToDO>=3):
                if(self.whatToDO==3):
                    self.choice = int(input("Enter which table you want to select \n(1)Distributor\n(2)Salesman\n(3)Manager\nhere : "))
                    self.query = self.ADDuser(self.choice)
                    self.CONN(self.whatToDO,self.query)
                elif (self.whatToDO==4):
                    os.startfile('C:/Users/parth/OneDrive/Desktop/pbs_backup/restore.py')
                    print("Successfully restored database")
                    self.choice=0
                elif (self.whatToDO==5):
                    print("Successfully backedup database")
                    self.backup()
                    self.choice=0
            else:
                self.choice = int(input("Enter which table you want to select \n(1)Salesman\n(2)Supplier\n(3)Category\n(4)Products\n(5)User_credentials\nhere : "))
                if(self.whatToDO==1):
                    self.query = self.SWITCH_CASE_CREATE_TABLE(self.choice)
                    self.CONN(self.whatToDO,self.query)
                elif(self.whatToDO==2):
                    self.query = self.SWITCH_CASE_DELETE_TABLE(self.choice)
                    self.CONN(self.whatToDO,self.query)
                else:
                    print("Invalid Choice")


            '''
            print("\n\nEnter what do you want to do\n(1)Create\n(2)Delete\n(3)Add Distributor or Salesman or Manager\n(4)Restore Database\n(5)Backup Database\n(6)Exit")
            self.whatToDO = int(input("here : "))
            print(self.whatToDO)
            '''
            return self.choice

    def ADDuser(self,choice):
        username = str(input("Enter the Username here : "))
        password = str(input("Enter the password here : "))
        self.query = str("INSERT into users values('"+str(username)+"','"+str(password)+"');")
        print(username," added successfully")
        return self.query

    def SWITCH_CASE_CREATE_TABLE(self,choice):
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

    def SWITCH_CASE_DELETE_TABLE(self,choice):
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

    def CONN(self,whatToDo,query):
        if self.whatToDO <3:
            con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        elif self.whatToDO==3:
            con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\user_credentials.db")
        else:
            print("Invalid self.choice")
        cur = con.cursor()
        cur.execute(self.query)
        row = cur.fetchall()
        con.commit()


if __name__ == "__main__":
    obj = admin()
    obj.SQLITE()
