import PIL
import sqlite3
from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

from backup import BackUP

class ProductsClass:
    def __init__(self,roo1):
        self.roo1 = roo1
        self.roo1.geometry("1400x600+40+60")
        self.roo1.title("Parth Inventory Software")
        self.roo1.config(bg = "lightblue")
        self.roo1.attributes("-fullscreen", False)
        self.roo1.focus_force()

        self.var_pid = StringVar()
        self.var_productName = StringVar()
        self.var_category = StringVar()
        self.var_supplier = StringVar()
        self.var_price = StringVar()
        self.var_quantity = StringVar()
        self.var_status = StringVar()

        self.var_pid = StringVar()
        self.var_productName = StringVar()
        self.var_category = StringVar()
        self.var_supplier = StringVar()
        self.var_price = StringVar()
        self.var_quantity = StringVar()
        self.var_status = StringVar()

        self.cat_list = []
        self.sup_list = []        
        self.pid_list = []
        self.name_list = []
        self.fetch_cat_sup()
        self.pidGET()
        self.var_pidONE = StringVar()

        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()


        self.pf = Frame(self.roo1,bd=2,relief=RIDGE,bg="white").place(x=0,y=10,width=465,height=580)

        title=Label(self.roo1,text="Product Details",font=("times new roman",20,"bold"),bg="#0f4d7d",fg="white").place(x=2,y=12,width=462)

        lbl_pid=Label(self.roo1,text="Product id",font=("times new roman",20,"bold"),bg="white").place(x=30,y=60)
        lbl_category=Label(self.roo1,text="Category",font=("times new roman",20,"bold"),bg="white").place(x=30,y=120)
        lbl_supplier=Label(self.roo1,text="Supplier",font=("times new roman",20,"bold"),bg="white").place(x=30,y=180)
        lbl_productName=Label(self.roo1,text="Product Name",font=("times new roman",20,"bold"),bg="white").place(x=30,y=240)
        lbl_price=Label(self.roo1,text="Price",font=("times new roman",20,"bold"),bg="white").place(x=30,y=300)
        lbl_quantity=Label(self.roo1,text="Quantity",font=("times new roman",20,"bold"),bg="white").place(x=30,y=360)
        lbl_status=Label(self.roo1,text="Status",font=("times new roman",20,"bold"),bg="white").place(x=30,y=420)
        
        txt_pid = Entry(self.roo1,textvariable=self.var_pidONE,font=("times new roman",20,"bold"),bg="lightyellow").place(x=220,y=60,width=230,height=45)

        txt_category=ttk.Combobox(self.roo1,textvariable=self.var_category,values=self.cat_list,state="readonly",justify=CENTER,font=("times new roman",15))
        txt_category.place(x=220,y=120,width=230,height=45)
        
        txt_supplier=ttk.Combobox(self.roo1,textvariable=self.var_supplier,values=self.sup_list,state="readonly",justify=CENTER,font=("times new roman",15))
        txt_supplier.place(x=220,y=180,width=230,height=45)

        txt_productName=Entry(self.roo1,textvariable=self.var_productName,font=("times new roman",20,"bold"),bg="lightyellow").place(x=220,y=240,width=230,height=45)

        txt_price=Entry(self.roo1,textvariable=self.var_price,font=("times new roman",20,"bold"),bg="lightyellow").place(x=220,y=300,width=230,height=45)

        txt_quantity=Entry(self.roo1,textvariable=self.var_quantity,font=("times new roman",20,"bold"),bg="lightyellow").place(x=220,y=360,width=230,height=45)
        
        txt_status=ttk.Combobox(self.roo1,textvariable=self.var_status,values=("Select","Active","Inactive"),state="readonly",justify=CENTER,font=("times new roman",15))
        txt_status.place(x=220,y=420,width=230,height=45)
        #txt_status.current(0)
        
        btn_save=Button(self.roo1,text="Save",command=self.SAVE,font=("times new roman",18),bg="#0f4d7d",fg="white",bd=2,relief=RIDGE,cursor="hand2")
        btn_save.place(x=10,y=485,width=85,height=50)

        btn_update=Button(self.roo1,text="Update",command=self.UPDATE,font=("times new roman",18),bg="#0f4d7d",fg="white",bd=2,relief=RIDGE,cursor="hand2")
        btn_update.place(x=100,y=485,width=85,height=50)

        btn_delete=Button(self.roo1,text="Delete",command=self.DELETE,font=("times new roman",18),bg="#0f4d7d",fg="white",bd=2,relief=RIDGE,cursor="hand2")
        btn_delete.place(x=190,y=485,width=85,height=50)
        
        btn_clear=Button(self.roo1,text="Clear",command=self.CLEAR,font=("times new roman",18),bg="#0f4d7d",fg="white",bd=2,relief=RIDGE,cursor="hand2")
        btn_clear.place(x=280,y=485,width=85,height=50)

        btn_exit = Button(self.roo1,text="EXIT",command=self.roo1.destroy,font=("times new roman",18),bg="#0f4d7d",fg="white",bd=2,relief=RIDGE,cursor="hand2")
        btn_exit.place(x=370,y=485,width=85,height=50)

