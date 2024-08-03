import PIL
import sqlite3
from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk


class CategoryClass:

    def __init__(self,root):
        self.var_category_id = StringVar()
        self.var_name = StringVar()
#==================================================================================================================================================================================================================================
#==================================================================================================================================================================================================================================

        #SCREEN
        self.root = root
        self.root.geometry("1400x850+40+20")
        self.root.title("Parth Inventory Software")
        self.root.config(bg = "lightblue")
        self.root.attributes("-fullscreen", False)
        self.root.focus_force()

        lbl_title = Label(self.root,text = "Manage Product Category",font = ("times new roman",30,"bold"),bg="white",fg="red",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=5,pady=5)


        lbl_cid = Label(self.root,text = "Enter Category Id",font = ("times new roman",20,"bold"),bg="white").place(x=100,y=100,height=50,width=350)
        lbl_cid = Entry(self.root,textvariable=self.var_category_id,font = ("times new roman",20,"bold"),bg="lightyellow").place(x=460,y=100,height=50,width=350)
        lbl_name = Label(self.root,text = "Enter Category Name",font = ("times new roman",20,"bold"),bg="white").place(x=100,y=175,height=50,width=350)
        lbl_name = Entry(self.root,textvariable=self.var_name,font = ("times new roman",20,"bold"),bg="lightyellow").place(x=460,y=175,height=50,width=350)
        
        btn_add = Button(self.root,text="Add",command=self.ADD,font = ("times new roman",20,"bold"),bg="lightgreen").place(x=820,y=100,height=50,width=150)
        btn_delete = Button(self.root,text="Delete",command=self.DELETE,font = ("times new roman",20,"bold"),bg="lightgreen").place(x=980,y=100,height=50,width=150)
        btn_clear = Button(self.root,text="Clear",command=self.CLEAR,font = ("times new roman",20,"bold"),bg="lightgreen").place(x=820,y=175,height=50,width=150)
        btn_exit = Button(self.root,text="Exit",command=self.root.destroy,font = ("times new roman",20,"bold"),bg="lightgreen").place(x=980,y=175,height=50,width=150)
        
        category_frame=Frame(self.root,bd=3,relief=RIDGE)
        category_frame.place(x=0,y=650,relwidth=1,height=200)

        scroll_x = Scrollbar(category_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(category_frame,orient=VERTICAL)

        self.categoryTable=ttk.Treeview(category_frame,columns=("cid","name"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.categoryTable.xview)
        scroll_y.config(command=self.categoryTable.yview)

#==================================================================================================================================================================================================================================
        self.categoryTable.heading("cid",text="Category Id")
        self.categoryTable.heading("name",text="Name")
        
#==================================================================================================================================================================================================================================
        self.categoryTable["show"]="headings"
#==================================================================================================================================================================================================================================
        self.categoryTable.column("cid",width=100)
        self.categoryTable.column("name",width=100)

#==================================================================================================================================================================================================================================
        self.categoryTable.pack(fill=BOTH,expand=1)

        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)

        self.MenuLogo = Image.open("images/cat.png")
        self.MenuLogo = self.MenuLogo.resize((680,250),PIL.Image.Resampling.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        self.lbl_im1 = Label(self.root,image=self.MenuLogo,bd=2,relief=RAISED).place(x=10,y=250)

        self.MenuLogo1 = Image.open("images/cat2.png")
        self.MenuLogo1 = self.MenuLogo1.resize((680,250),PIL.Image.Resampling.LANCZOS)
        self.MenuLogo1 = ImageTk.PhotoImage(self.MenuLogo1)

        self.lbl_im2 = Label(self.root,image=self.MenuLogo1,bd=2,relief=RAISED).place(x=710,y=250)

        self.show()

    def ADD(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            if (self.var_name.get()=="" or self.var_category_id.get()==""):
                messagebox.showerror("ERROR","Category Id/Name is a required field",parent=self.root)

            else:
                cur.execute("SELECT * FROM category WHERE cid = ?",(self.var_category_id.get(),))
                row = cur.fetchall()
                if row!=None:
                    cur.execute("INSERT INTO category (cid, name) values(?,?)",(
                    self.var_category_id.get(),
                    self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","category added successfully",parent=self.root)

                else:
                    messagebox.showerror("ERROR","This Category Id is already assigned, try different",parent=self.root)

            self.CLEAR()
            self.show()

        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to in save:  "+str(error),parent=self.root)

    def DELETE(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()

        try:
            if (self.var_name.get()==""):
                messagebox.showerror("ERROR","Category Name is a required field",parent=self.root)

            else:
                cur.execute("SELECT * FROM category WHERE name = ?",(self.var_name.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","Invalid Category Name",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if(op==True):
                        cur.execute("DELETE FROM category WHERE name = ?",(self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("DELETE","category deleted successfully",parent = self.root)
                        self.show()
                        self.CLEAR()
                        
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)


    def get_data(self,ev):
        f = self.categoryTable.focus()
        content=self.categoryTable.item(f)
        row = content['values']
        self.var_category_id.set(row[0])
        self.var_name.set(row[1])

    def show(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM category")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            
            for row in range (0,len(rows)):
                self.categoryTable.insert('',END,values=rows[row])
        
        except Exception as error:
            pass
            #messagebox.showerror("ERROR",f"Error due to in show :  "+str(error),parent=self.root)

    
    def CLEAR(self):
        self.var_category_id.set("")
        self.var_name.set("")
        self.show()

#==================================================================================================================================================================================================================================
if __name__ == "__main__":
    root=Tk()
    obj=CategoryClass(root)
    root.mainloop()
#==================================================================================================================================================================================================================================
