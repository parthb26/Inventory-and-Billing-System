import PIL
import sqlite3

from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox

class InvoiceClass:

    def __init__(self,root):

#==================================================================================================================================================================================================================================
#==================================================================================================================================================================================================================================

        #SCREEN
        self.root = root
        self.root.geometry("1400x650+40+120")
        self.root.title("Parth Inventory Software")
        self.root.config(bg = "lightblue")
        self.root.attributes("-fullscreen", False)
        self.root.focus_force()

#==================================================================================================================================================================================================================================
#==================================================================================================================================================================================================================================

        #ALL variable

        #Search
        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()

        #Fields
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_desc=StringVar()
#==================================================================================================================================================================================================================================
#==================================================================================================================================================================================================================================

        #SEARCH

        SearchFrame=LabelFrame(self.root,text="Search Invoice",bg="white",font=("times new roman",25,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=50,y=0,width = 1300, height = 90)

        #Options

        lbl_search=Label(SearchFrame,text="Search by Invoice Number",font=("times new roman",15))
        lbl_search.place(x=10,y=10,width=400)

        text_search=Entry(SearchFrame,textvariable=self.var_searchtext,font=("times new roman",15),bg="lightyellow").place(x=400,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.SEARCH,font=("times new roman",15),bg="lightgreen",fg="white",cursor="hand2").place(x=610,y=9,width=150,height=30)

        btn_clr=Button(SearchFrame,text="Clear",command=self.CLEAR,font=("times new roman",15),bg="lightgreen",fg="white",cursor="hand2").place(x=780,y=9,width=150,height=30)        

#==================================================================================================================================================================================================================================
#==================================================================================================================================================================================================================================

        #MIDDLE TITLE
        title=Label(self.root,text="Supplier Details",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=50,y=100,width=1300)
 
#==================================================================================================================================================================================================================================

        #ENTRY FIELDS

        #ROW 1
        label_sup_invoice=Label(self.root,text="Invoice",font=("times new roman",15),fg="black",bg="white").place(x=50,y=150,width=125,height=50)
        text_sup_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("times new roman",15),fg="black",bg="lightyellow").place(x=180,y=150,width=150,height=50)


#==================================================================================================================================================================================================================================

        #ROW 2
        label_name=Label(self.root,text="Name",font=("times new roman",15),fg="black",bg="white").place(x=50,y=225,width=125,height=50)
        text_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15),fg="black",bg="lightyellow").place(x=180,y=225,width=150,height=50)


#==================================================================================================================================================================================================================================

        #ROW 3
        label_contact=Label(self.root,text="Contact",font=("times new roman",15),fg="black",bg="white").place(x=50,y=300,width=125,height=50)
        text_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15),fg="black",bg="lightyellow").place(x=180,y=300,width=150,height=50)


#==================================================================================================================================================================================================================================

        #ROW 4
        label_desc=Label(self.root,text="Description",font=("times new roman",15),fg="black",bg="white").place(x=50,y=375,width=125,height=50)
        text_desc=Entry(self.root,textvariable=self.var_desc,font=("times new roman",15),fg="black",bg="lightyellow").place(x=180,y=375,width=150,height=50)


#==================================================================================================================================================================================================================================

        #BUTTONS
        btn_save=Button(self.root,text="Save",command=self.SAVE,font=("times new roman",18),bg="lightgreen",fg="white",bd=2,relief=RIDGE,cursor="hand2")

        btn_save.place(x=780,y=375,width=100,height=50)

        btn_update=Button(self.root,text="Update",command=self.UPDATE,font=("times new roman",18),bg="lightgreen",fg="white",bd=2,relief=RIDGE,cursor="hand2")
        btn_update.place(x=885,y=375,width=100,height=50)

        btn_delete=Button(self.root,text="Delete",command=self.DELETE,font=("times new roman",18),bg="lightgreen",fg="white",bd=2,relief=RIDGE,cursor="hand2")
        btn_delete.place(x=990,y=375,width=100,height=50)
        
        btn_clear=Button(self.root,text="Clear",command=self.CLEAR,font=("times new roman",18),bg="lightgreen",fg="white",bd=2,relief=RIDGE,cursor="hand2")
        btn_clear.place(x=1095,y=375,width=100,height=50)

        btn_exit = Button(self.root,text="EXIT",command=self.root.destroy,font=("times new roman",18),bg="lightgreen",fg="white",bd=2,relief=RIDGE,cursor="hand2")
        btn_exit.place(x=1200,y=375,width=100,height=50)

