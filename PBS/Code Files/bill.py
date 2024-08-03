import sqlite3
import PIL
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk,messagebox
from backup import BackUP
import os
import tempfile
from PIL import Image,ImageTk
import time
import datetime


class BillClass:
    def __init__(self, root):
        self.root = root
        #self.root.geometry("1400x760+40+60")
        self.root.attributes("-fullscreen", True)
        self.root.title("Parth Inventory Software")
        self.root.config(bg = "lightblue")
        self.chk_print=0
        self.bill_amnt = 0
        self.discount = 0
        self.cart_list = []
        self.net_pay = 0
        self.txt_bill_area = ''
        self.var_date = StringVar()
        

        # TITLE
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Parth Inventory Software", image=self.icon_title, compound=LEFT,font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # LOGOUT BUTTON
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow",fg="black",command=self.backup, bd=2,relief=RIDGE,cursor="hand2")
        btn_logout.place(x=1150, y=10, height=50, width=150)
        btn_exit = Button(self.root,text="Exit",command=self.root.destroy,font=("times new roman",15,"bold"),bg="yellow",fg="black",bd=2,relief=RIDGE,cursor="hand2")
        btn_exit.place(x=1350,y=10,width=150,height=50)

        # CLOCK
        self.label_clock = Label(self.root, text="Welcome\t\t Date : "+str(time.strftime("%d"))+"-"+str(time.strftime("%m"))+"-"+str(time.strftime("%y")), font=("times new roman", 15), bg="#5d636d", fg="white")
        self.label_clock.place(x=0, y=70, relwidth=1, height=30)

        # Product Frame
        self.var_search=StringVar()
        ProductFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        ProductFrame1.place(x=6, y=110, width=764, height=400)

        titleLabel = Label(ProductFrame1, text="All Products", font=("goudy old style", 20, "bold"), bg="#262626", fg="white")
        titleLabel.pack(side=TOP, fill=X)

        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=752,height=40)

        lbl_search=Label(ProductFrame2,text="Search Product | By Name ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5,height=25)

        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=345,y=5,height=25)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=485,y=5,width=150,height=25)
        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=645,y=5,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show all",command=self.show,font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=235,y=5,width=100,height=25)
        
        #Supplier Frame
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=92,width=752,height=273)

        scroll_x = Scrollbar(ProductFrame3,orient=HORIZONTAL)
        scroll_y = Scrollbar(ProductFrame3,orient=VERTICAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","quantity","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.product_Table.xview)
        scroll_y.config(command=self.product_Table.yview)


        self.product_Table.heading("pid",text="PID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("quantity",text="Quantity")
        self.product_Table.heading("status",text="Status")
        

        self.product_Table["show"]="headings"

        self.product_Table.column("pid",width=100)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("quantity",width=100)
        self.product_Table.column("status",width=100)


        self.product_Table.pack(fill=BOTH,expand=1)

        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrame1,text="Note:'Enter 0 Quantity to remove product from cart.",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=780,y=110,width=750,height=80)

        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35,height=30)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=150,height=30)

        lbl_contact=Label(CustomerFrame,text="Contact No.",font=("times new roman",15),bg="white").place(x=250,y=35,height=30)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=350,y=35,width=140,height=30)

        self.x =datetime.datetime.now()
        self.Y = self.x.year
        self.M = self.x.month
        self.D = self.x.day

        lbl_date=Label(CustomerFrame,text="Bill Date",font=("times new roman",15),bg="white").place(x=510,y=35,height=30)
        txt_date=Label(CustomerFrame,text=(str(self.Y)+"-"+str(self.M)+"-"+str(self.D)),font=("times new roman",13),bg="lightyellow").place(x=590,y=35,width=140,height=30)


        #=====Cal Cart Frame======================================
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=6,y=515,width=764,height=400)


            #=====Calculator Frame==============================================
        self.var_cal_input=StringVar() 
        
        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=465,y=10,width=280,height=385)

        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_Frame,text='7',font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)

        btn_4=Button(Cal_Frame,text='4',font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)

        btn_1=Button(Cal_Frame,text='1',font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text='3',font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)

        btn_0=Button(Cal_Frame,text='0',font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='c',font=('arial',15,'bold'),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',font=('arial',15,'bold'),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)

            #=====Cart Frame==============================================

        self.cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        self.cart_Frame.place(x=5,y=10,width=450,height=385)
        self.lbl_cartTitle=Label(self.cart_Frame,text="Cart \t Total Product: [0]",font=("goudy old style",15),bg="lightgray")
        self.lbl_cartTitle.pack(side=TOP,fill=X)


        scrolly=Scrollbar(self.cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(self.cart_Frame,columns=("pid","name","price","quantity"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.pack(side=BOTTOM,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("quantity",text="quantity")
        
        self.CartTable["show"]="headings"
        self.CartTable.column("pid",width=15)
        self.CartTable.column("name",width=60)
        self.CartTable.column("price",width=30)
        self.CartTable.column("quantity",width=30)
        
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)

        #=====ADD Cart Widgets Frame=========================================
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_cartquantity=StringVar()
        self.var_salesman=StringVar()
        self.var_stock=StringVar()
        self.var_total= 0
        self.sm_list = []
        self.fetch_sm()
        

        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=780,y=200,width=750,height=200)
        
        self.icon_title = PhotoImage(file="images/sales3.png")
        title = Label(Add_CartWidgetsFrame, text="Parth Inventory Software", image=self.icon_title, compound=LEFT,font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=410, y=5, width=600,height=440)

        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5,width=190,height=25)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow").place(x=205,y=5,width=190,height=25)

        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price Per quantity",font=("times new roman",15),bg="white").place(x=5,y=42,width=190,height=25)
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow").place(x=205,y=42,width=190,height=25)
        
        lbl_p_quantity=Label(Add_CartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=5,y=80,width=190,height=25)
        txt_p_quantity=Entry(Add_CartWidgetsFrame,textvariable=self.var_cartquantity,font=("times new roman",15),bg="lightyellow").place(x=205,y=80,width=190,height=25)

        lbl_salesman = Label(Add_CartWidgetsFrame,text="Salesman",font=("times new roman",15),bg="white")
        lbl_salesman.place(x=5,y=117,width=190,height=25)
        txt_salesman=ttk.Combobox(self.root,textvariable=self.var_salesman,values=self.sm_list,state="readonly",justify=CENTER,font=("times new roman",15))
        txt_salesman.place(x=985,y=317,width=190,height=25)
        #txt_p_salesman=Entry(Add_CartWidgetsFrame,textvariable=self.var_salesman,font=("times new roman",15),bg="lightyellow").place(x=205,y=117,width=190,height=25)
        txt_salesman.current(0)
        


        buttonAdd_CartWidgetsFrame=Frame(Add_CartWidgetsFrame,bd=2,relief=RIDGE,bg="white",background="white")
        buttonAdd_CartWidgetsFrame.place(x=0,y=160,width=748,height=38)

        self.lbl_inStock=Label(buttonAdd_CartWidgetsFrame,text="In Stock [9999]",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=5,width=190,height=25)

        btn_clear_cart=Button(buttonAdd_CartWidgetsFrame,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=5,width=150,height=25)
        btn_add_cart=Button(buttonAdd_CartWidgetsFrame,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=5,width=180,height=25)


 #       ========================billing area==================
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billFrame.place(x=780,y=550,width=750,height=365)

        Btitle = Label(billFrame, text="Customer Bill", font=("Goudy old style", 20, "bold"),bg="#FFA07A", fg="white").pack(side=TOP, fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #=============================billing buttons=================
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billMenuFrame.place(x=780,y=405,width=750,height=140)

        self.lbl_amnt=Label(billMenuFrame,text='Bill Amount\n[0]',font=("goudy old style",13,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=10,y=5,width=235,height=60)

        self.lbl_discount=Label(billMenuFrame,text='Discount\n[5%]',font=("goudy old style",13,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=255,y=5,width=235,height=60)

        self.lbl_net_pay=Label(billMenuFrame,text='Net Pay\n[0]',font=("goudy old style",13,"bold"),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=500,y=5,width=235,height=60)

        btn_print=Button(billMenuFrame,text='Print',command=self.print_bill,cursor='hand2',font=("goudy old style",13,"bold"),bg="lightblue",fg="white")
        btn_print.place(x=10,y=70,width=235,height=60)

        btn_clear_all=Button(billMenuFrame,text='Clear All',command=self.clear_all,cursor='hand2',font=("goudy old style",13,"bold"),bg="gray",fg="white")
        btn_clear_all.place(x=255,y=70,width=235,height=60)

        btn_generate=Button(billMenuFrame,text='Generate Bill',command=self.generate_bill,cursor='hand2',font=("goudy old style",13,"bold"),bg="#009688",fg="white")
        btn_generate.place(x=500,y=70,width=235,height=60)

        #==============================Footer===========================
        footer=Label(self.root,text="Parth Inventory System",font=("times new roman", 12),bg="#5d636d",fg="white",bd=0,cursor="hand2").pack(side=BOTTOM,fill=X)

        self.show()
        self.bill_top()

    def backup(self):
        self.new_obj = BackUP.bckup(self)    

    def fetch_sm(self):
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

    def show(self):
        con=sqlite3.connect(database=r'C:\Users\parth\OneDrive\Desktop\PBS\pbs.db')
        cur=con.cursor()
        try:
            cur.execute("select pid,name,price,quantity,status from product where status='Active' and quantity>0")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to show: {str(ex)}",parent=self.root)

    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                #print(row)
                self.CartTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to show cart: {str(ex)}",parent=self.root)

        self.show()

    def search(self):   
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("ERROR","Search input should be required",parent=self.root)
            else:
                cur.execute("SELECT pid, name, price, quantity, status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows=cur.fetchall()
                if(len(rows)!=0):
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("ERROR","No record found!!!",parent=self.root)
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to search :  ",{str(error)},parent=self.root)


    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[4])
        self.show()
        #self.var_quantity.set(row[5])

    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        #pid,name,price,quantity,stock
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_stock.set(row[3])
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        #self.var_quantity.set(row[5])
        self.show()


    def generate_bill(self):
        if self.var_cname.get()==''or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are required",parent=self.root)
        elif len(self.cart_list)<0:
            messagebox.showerror("Error",f"Please add product to the cart",parent=self.root)
        else:
            #Bill top
            self.bill_top() 
            #Bill middle
            self.bill_middle()
            #Bill Bottom
            self.bill_bottom()
            con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
            cur = con.cursor()
            try:
                cur.execute("SELECT invoiceNumber from billingTable")
                rows=cur.fetchall()
                a = len(rows)
                invoice = rows[a-1][0] + 1
                name = self.var_cname.get()
                num = self.var_contact.get()
                sm = self.var_salesman.get()
                totalAmount = self.var_total
                x =datetime.datetime.now()
                Y = x.year
                M = x.month
                D = x.day
                date = str(Y)+"-"+str(M)+"-"+str(D)
                print(date)
                cur.execute("insert into billingTable (invoiceNumber, customerName,customerPhone,sm,total,billdate) values(?,?,?,?,?,?)",(invoice,name,num,sm,totalAmount,date))
                
            except Exception as error:
                messagebox.showerror("ERROR",f"Error due to search :  ",{str(error)},parent=self.root)
            con.commit()
            fp=open(f'bill/{str(invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved","Bill has been generated/Save in Backend",parent=self.root)
            self.chk_print=1
        self.show()
    
    

    def bill_top(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT invoiceNumber from billingTable")
            rows=cur.fetchall()
            a = len(rows)
            invoice = rows[a-1][0] + 1
            
            
        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to search :  ",{str(error)},parent=self.root)
        bill_top_temp = f'''
                                 Parth-Inventory
    Phone No. 98938*****                                         Indore-452016
    {str("="*83)}
    Customer Name: {self.var_cname.get()}       Ph no. : {self.var_contact.get()}         Bill No. {str(invoice)}
    {str("="*83)}
    Product Name                  Quantity                       Price
    {str("="*83)}
    '''
        self.txt_bill_area.delete('1.0', END)
        self.txt_bill_area.insert('1.0', bill_top_temp)
        self.show()

    def bill_middle(self):
        con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
        cur = con.cursor()
        cur1 = con.cursor()
        try:
            for row in self.cart_list:
                #print(row)
                pid=row[0]   
                name=row[1]
                cur1.execute("SELECT quantity from product where pid=?",(pid))
                qty = cur1.fetchone()                
                quantity=int(qty[0])-int(row[3])
                #quantity=row[3]
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n\t"+name+"\t\t\t"+row[3]+"\t\t\t\tRs."+price)
            #=========Update quantity in product table======================================================
                cur.execute('Update product set quantity=? where pid=?',(
                quantity,
                pid,
                ))   
                con.commit()
            con.close()    
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to billmiddle: {str(ex)}",parent=self.root)



    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*83)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*83)}\n
        '''
        
        #self.txt_bill_area.append(bill_bottom_temp)
        self.txt_bill_area.insert('1500.0', bill_bottom_temp)
        #self.txt_bill_area.insert('2.0', bill_bottom_temp)
        self.show()


    
    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_cartquantity.set('')
        self.lbl_inStock.config(text=f"In Stock")
        self.var_stock.set('')
        self.show()
    
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_cartquantity.set('')
        self.lbl_inStock.config(text=f"In Stock")
        self.var_stock.set('')
        self.txt_bill_area.delete('1.0',END)
        self.lbl_cartTitle.config(text=f"Cart \t Total Product: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()



    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror('Error',"Please select product from the list",parent=self.root)
        elif self.var_cartquantity.get()=='':
            messagebox.showerror('Error',"Quantity is Required",parent=self.root)
        elif int(self.var_cartquantity.get())>int(self.var_cartquantity.get()):
            messagebox.showerror('Error',"Invalid Quantity",parent=self.root)
        else:
            self.price_cal=int(self.var_cartquantity.get())*int(self.var_price.get())
            self.price_cal=(self.price_cal)
            self.price_cal=self.var_cartquantity.get()
            self.cart_data=[self.var_pid.get(),self.var_pname.get(),self.var_price.get(),self.var_cartquantity.get(),self.var_stock.get()]
            #=====update cart==========================================
            #self.cart_list.append(self.cart_data)
            #print(self.cart_list)
            #self.cart_list.pop(0)
            #print(self.cart_list)
            
            self.cart_list.append(self.cart_data)
            self.show_cart()  
            self.bill_updates()
            self.clear_cart()
        self.show()

    def bill_updates(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            #pid,name,price,quantity,status
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
        self.discount=(self.bill_amnt*5)/100
        self.net_pay=self.bill_amnt-self.discount
        self.var_total = self.net_pay
        self.lbl_amnt.config(text=f'Bill Amnt\n{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')    
        self.lbl_cartTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")
        self.show()

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl.clock.after(200,self.update_date_time)

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print',"Please wait while printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror('Print',"Please generate bill, to print the receipt",parent=self.root)
            

#==========================billing area================================
    

#=================All Functions=====================================
    def get_input(self,num):
          xnum=self.var_cal_input.get()+str(num)
          self.var_cal_input.set(xnum)
    def clear_cal(self):
        self.var_cal_input.set('')
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

          
          
if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()
