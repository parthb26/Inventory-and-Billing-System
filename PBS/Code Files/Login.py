from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
from dashboard import PBS
class LOGIN:
    def __init__(self,root):
        self.root = root
        root.geometry("550x400+365+160")
        root.title("Login Page")
        self.root.config(bg = "lightblue")
        self.var_USERNAME = StringVar()
        self.var_PASSWORD = StringVar()
        username=''
        label_username = Label(self.root, text="Username",font=("times new roman", 20, "bold"),bg="#5d636d",fg="white")
        label_username.place(x=25,y=75,width = 225, height = 50)

        entry_username = Entry(self.root,textvariable=self.var_USERNAME,font=("times new roman", 20, "bold"),bg="#5d636d",fg="white")
        entry_username.place(x=275,y=75,width = 225, height = 50)

        label_password = Label(self.root, text="Password",font=("times new roman", 20, "bold"),bg="#5d636d",fg="white")
        label_password.place(x=25,y=150,width = 225, height = 50)

        entry_password = Entry(self.root,textvariable=self.var_PASSWORD, show="*",font=("times new roman", 20, "bold"),bg="#5d636d",fg="white")
        entry_password.place(x=275,y=150,width = 225, height = 50)

        # Create a login button
        login_button = Button(self.root, text="Login", command=self.validate_login,font=("times new roman", 20, "bold"),bg="#5d636d",fg="white",cursor="hand2")
        login_button.place(x=175,y=250,width = 225, height = 50)

        self.sm_list = []

    def get_sm_list(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        self.sm_list.append("Empty")

        try:
            cur.execute("SELECT DISTINCT sm FROM billingTable")
            sm = cur.fetchall()

            if len(sm)>0:
                del self.sm_list[:]
                self.sm_list.append("Select")
                for i in sm:
                    self.sm_list.append(i[0])
            
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)        
        #print(self.sm_list)
        con.close()

    def validate_login(self):
        self.get_sm_list()
        #print(self.sm_list)
        username = self.var_USERNAME.get()
        password = self.var_PASSWORD.get()
        
        conn = sqlite3.connect("user_credentials.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            if username=="Admin":
                messagebox.showinfo("Login Successful", "Welcome, " + username)
                os.startfile("dashboard_Admin.py")
                self.root.destroy()

            elif username=="Manager":
                messagebox.showinfo("Login Successful", "Welcome, " + username)
                os.startfile("dashboard_Manager.py")
                self.root.destroy()

            elif username=="Distributor":
                messagebox.showinfo("Login Successful", "Welcome, " + username)
                os.startfile("dashboard.py")
                #self.DASHBOARD()
                self.root.destroy()
            #quit()
            else:
                messagebox.showinfo("Login Successful", "Welcome, " + username)
                os.startfile("dashboard_Salesman.py")
                self.root.destroy()

        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

        conn.close()
        self.currentSession(username)
        return username
    
    def DASHBOARD(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = PBS(self.new_window)

    def currentSession(self,username):
        file1 = open("currentsession.py", "w")
        line = "User = '"+ str(username)+"'"
        file1.writelines(line)

# Create the main window
if __name__ == "__main__":
    root=Tk()
    obj = LOGIN(root)

    root.mainloop()
