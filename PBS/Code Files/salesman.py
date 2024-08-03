import PIL
import sqlite3

from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox

class salesmanClass:

    def __init__(self,root):

#==================================================================================================================================================================================================================================
#==================================================================================================================================================================================================================================

        #SCREEN
        self.root = root
        self.root.geometry("1400x650+40+60")
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
        self.var_sm_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_usertype=StringVar()
        self.var_address=StringVar()
        self.var_salary=StringVar()

#==================================================================================================================================================================================================================================
#==================================================================================================================================================================================================================================

        #SEARCH

        SearchFrame=LabelFrame(self.root,text="Search Salesman",bg="white",font=("times new roman",25,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=50,y=0,width = 1300, height = 90)

        #Options

        self.cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state="readonly",justify=CENTER,font=("times new roman",15))
        self.cmb_search.place(x=10,y=10,width=180)
        self.cmb_search.current(0)

        text_search=Entry(SearchFrame,textvariable=self.var_searchtext,font=("times new roman",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.SEARCH,font=("times new roman",15),bg="lightgreen",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        btn_clr=Button(SearchFrame,text="Clear",command=self.CLEAR,font=("times new roman",15),bg="lightgreen",fg="white",cursor="hand2").place(x=580,y=9,width=150,height=30)        

#==================================================================================================================================================================================================================================
#==================================================================================================================================================================================================================================

        #MIDDLE TITLE
        title=Label(self.root,text="Salesman Details",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=50,y=100,width=1250)
 
#==================================================================================================================================================================================================================================

        #ENTRY FIELDS

        #ROW 1
        label_sm_id=Label(self.root,text="Salesman Id",font=("times new roman",15),fg="black",bg="white").place(x=50,y=150,width=125,height=50)
        text_sm_id=Entry(self.root,textvariable=self.var_sm_id,font=("times new roman",15),fg="black",bg="lightyellow").place(x=180,y=150,width=150,height=50)

        label_gender=Label(self.root,text="Gender",font=("times new roman",15),fg="black",bg="white").place(x=450,y=150,width=125,height=50)
        self.cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),state="readonly",justify=CENTER,font=("times new roman",15))
        self.cmb_gender.place(x=580,y=150,width=150,height=50)
        self.cmb_gender.current(0)

        label_contact=Label(self.root,text="Contact",font=("times new roman",15),fg="black",bg="white").place(x=850,y=150,width=125,height=50)
        text_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15),fg="black",bg="lightyellow").place(x=980,y=150,width=150,height=50)

#==================================================================================================================================================================================================================================

        #ROW 2
        label_name=Label(self.root,text="Name",font=("times new roman",15),fg="black",bg="white").place(x=50,y=225,width=125,height=50)
        text_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15),fg="black",bg="lightyellow").place(x=180,y=225,width=150,height=50)

        label_dob=Label(self.root,text="DOB",font=("times new roman",15),fg="black",bg="white").place(x=450,y=225,width=125,height=50)
        text_dob=Entry(self.root,textvariable=self.var_dob,font=("times new roman",15),fg="black",bg="lightyellow").place(x=580,y=225,width=150,height=50)

        label_doj=Label(self.root,text="DOJ",font=("times new roman",15),fg="black",bg="white").place(x=850,y=225,width=125,height=50)
        text_doj=Entry(self.root,textvariable=self.var_doj,font=("times new roman",15),fg="black",bg="lightyellow").place(x=980,y=225,width=150,height=50)

#==================================================================================================================================================================================================================================

        #ROW 3
        label_email=Label(self.root,text="Email",font=("times new roman",15),fg="black",bg="white").place(x=50,y=300,width=125,height=50)
        text_email=Entry(self.root,textvariable=self.var_email,font=("times new roman",15),fg="black",bg="lightyellow").place(x=180,y=300,width=150,height=50)

        label_password=Label(self.root,text="Password",font=("times new roman",15),fg="black",bg="white").place(x=450,y=300,width=125,height=50)
        text_password=Entry(self.root,textvariable=self.var_password,font=("times new roman",15),fg="black",bg="lightyellow").place(x=580,y=300,width=150,height=50)

        label_usertype=Label(self.root,text="User Type",font=("times new roman",15),fg="black",bg="white").place(x=850,y=300,width=125,height=50)
        self.cmb_usertype=ttk.Combobox(self.root,textvariable=self.var_usertype,values=("Select","Admin","Manager","Distributor","Salesman"),state="readonly",justify=CENTER,font=("times new roman",15))
        self.cmb_usertype.place(x=980,y=300,width=150,height=50)
        self.cmb_usertype.current(0)

