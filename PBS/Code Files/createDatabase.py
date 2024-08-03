import sqlite3

def create_emp_db():
   con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
   cur=con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS salesman(sm_id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT,gender TEXT NOT NULL,contact TEXT NOT NULL UNIQUE,dob TEXT,doj TEXT,password TEXT,usertype TEXT,address TEXT,salary TEXT)")
   con.commit()

def create_purchase_record_db():
   con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
   cur=con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS purchase_record(record_number INTEGER PRIMARY KEY AUTOINCREMENT,invoice_number INTEGER,godown_id TEXT NOT NULL, godown_name TEXT NOT NULL, invoice_date TEXT, godown_GST TEXT NOT NULL,godown_address TEXT, distributor_GST TEXT NOT NULL, distributor_address TEXT)")
   con.commit()


def create_purchase_receipt_db():
   con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
   cur=con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS purchase_receipt(invoice_number INTEGER PRIMARY KEY,record_number TEXT,item_number INTEGER ,item_code TEXT UNIQUE, item_name TEXT ,purchase_price REAL, selling_price REAL, tax_percent REAL DEFAULT 0.0,tax_amount REAL DEFAULT 0.0, total_amount REAL ,FOREIGN KEY(record_number) REFERENCES purchase_record(record_number ))")
   con.commit()


def supplier():
   con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
   cur=con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text, contact text, desc text);")
   con.commit()


def category():
   con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
   cur=con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text);")
   con.commit()

def product():
   con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\pbs.db")
   cur=con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,name text, cateogry text, supplier text,price real not null, quantity integer, status text);")
   con.commit()

def UC():
   con=sqlite3.connect(database=r"C:\Users\parth\OneDrive\Desktop\PBS\user_credentials.db")
   cur=con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
   cur.execute("INSERT INTO USER VALUES('Admin','Adm_8420')")

   


if __name__ == "__main__":
   print("Which database would you like to create?\n(1)Salesman Database\n(2)Purchase Record Database\n(3)Purchase Receipt Database\n(4)Supplier Database\n(5)Category Database\n(6)Product Database\n(7)User Credentials\n")
   choice = int(input("Enter your choice here : "))
   while(choice!=0):
      if (choice>7):
         print("Invalid input.")
         break; 
      
      if(choice==1):
         create_emp_db()
         print("Salesman Database created successfully")

      if(choice==2):
         create_purchase_record_db()
         print("Purchase Record Database created successfully")

      if(choice==3):
         create_purchase_receipt_db()
         print("Purchase Receipt Database created successfully")

      if(choice==4):
         supplier()
         print("Supplier Database created successfully")

      if(choice==5):
         category()
         print("Category Database created successfully")

      if(choice==6):
         product()
         print("Product Database created successfully")

      if(choice==7):
         UC()
         print("User Credentials Database created successfully")

      choice = int(input("Enter your choice here : "))