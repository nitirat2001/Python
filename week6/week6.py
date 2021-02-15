import os
import sqlite3



word_dictionary = {}
def menu():
    global choice
    print('*******ระบบข้อมูลนักเรียน*******\n'+'#'*25+'\n เพิ่มข้อมูลนักเรียนกด [a]\n แสดงข้อมูลนักเรียน [s]\n แก้ไขข้อมูลนักเรียน [e]\n ลบข้อมูลนักเรียน [d]\n ออกจากโปรแกรม [x]\n')
    choice = input('กรุณาเลือกรายการ : ')

def add():
    global Fname,Lname,Ename,Sex,Age,data1
    data1 = input('input name,lastname,email,sex,age (Must enter,) : ')
    data2 = data1.split(",")
    Fname = data2[0]
    Lname = data2[1]
    Ename = data2[2]
    Sex = data2[3]
    Age = data2[4]

def insertTousers (Fname,Lname,Ename,Sex,Age):
    try :
        conn = sqlite3.connect (r"D:\Nitirat_Python\week6.db")
        c = conn.cursor()
        sql = ''' INSERT INTO users (Name,Lastname,Email,Sex,Age) VALUES (?,?,?,?,?) '''
        data = (Fname,Lname,Ename,Sex,Age)
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn : 
            conn.close()

def show():
    conn = sqlite3.connect (r"D:\Nitirat_Python\week6.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    print("{0: <15}{1: <15}{2: <15}{3: <15}{4: <15}{5: <15}".format('ลำดับที่','ชื่อ','สกุล','อีเมลล์','เพศ','อายุ')+"-"*120)
    for i in rows:
        print("{0: <15}{1: <15}{2: <15}{3: <15}{4: <15}{5: <15}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    print('ทำการแสดงรายการเสร็จสิ้น\n')

def editinfo(Fname,Lname,Ename,Sex,Age,change):
    try :
        conn = sqlite3.connect(r"D:\Nitirat_Python\week6.db")
        c = conn.cursor()
        data = (Fname,Lname,Ename,Sex,Age,change)
        c.execute('''UPDATE users SET Name =?,Lastname =?,Email =?,Sex =?,Age =? WHERE NO = ?''',data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Failed to edit : ',e)
    finally : 
        if conn : 
            conn.close()

def deleted(delete):
    try:
        conn=sqlite3.connect(r"D:\Nitirat_Python\week6.db")
        c=conn.cursor()
        c.execute('''DELETE FROM users WHERE NO = ?''',delete)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('FAILED TO DELETE: ',e)
    finally:
        if conn:
            conn.close()

while True:
    menu()
    if choice == 'a':
        os.system('cls')
        add()
        insertTousers(Fname,Lname,Ename,Sex,Age)
    elif choice == 's':
        os.system('cls')
        show()
    elif choice == 'e':
        os.system('cls')
        change=input('กรอกตำแหน่ง (ตัวเลข) ที่ต้องการแก้ไขข้อมูล กรอก 0 หากไม่ต้องการแก้ไขข้อมูล : ')
        if change != '0':
            add()
            editinfo(Fname,Lname,Ename,Sex,Age,change)
    elif choice == 'd':
        os.system('cls')
        delete = input('กรอกตำแหน่ง (ตัวเลข) ที่ต้องการแก้ไขข้อมูล กรอก 0 หากไม่ต้องการแก้ไขข้อมูล : ')
        if delete != '0':
            deleted(delete)
    elif choice == 'x':
        os.system('cls')
        c=input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n:')
        if c.lower() == 'y':
            os.system('cls')
            break
        elif c.lower() == 'n':
            os.system('cls')