#==================================================================================================================================================================================================================================

        #sup DETAILS
        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=0,y=450,relwidth=1,height=200)

        scroll_x = Scrollbar(sup_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(sup_frame,orient=VERTICAL)

        self.supplierTable=ttk.Treeview(sup_frame,columns=("invoice","name","contact","desc"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.supplierTable.xview)
        scroll_y.config(command=self.supplierTable.yview)

#==================================================================================================================================================================================================================================
        self.supplierTable.heading("invoice",text="Invoice Number")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("desc",text="Description")
        
#==================================================================================================================================================================================================================================
        self.supplierTable["show"]="headings"
#==================================================================================================================================================================================================================================
        self.supplierTable.column("invoice",width=100)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=200)

#==================================================================================================================================================================================================================================
        self.supplierTable.pack(fill=BOTH,expand=1)

        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#==================================================================================================================================================================================================================================
    #Fullscreen enable
    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.tk.attributes("-fullscreen", self.state)
        return "break"
    
    #Fullscreen disable
    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

#==================================================================================================================================================================================================================================
    #Show data
    def show(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            
            for row in range (0,len(rows)):
                for i in range(0,4):
                    self.supplierTable.insert('',END,values=rows[i])
        
        except Exception as error:
            pass
            #messagebox.showerror("ERROR",f"Error due to in show :  "+str(error),parent=self.root)

#==================================================================================================================================================================================================================================
    #Get Data
    def get_data(self,ev):
        f = self.supplierTable.focus()
        content=self.supplierTable.item(f)
        row = content['values']
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.var_desc.set(row[3])

#==================================================================================================================================================================================================================================

    #Search data
    def SEARCH(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            if (self.var_searchtext.get()==""):
                messagebox.showerror("ERROR","Invoice number is required",parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice = ?",(self.var_searchtext.get(),))
                rows=cur.fetchall()
                if rows!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in range (0,len(rows)):
                        for i in range(0,4):
                            self.supplierTable.insert('',END,values=rows[i])
                else:
                    messagebox.showerror("ERROR","No record found",parent=self.root)
        except Exception as error:
            pass
            #messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)

#==================================================================================================================================================================================================================================
    #Save data
    def SAVE(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            if (self.var_sup_invoice.get()==""):
                messagebox.showerror("ERROR","Invoice is a required field",parent=self.root)

            else:
                cur.execute("SELECT * FROM supplier WHERE invoice = ?",(self.var_sup_invoice.get(),))
                row = cur.fetchall()
                if row!=None:
                    cur.execute("INSERT INTO supplier (invoice, name, contact, desc) values(?,?,?,?)",(
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.var_desc.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success","supplier added successfully",parent=self.root)

                else:
                    messagebox.showerror("ERROR","This Invoice Number is already assigned, try different",parent=self.root)

            self.CLEAR()
            self.show()

        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to in save:  "+str(error),parent=self.root)

#==================================================================================================================================================================================================================================
    #Update data
    def UPDATE(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()

        try:
            if (self.var_sup_invoice.get()==""):
                messagebox.showerror("ERROR","Invoice number is a required field",parent=self.root)

            else:
                cur.execute("SELECT * FROM supplier WHERE invoice = ?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","Invalid Invoice Number",parent=self.root)
                else:
                    cur.execute("UPDATE supplier set name=?, contact=?, desc=? WHERE invoice = ?" ,(
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.var_desc.get(), 
                        self.var_sup_invoice.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success","supplier updated successfully",parent=self.root)
                    self.CLEAR()
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)

#==================================================================================================================================================================================================================================
    #Delete data
    def DELETE(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()

        try:
            if (self.var_sup_invoice.get()==""):
                messagebox.showerror("ERROR","Invoice Number is a required field",parent=self.root)

            else:
                cur.execute("SELECT * FROM supplier WHERE invoice = ?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","Invalid Invoice Number",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if(op==True):
                        cur.execute("DELETE FROM supplier WHERE invoice = ?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("DELETE","supplier deleted successfully",parent = self.root)
                        self.show()
                        self.CLEAR()
                        
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)

#==================================================================================================================================================================================================================================
    #Clear screen
    def CLEAR(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_desc.set("")
        self.var_searchtext.set("")
        self.show()

#==================================================================================================================================================================================================================================
if __name__ == "__main__":
    root=Tk()
    obj=InvoiceClass(root)
    root.mainloop()
#==================================================================================================================================================================================================================================