#==================================================================================================================================================================================================================================

        #SEARCH

        SearchFrame=LabelFrame(self.roo1,text="Search Product",bg="white",font=("times new roman",25,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=480,y=10,width = 1300, height = 90)

        #Options

        self.cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Name","Category","Supplier"),state="readonly",justify=CENTER,font=("times new roman",15))
        self.cmb_search.place(x=10,y=10,width=180)
        self.cmb_search.current(0)

        text_search=Entry(SearchFrame,textvariable=self.var_searchtext,font=("times new roman",15),bg="lightyellow").place(x=200,y=10,height=30)
        btn_search=Button(SearchFrame,text="Search",command=self.SEARCH,font=("times new roman",15),bg="#0f4d7d",fg="white",cursor="hand2").place(x=415,y=10,width=150,height=30)

        btn_clr=Button(SearchFrame,text="Clear",command=self.CLEAR,font=("times new roman",15),bg="#0f4d7d",fg="white",cursor="hand2").place(x=580,y=10,width=150,height=30)        

#==================================================================================================================================================================================================================================

        #Product DETAILS
        product_frame=Frame(self.roo1,bd=3,relief=RIDGE)
        product_frame.place(x=480,y=100,height=390)

        scroll_x = Scrollbar(product_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(product_frame,orient=VERTICAL)

        self.ProductTable=ttk.Treeview(product_frame,columns=("pid","name","category","supplier","price","quantity","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.ProductTable.xview)
        scroll_y.config(command=self.ProductTable.yview)

#==================================================================================================================================================================================================================================
        self.ProductTable.heading("pid",text="Product Id")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("category",text="Category")
        self.ProductTable.heading("supplier",text="Supplier")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("quantity",text="Quantity")
        self.ProductTable.heading("status",text="Status")
      
#==================================================================================================================================================================================================================================
        self.ProductTable["show"]="headings"
#==================================================================================================================================================================================================================================
        self.ProductTable.column("pid",width=110)
        self.ProductTable.column("name",width=110)
        self.ProductTable.column("category",width=180)
        self.ProductTable.column("supplier",width=180)
        self.ProductTable.column("price",width=110)
        self.ProductTable.column("quantity",width=110)
        self.ProductTable.column("status",width=110)
        
#==================================================================================================================================================================================================================================
        self.ProductTable.pack(fill=BOTH,expand=1)
        
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#==================================================================================================================================================================================================================================
    def show(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows=cur.fetchall()
            colnames = cur.description

            array = [[0 for _ in range(len(colnames))] for _ in range(len(rows))]
            for i in range (0,len(rows)):
                A = rows[i]
                for j in range(0,len(colnames)):
                    if(j==7):
                        array[i][j] = A[j]#"********"
                    else:
                        array[i][j] = A[j]

            self.ProductTable.delete(*self.ProductTable.get_children())
            
            for row in range (0,len(rows)):
                self.ProductTable.insert('',END,values=array[row])
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.roo1)



    def get_data(self,ev):
        f = self.ProductTable.focus()
        content=self.ProductTable.item(f)
        row = content['values']
        self.var_pidONE.set(row[0])
        self.var_productName.set(row[1])
        self.var_category.set(row[2])
        self.var_supplier.set(row[3])
        self.var_price.set(row[4])
        self.var_quantity.set(row[5])
        self.var_status.set(row[6])
        self.show()
        #Search data

    def SEARCH(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            if(self.var_searchby.get()=="Select"):
                messagebox.showerror("ERROR","Select search by selecting options",parent=self.roo1)
            elif (self.var_searchby.get()==""):
                messagebox.showerror("ERROR","Please input search data",parent=self.roo1)
            else:
                cur.execute("SELECT * FROM product WHERE "+self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows=cur.fetchall()
                if(len(rows)!=0):
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("ERROR","Norecord found",parent=self.roo1)
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.roo1)

#==================================================================================================================================================================================================================================
    #Save data
    def SAVE(self):
        print(self.var_pidONE.get(),self.var_productName.get(),self.var_category.get(),self.var_supplier.get(),self.var_price.get(),self.var_quantity.get(),self.var_status.get(),)
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            if (self.var_category.get()=="") or (self.var_supplier.get()=="Select") or (self.var_productName.get()=="") or (self.var_price.get()=="") or (self.var_quantity.get()=="") or (self.var_status.get()==""):
                messagebox.showerror("ERROR","All fields are required",parent=self.roo1)

            else:
                cur.execute("SELECT * FROM product where pid = ?",self.var_pidONE.get())
                row=cur.fetchone()
                
                if (row!=None):
                    messagebox.showerror("ERROR","This Product is already present, try different",parent=self.roo1)
                else:
                    cur.execute("INSERT INTO product(pid, name, category, supplier, price, quantity, status) values(?,?,?,?,?,?,?)",(self.var_pidONE.get(),
                        self.var_productName.get(),
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_status.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success","product added successfully",parent=self.roo1)
                self.show()
                self.CLEAR()
        
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.roo1)

#==================================================================================================================================================================================================================================
    #Update data
    def UPDATE(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            if (self.var_pidONE.get()==""):
                messagebox.showerror("ERROR","Product Id is a required field",parent=self.roo1)

            else:
                cur.execute("SELECT * FROM product WHERE pid = ?",(self.var_pidONE.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","Invalid Product Id",parent=self.roo1)
                else:
                    cur.execute("UPDATE product set name = ?, category=?, supplier=?, price=?, quantity=?, status=? WHERE pid = ?" ,(
                        self.var_productName.get(),
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_status.get(),
                        self.var_pidONE.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success","product updated successfully",parent=self.roo1)
                self.show()
                self.CLEAR()
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.roo1)


#==================================================================================================================================================================================================================================
    #Delete data
    def DELETE(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            if (self.var_pidONE.get()==""):
                messagebox.showerror("ERROR","Product Id is a required field",parent=self.roo1)

            else:
                cur.execute("SELECT * FROM product WHERE name = ?",(self.var_productName.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","Invalid Product Id",parent=self.roo1)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.roo1)
                    if(op==True):
                        cur.execute("DELETE FROM product WHERE pid = ?",(self.var_pidONE.get(),))
                        con.commit()
                        messagebox.showinfo("DELETE","product deleted successfully",parent = self.roo1)
                self.show()
                self.CLEAR()

        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.roo1)


#==================================================================================================================================================================================================================================
    #Clear screen
    def CLEAR(self):
        self.var_pidONE.set("")
        self.var_productName.set("")
        self.var_category.set("Select")
        self.var_supplier.set("Select")
        self.var_price.set("")
        self.var_quantity.set("")
        self.var_status.set("Select")
        self.var_searchby.set("Select")
        self.var_searchtext.set("")
        self.show()
#==================================================================================================================================================================================================================================
    def pidGET(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        self.pid_list.append("Empty")
        try:
            cur.execute("Select pid from product")
            pid = cur.fetchall()

            if len(pid)>0:
                del self.pid_list[:]
                for i in pid:
                    self.pid_list.append(i[0])

            cur.execute("Select name from product")
            name = cur.fetchall()
            if len(name)>0:
                del self.name_list[:]
                for i in name:
                    self.name_list.append(i[0])
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.roo1)


    def fetch_cat_sup(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")

        try:
            cur.execute("SELECT name FROM category")
            cat = cur.fetchall()

            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            

            cur.execute("SELECT name FROM supplier")
            sup = cur.fetchall()

            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.roo1)

        
#==================================================================================================================================================================================================================================

if __name__ == "__main__":
    roo1=Tk()
    obj = ProductsClass(roo1)
    roo1.mainloop()
