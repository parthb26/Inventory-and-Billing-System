import PIL
from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import os
class salesClass:
    def __init__(self,root):
        self.root=root
        #self.root.geometry("1400x1000+40+20")
        self.root.attributes("-fullscreen", True)
        self.root.title("Parth Inventory Software")
        self.root.config(bg = "lightblue")
        self.root.focus_force()

        self.bill_list=[]
        self.var_invoice=StringVar()
        #title===
        lbl_title = Label(self.root,text = "View Customer Bills",font = ("times new roman",30,"bold"),bg="white",fg="red",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=5,pady=5)
        
        lbl_invoice=Label(self.root,text="Invoive No",font=("times new roman",20,"bold"),bg="white").place(x=50,y=100,height=35)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",20),bg="lightyellow").place(x=190,y=100,width=180,height=35)
        
        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",20,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=380,y=100,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",20,"bold"),bg="lightgray",cursor="hand2").place(x=510,y=100,width=120,height=35)
        btn_exit = Button(self.root,text="Exit",command=self.root.destroy,font=("times new roman",20,"bold"),bg="yellow",fg="black",cursor="hand2").place(x=640,y=100,width=120,height=35)


        #====Bill List====================================
        sales_Frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_Frame.place(x=15,y=140,width=170,height=750)

        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.sales_List=Listbox(sales_Frame,font=("times new roman",20),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_List.yview)
        self.sales_List.pack(fill=BOTH,expand=1)
        self.sales_List.bind("<ButtonRelease-1>",self.get_data)


        #====Bill Area====================================
        bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=190,y=140,width=1335,height=750)

        lbl_title2 = Label(bill_Frame,text = " Customer Bill Area",font = ("times new roman",20,"bold"),bg="orange",).pack(side=TOP,fill=X)
        
        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        self.bill_area=Text(bill_Frame,font=("times new roman",20),bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        '''
        #===Image=============================
        self.MenuLogo1 = Image.open("images/cat2.png")
        self.MenuLogo1 = self.MenuLogo1.resize((200,250),PIL.Image.Resampling.LANCZOS)
        self.MenuLogo1 = ImageTk.PhotoImage(self.MenuLogo1)

        self.lbl_im2 = Label(self.root,image=self.MenuLogo1,bd=2,relief=RAISED).place(x=700,y=110)
        '''




        self.show()
#====================================================================================
    def show(self):
        del self.bill_list[:]
        self.sales_List.delete(0,END)
        #print(os.listdir('../IMS')) bill1.txt, category.py
        for i in os.listdir('bill'):
            #print(i.split('.'),i.split(.)[-1])
            if i.split('.')[-1]=='txt':
                self.sales_List.insert(END,i)
                self.bill_list.append(i.split('.')[0])



    def get_data(self,ev):
        index_=self.sales_List.curselection()
        file_name=self.sales_List.get(index_)
        #print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invaild Invoice No.",parent=self.root)


    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)

if __name__=="__main__":
    root=Tk()
    obj=salesClass(root)
    root.mainloop()
    
