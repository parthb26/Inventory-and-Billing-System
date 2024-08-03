import matplotlib.pyplot as plt 
import pandas
import sqlite3
import pandas as pd

conn = sqlite3.connect("pbs.db")
cursor = conn.cursor()
'''
cursor.execute("SELECT * FROM test ")
user = cursor.fetchall()
#for users in user:
    #print(users)
print((user))
df = pd.DataFrame(user)
df.columns=['Username','Password']

plt.bar(df['Username'],df['Password'])
plt.show()
'''
'''
plt.plot(df['Username'],df['Password'],'r^-',linewidth=2,markersize=12)
plt.ylim(1000,18000)
plt.title("TEST")
plt.xlabel("Username")
plt.ylabel("Password")
plt.grid()
plt.show()
'''

'''
plt.pie(df['Username'],df['Password'])
plt.show()
conn.close()

'''
conn = sqlite3.connect("pbs.db")
cursor.execute("select invoiceNumber from billingTable where sm LIKE '%Parth Swamy%' and billdate BETWEEN ('2001/01/01') and ('2030/01/01')")
index = cursor.fetchall()

billCount=0
for indexs in index:
    billCount = billCount + 1

cursor.execute("select total from billingTable where sm LIKE '%Parth Swamy%' and billdate BETWEEN ('2001/01/01') and ('2030/01/01')")
tamt=cursor.fetchall()
billTotal = 0
countTotal = 0
print(index,tamt)
for amt in tamt:
    print(amt)
    billTotal = billTotal + int(amt[countTotal])
c=[(0,0)]
for i in range (0,len(index)):
    print(i)
    d = index[i]
    e = tamt[i]
    b=(d[0],e[0])
    print(b)
    c.append(b)
print(c)
df = pd.DataFrame(c)
df.columns=['Invoice Number', 'Amount']
plt.bar(df['Invoice Number'],df['Amount'])
plt.title("TEST")
plt.xlim(240001,240010)
plt.xlabel("Invoice Number")
plt.ylabel("Amount")
plt.grid()
plt.show()