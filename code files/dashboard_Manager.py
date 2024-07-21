import matplotlib.pyplot as plt 
import pandas
import sqlite3
import pandas as pd
import tkinter
import PIL
import time

from backup import BackUP

from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk


class Manager:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x760+40+60")
        self.root.attributes("-fullscreen",False)
        self.root.title("Parth Inventory Software")
        self.root.config(bg = "lightblue")
        self.icon_title=PhotoImage(file="images/logo1.png")
        title = Label(self.root,text = "Parth Inventory Software",image=self.icon_title,compound=LEFT, font=("times new roman", 40, "bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)


        self.var_salesman=StringVar()
        self.sm_list=[]
        self.fetch_sm()
        '''
        self.var_fromMONTH=StringVar()
        self.var_fromDATE=StringVar()
        self.var_fromYEAR=StringVar()
        self.var_toMONTH=StringVar()
        self.var_toDATE=StringVar()
        self.var_toYEAR=StringVar()

        self.variable_fromDATE = StringVar()
        self.variable_toDATE = StringVar()
        '''
        self.var_fromMONTH=''
        self.var_fromDATE=''
        self.var_fromYEAR=''
        self.var_toMONTH=''
        self.var_toDATE=''
        self.var_toYEAR=''

        self.variable_fromDATE = ''
        self.variable_toDATE = ''
        #LOGOUT BUTTON
        btn_logout = Button(self.root,text="Logout",command=self.backup,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1200,y=10,height = 50,width = 150)

        #CLOCK
        self.label_clock = Label(self.root,text = "Welcome\t\t Date : "+str(time.strftime("%d"))+"-"+str(time.strftime("%m"))+"-"+str(time.strftime("%y")), font=("times new roman", 15),bg="#5d636d",fg="white")
        self.label_clock.place(x=0,y=70,relwidth=1,height=30)

        #LEFT MENU
        FirstRow=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        FirstRow.place(x=0,y=102,width=1430,height=105)
        self.icon_side=PhotoImage(file="images/side.png")

        label_Menu = Label(FirstRow,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)

        #Buttons
        btn_SalesReport = Button(FirstRow,text="Sales Report",command=self.SALESREPORT,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").place(x=5,y=40,width=350)
        btn_SalesManPerformance = Button(FirstRow,text="Salesman Performance",command=self.SalesManPerformance,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").place(x=360,y=40,width=350)
        btn_StockReport = Button(FirstRow,text="Stock Report",image=self.icon_side,command=self.StockReport,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").place(x=715,y=40,width=350)
        btn_exit = Button(FirstRow,text="Exit",image=self.icon_side,command=self.confirm_EXIT,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").place(x=1070,y=40,width=350)
        
        #FOOTER
        label_footer = Label(self.root,text = "Parth Inventory System", font=("times new roman", 12),bg="#5d636d",fg="white").pack(side=BOTTOM,fill=X)

        SecondRow=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        SecondRow.place(x=0,y=212,width=1430,height=210)

        txt_salesman=ttk.Combobox(self.root,textvariable=self.var_salesman,values=self.sm_list,state="readonly",justify=CENTER,font=("times new roman",15))
        txt_salesman.place(x=5,y=217,width=350,height=45)
        txt_salesman.current(0)

        self.from_date=Frame(SecondRow,bd=2,relief=RIDGE,bg="#5d636d")
        self.from_date.place(x=360,y=2,width=350,height=206)
        lbl_from_date=Label(self.from_date,text = "From Date", font=("times new roman", 16),bg="#5d636d",fg="white").pack(side=TOP,fill=X)
        self.fromDATE = ttk.Combobox(SecondRow,textvariable=self.var_fromDATE,values=('Select','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'),state="readonly",justify=CENTER,font=("times new roman",15))
        self.fromDATE.place(x=365,y=40,width=340,height=50)
        self.fromDATE.current(0)

        self.fromMONTH = ttk.Combobox(SecondRow,textvariable=self.var_fromMONTH,values=('Select','01','02','03','04','05','06','07','08','09','10','11','12'),state="readonly",justify=CENTER,font=("times new roman",15))
        self.fromMONTH.place(x=365,y=95,width=340,height=50)
        self.fromMONTH.current(0)

        self.fromYEAR = ttk.Combobox(SecondRow,textvariable=self.var_fromYEAR,values=('Select','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026','2027','2028','2029','2030','2031','2032','2033','2034','2035','2036','2037','2038','2039','2040','2041','2042','2043','2045','2046','2047','2048','2049','2050'),state="readonly",justify=CENTER,font=("times new roman",15))
        self.fromYEAR.place(x=365,y=150,width=340,height=50)
        self.fromYEAR.current(0)


        self.to_date=Frame(SecondRow,bd=2,relief=RIDGE,bg="#5d636d")
        self.to_date.place(x=715,y=2,width=350,height=206)
        lbl_to_date=Label(self.to_date,text = "To Date", font=("times new roman", 16),bg="#5d636d",fg="white").pack(side=TOP,fill=X)
        self.toDATE = ttk.Combobox(SecondRow,textvariable=self.var_toDATE,values=('Select','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'),state="readonly",justify=CENTER,font=("times new roman",15))
        self.toDATE.place(x=720,y=40,width=340,height=50)
        self.toDATE.current(0)

        self.toMONTH = ttk.Combobox(SecondRow,textvariable=self.var_toMONTH,values=('Select','01','02','03','04','05','06','07','08','09','10','11','12'),state="readonly",justify=CENTER,font=("times new roman",15))
        self.toMONTH.place(x=720,y=95,width=340,height=50)
        self.toMONTH.current(0)

        self.toYEAR = ttk.Combobox(SecondRow,textvariable=self.var_toYEAR,values=('Select','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026','2027','2028','2029','2030','2031','2032','2033','2034','2035','2036','2037','2038','2039','2040','2041','2042','2043','2045','2046','2047','2048','2049','2050'),state="readonly",justify=CENTER,font=("times new roman",15))
        self.toYEAR.place(x=720,y=150,width=340,height=50)
        self.toYEAR.current(0)
        
        RightFrame = Frame(self.root,bd=2,relief=RIDGE,bg="white").place(x=1075,y=214,width=350,height=205)
        self.photo=PhotoImage(file="images/report1.png")

        label_Menu = Label(self.root,image=self.photo).place(x=1083,y=216,width=340,height=198)
        

        '''
        btn_clear = Button(SecondRow,text="Clear",image=self.icon_side,command=self.CLEAR,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").place(x=1070,y=5,width=350,height=45)
        btn_GenerateReport = Button(SecondRow,text="Generate Report",image=self.icon_side,command=self.GR,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").place(x=1070,y=55,width=350,height=45)
        btn_Print = Button(SecondRow,text="Print",image=self.icon_side,command=self.Print,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="lightgreen",bd=3,cursor="hand2").place(x=1070,y=105,width=350,height=45)
        '''
        
    def getDATE(self):
        self.variable_fromDATE = str(str(self.fromYEAR.get())+"-"+str(self.fromMONTH.get())+"-"+str(self.fromDATE.get()))
        #rint(self.variable_fromDATE)

        self.variable_toDATE = str(str(self.toYEAR.get()+"-"+str(self.toMONTH.get())+"-"+str(self.toDATE.get())))
        #print(self.variable_toDATE)
    
    def CLEAR(self):
        self.var_salesman.set('Select')
        """
        self.var_fromMONTH = 
        self.var_fromDATE = ''
        self.var_fromYEAR = ''
        self.var_toMONTH = ''
        self.var_toDATE = ''
        self.var_toYEAR = ''

        self.variable_fromDATE = ''
        self.variable_toDATE = ''
        """
    def GR(self):
        pass
    def Print(self):
        pass
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



    def SALESREPORT(self):
        try:
            self.getDATE()
            conn = sqlite3.connect("pbs.db")
            cursor = conn.cursor()
            cursor.execute("select invoiceNumber from billingTable where sm LIKE '"+self.var_salesman.get()+"%' and billdate BETWEEN ('"+str(self.variable_fromDATE)+"') and ('"+str(self.variable_toDATE)+"')")
            print(("select invoiceNumber from billingTable where sm LIKE '"+self.var_salesman.get()+"%' and billdate BETWEEN ('"+str(self.variable_fromDATE)+"') and ('"+str(self.variable_toDATE)+"')"))
            index = cursor.fetchall()

            billCount=0
            for indexs in index:
                billCount = billCount + 1

            cursor.execute("select total from billingTable where sm LIKE '%"+self.var_salesman.get()+"%' and billdate BETWEEN ('"+str(self.variable_fromDATE)+"') and ('"+str(self.variable_toDATE)+"')")
            print("select total from billingTable where sm LIKE '%"+self.var_salesman.get()+"%' and billdate BETWEEN ('"+str(self.variable_fromDATE)+"') and ('"+str(self.variable_toDATE)+"')")
            tamt=cursor.fetchall()
            billTotal = 0
            countTotal = 0
            for amt in tamt:
                #print(amt)
                billTotal = billTotal + int(amt[countTotal])
            #c=[]
            c=[(0,0)]
            for i in range (0,len(index)):
                d = index[i]
                e = tamt[i]
                b=(d[0],e[0])
                c.append(b)
            c.pop(0)
            #print(c)
            df = pd.DataFrame(c)
            df.columns=['Invoice Number', 'Amount']
            plt.bar(df['Invoice Number'],df['Amount'])#,'r^-',linewidth=2,markersize=12)
            plt.title("Salesman Sales Report")
            #a = index[len(index)-1] + 5
            #print(index[len(index)-1])
            A = index[len(index)-1]
            B = int(A[0] + 2)
            C = index[0]
            D = int(C[0] - 2)            
            plt.xlim(D,B)
            plt.xlabel("Invoice Number")
            plt.ylabel("Amount")
            plt.grid()
            plt.show()

        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)


    def SalesManPerformance(self):
        try:
            self.getDATE()
            self.fetch_sm()
            #print(self.sm_list)
            #self.sm_list
            conn = sqlite3.connect("pbs.db")
            cursor = conn.cursor()
            total = []
            TOTAL=[]
            t = 0
            for i in range(1,len(self.sm_list)):
                #total.append(0)
                t = 0
                total = []
                cursor.execute("SELECT total from billingTable where sm = '"+str(self.sm_list[i]+"' ") + "and billdate BETWEEN ('"+str(self.variable_fromDATE)+"') and ('"+str(self.variable_toDATE)+"')")
                numOfBill = cursor.fetchall()
                for n in numOfBill:
                    #print(n[0])
                    total.append(n[0])
                #print(str(self.sm_list[i])+" = "+str(total))
                for j in range(0,len(total)):
                    t = t + total[j]
                a = (self.sm_list[i],t)
                TOTAL.append(a)
            #print(TOTAL)
            df = pd.DataFrame(TOTAL)
            df.columns=['Salesman', 'Total']
            plt.plot(df['Salesman'],df['Total'],'r^-',linewidth=2,markersize=12)
            plt.title("Salesman Performance Graph")
            plt.xlabel("Salesman")
            plt.ylabel("Total")
            plt.grid()
            plt.show()

        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)


    def StockReport(self):
        try:
            conn = sqlite3.connect("pbs.db")
            cursor = conn.cursor()
            cursor.execute("Select name,quantity from product where quantity > 0")
            product = cursor.fetchall()
            df = pd.DataFrame(product)
            cursor.execute("Select MIN(quantity) from product")
            minQTY = cursor.fetchone()
            df.columns=['Name', 'Quantity']
            plt.bar(df['Name'],df['Quantity'])#,'r^-',linewidth=2,markersize=12)
            plt.title("Current active stock report")
            plt.ylim(int(minQTY[0])-3,int(minQTY[0])+3)
            plt.xlabel("Name")
            plt.ylabel("Quantity")
            plt.grid()
            plt.show()

        except Exception as error:
            messagebox.showerror("ERROR",f"Error due to :  "+str(error),parent=self.root)


    def confirm_EXIT(self):
        root1=Tk()
        self.root1=root1
        self.root1.title("EXIT")
        root1.geometry("500x200")
        self.label_exit = Label(self.root1,text="Do you want to exit without backup?",bd=5,relief= RIDGE,bg="white",fg="black",font=("times new roman",16,"bold")).pack(fill=X)
        btn_exit_yes = Button(self.root1,text = "YES",command=quit,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").place(x=50,y=100,width=100,height=50)
        btn_exit_no = Button(self.root1,text = "NO",command=root1.destroy,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").place(x=150,y=100,width=100,height=50)

    def backup(self):
        self.new_obj = BackUP.bckup(self)        

if __name__ == "__main__":
    root = Tk()
    obj = Manager(root)
    root.mainloop()
