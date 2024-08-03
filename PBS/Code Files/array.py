import sqlite3
con=sqlite3.connect(database=r"pbs.db")
cur = con.cursor()
cur.execute("SELECT * FROM salesman")

rows=cur.fetchall()
colnames = cur.description

array = [[0 for _ in range(len(colnames))] for _ in range(len(rows))]
print(rows)
print(len(colnames))
for i in range (0,len(rows)):
    A = rows[i]
    for j in range(0,len(colnames)):
        array[i][j] = A[j]
    
print(array)
'''
rows = (1, '4', '7', 'Male', '3', '5', '6', '8', 'Salesman', '10', '11')
ROWS = 2
COLS = 11
my_2d_array = [[0 for _ in range(COLS)] for _ in range(ROWS)]
for i in range(0,2):
    for j in range (0,11):
        my_2d_array[i][j] = rows[j]

        
my_2d_array


countCOLS = 0
countROWS = 0
for ROWS in rows:
    count = 11
    print(ROWS)
    for COLS in colnames:
        #print("["+str(countCOLS)+"]["+str(countROWS)+"]")
        a = 11-count
        if(a==7):
            array[countROWS][countCOLS] = "********"            
        else:
            print("A = "+str(a))
            array[countROWS][countCOLS] = ROWS[a]
        print("ARRAY = " +  str(array[countROWS][countCOLS]))
        countCOLS = countCOLS + 1
        count -= 1
    print(array)

    countROWS = countROWS + 1
    print("\n\n")




            cur.execute("SELECT * FROM salesman")
            rows=cur.fetchall()
            colnames = cur.description
            array = [[0 for _ in range(len(colnames))] for _ in range(len(rows))]

            countCOLS = 0
            countROWS = 0
            count = 0

            self.salesmanTable.delete(*self.salesmanTable.get_children())
            for ROWS in rows:

                for COLS in colnames:
                    if(countCOLS == 7):
                        array[countROWS][countCOLS] = "********"
                    else:
                        array[countROWS][countCOLS] = ROWS[count]
                    countCOLS = countCOLS + 1
                    count += 1

                countROWS = countROWS + 1

            for row in rows:
                self.salesmanTable.insert('',END,values=rows)
                #array[row][(11-countCOLS)])
                countCOLS = countCOLS + 1
'''