#==================================================================================================================================================================================================================================

        #ROW 4
        label_address=Label(self.root,text="Address",font=("times new roman",15),fg="black",bg="white").place(x=50,y=375,width=125,height=50)
        text_address=Entry(self.root,textvariable=self.var_address,font=("times new roman",15),fg="black",bg="lightyellow").place(x=180,y=375,width=150,height=50)

        label_salary=Label(self.root,text="Salary",font=("times new roman",15),fg="black",bg="white").place(x=450,y=375,width=125,height=50)
        text_salary=Entry(self.root,textvariable=self.var_salary,font=("times new roman",15),fg="black",bg="lightyellow").place(x=580,y=375,width=150,height=50)
        

#==================================================================================================================================================================================================================================
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
#==================================================================================================================================================================================================================================

        #EMP DETAILS
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=450,relwidth=1,height=200)

        scroll_x = Scrollbar(emp_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(emp_frame,orient=VERTICAL)

        self.salesmanTable=ttk.Treeview(emp_frame,columns=("sm_id","name","email","gender","contact","dob","doj","password","usertype","address","salary"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.salesmanTable.xview)
        scroll_y.config(command=self.salesmanTable.yview)

#==================================================================================================================================================================================================================================
        self.salesmanTable.heading("sm_id",text="")
        self.salesmanTable.heading("name",text="Name")
        self.salesmanTable.heading("email",text="Email")
        self.salesmanTable.heading("gender",text="Gender")
        self.salesmanTable.heading("contact",text="Contact")
        self.salesmanTable.heading("dob",text="DOB")
        self.salesmanTable.heading("doj",text="DOJ")
        self.salesmanTable.heading("password",text="Password")
        self.salesmanTable.heading("usertype",text="Usertype")
        self.salesmanTable.heading("address",text="Address")
        self.salesmanTable.heading("salary",text="Salary")
#==================================================================================================================================================================================================================================
        self.salesmanTable["show"]="headings"
#==================================================================================================================================================================================================================================
        self.salesmanTable.column("sm_id",width=90)
        self.salesmanTable.column("name",width=100)
        self.salesmanTable.column("email",width=100)
        self.salesmanTable.column("gender",width=100)
        self.salesmanTable.column("contact",width=100)
        self.salesmanTable.column("dob",width=100)
        self.salesmanTable.column("doj",width=100)
        self.salesmanTable.column("password",width=100)
        self.salesmanTable.column("usertype",width=100)
        self.salesmanTable.column("address",width=200)
        self.salesmanTable.column("salary",width=100)

#==================================================================================================================================================================================================================================
        self.salesmanTable.pack(fill=BOTH,expand=1)
        
        self.salesmanTable.bind("<ButtonRelease-1>",self.get_data)

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
    #Fetch data
    def get_data(self,ev):
        f = self.salesmanTable.focus()
        content=self.salesmanTable.item(f)
        row = content['values']
        self.var_sm_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_password.set(row[7])
        self.var_usertype.set(row[8])
        self.var_address.set(row[9])
        self.var_salary.set(row[10])

#==================================================================================================================================================================================================================================
    #Show data
    def show(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM salesman")
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

            self.salesmanTable.delete(*self.salesmanTable.get_children())
            
            for row in range (0,len(rows)):
                self.salesmanTable.insert('',END,values=array[row])
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)

#==================================================================================================================================================================================================================================
    #Search data
    def SEARCH(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            if(self.var_searchby.get()=="Select"):
                messagebox.showerror("ERROR","Select search by selecting options",parent=self.root)
            elif (self.var_searchby.get()==""):
                messagebox.showerror("ERROR","Please input search data",parent=self.root)
            else:
                cur.execute("SELECT * FROM salesman WHERE "+self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows=cur.fetchall()
                if(len(rows)!=0):
                    self.salesmanTable.delete(*self.salesmanTable.get_children())
                    for row in rows:
                        self.salesmanTable.insert('',END,values=row)
                else:
                    messagebox.showerror("ERROR","Norecord found",parent=self.root)
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)

#==================================================================================================================================================================================================================================
    #Save data
    def SAVE(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        con1=sqlite3.connect(database=r"user_credentials.db")
        cur1 = con1.cursor()
        try:
            if (self.var_sm_id.get()==""):
                messagebox.showerror("ERROR","Salesman Id is a required field",parent=self.root)

            else:
                cur.execute("SELECT * FROM salesman WHERE sm_id = ?",(self.var_sm_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("ERROR","This Salesman Id is already assigned, try different",parent=self.root)
                else:
                    cur1.execute("INSERT INTO USERS (username, password) VALUES(?,?)",(self.var_sm_id.get(),self.var_password.get()))
                    cur.execute("INSERT INTO salesman (sm_id, name, email, gender, contact, dob, doj, password, usertype, address, salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_sm_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_password.get(),
                        self.var_usertype.get(),
                        self.var_address.get(),
                        self.var_salary.get()
                        ))
                    con.commit()
                    con1.commit()
                    messagebox.showinfo("Success","salesman added successfully",parent=self.root)
                    self.show()
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)

#==================================================================================================================================================================================================================================
    #Update data
    def UPDATE(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        con1=sqlite3.connect(database=r"user_credentials.db")
        cur1 = con1.cursor()

        try:
            if (self.var_sm_id.get()==""):
                messagebox.showerror("ERROR","Salesman Id is a required field",parent=self.root)

            else:
                cur.execute("SELECT * FROM salesman WHERE sm_id = ?",(self.var_sm_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","Invalid Salesman Id",parent=self.root)
                else:
                    cur1.execute("UPDATE USERS set password = ? where username = ?",(self.var_password.get(),self.var_sm_id.get()))
                    cur.execute("UPDATE salesman set name=?, email=?, gender=?, contact=?, dob=?, doj=?, password=?, usertype=?, address=?, salary=? WHERE sm_id = ?" ,(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_password.get(),
                        self.var_usertype.get(),
                        self.var_address.get(),
                        self.var_salary.get(),
                        self.var_sm_id.get()
                        ))
                    con.commit()
                    con1.commit()
                    messagebox.showinfo("Success","salesman updated successfully",parent=self.root)
                    self.CLEAR()
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)

#==================================================================================================================================================================================================================================
    #Delete data
    def DELETE(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        con1=sqlite3.connect(database=r"user_credentials.db")
        cur1 = con1.cursor()

        try:
            if (self.var_sm_id.get()==""):
                messagebox.showerror("ERROR","Salesman Id is a required field",parent=self.root)

            else:
                cur.execute("SELECT * FROM salesman WHERE sm_id = ?",(self.var_sm_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","Invalid Salesman Id",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if(op==True):
                        cur1.execute("DELETE FROM USERS WHERE username = ?",(self.var_sm_id.get(),))
                        cur.execute("DELETE FROM salesman WHERE sm_id = ?",(self.var_sm_id.get(),))
                        con.commit()
                        con1.commit()
                        messagebox.showinfo("DELETE","salesman deleted successfully",parent = self.root)
                        self.show()
                        self.CLEAR()
                        
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)

#==================================================================================================================================================================================================================================
    #Clear screen
    def CLEAR(self):
        self.var_sm_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_password.set("")
        self.var_usertype.set("")
        self.var_address.set("")
        self.var_salary.set("")
        self.var_searchtext.set("")
        self.var_searchby.set("Select")
        self.show()


#==================================================================================================================================================================================================================================
#==================================================================================================================================================================================================================================

#==================================================================================================================================================================================================================================
if __name__ == "__main__":
    root=Tk()
    obj=salesmanClass(root)
    root.mainloop()
#==================================================================================================================================================================================================================================
