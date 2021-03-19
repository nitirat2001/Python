import sqlite3 as It
from os import name,system
import datetime
import random 
import string
import random
import uuid

# conn = It.connect (r"D:\Phisit_Python\Project\Projectfinish.db")
# c = conn.cursor()
# c.execute ('''CREATE TABLE nomalusers(id integer PRIMARY KEY AUTOINCREMENT,
#     VIP varchar(10) NOT NULL,
#     username varchar(50) NOT NULL,
#     password varchar(50) NOT NULL,
#     timer varchar(50) NOT NULL,
#     Phonenumber varchar(10) NOT NULL,
#     Yourtime varchar(10) NOT NULL,
#     key varchar(50) NOT NULL,
#     price varchar(50) NOT NULL)''')
# conn.commit()
# conn.close()

def menu_interface():
    global choice
    print('='*50)
    print('****ระบบจองเวลาร้าน ต.เต่าแฮปปี้เน็ตยินดีให้บริการ****')
    print('='*50)
    print('กด [1] สมัครเข้าใช้งาน\nกด [2] ล็อคอินผู้ใช้ VIP\nกด [3] ดูโปรโมชั่นต่างๆ\nกด [4] โชว์ข้อมูลลูกค้า\nกด [5] ลบข้อมูลลูกค้า\nออกจากโปรแกรม [x]\n')
    choice = input('กรุณาเลือกรายการ : ')

def menu():
    pick = input('กด [1] สมัคร VIP \n'+'กด [2] จองแบบธรรมดา  \nกด [m] กลับสู่เมนูหลัก \nกรุณาเลือกรายการ : ')
    if pick == '1' :
        while True:
            global Timer,username,password,phonenumber
            clear()
            print('โปรดกรอก USER AND PASS 6-10 ตัว')
            print('กรอกเฉพาะตัวเลขหรือ กรุณากรอกใหม่')
            username = input('กรุณากรอก Username : ')
            password = input('กรุณากรอก Password : ')
            try:
                phonenumber = int(input('phonenumber :'))
            except:
                print('กรอกแต่เลข')
                continue
            t = datetime.datetime.now()
            Timer = str(t)
            if len(username)< 6 :
                clear()
                print('โปรดใส่ชื่อ 6-10 ตัวอักษร')
                    
            elif len(username)>10:
                clear()
                print('โปรดใส่ชื่อ 6-10 ตัวอักษร')
            
            elif len(password)< 6 :
                clear()
                print('โปรดใส่รหัส 6-10 ตัวอักษร')
                        
            elif len(password)>10:
                clear()
                print('โปรดใส่รหัส 6-10 ตัวอักษร')
            
            else:
                choose_hours()
                break
 
    elif pick == '2' :
        global Timer1,username1,password1,phonenumber1
        t = datetime.datetime.now()
        Timer1 = str(t)
        choose_hours1()
    elif pick == 'm':
        clear()
        menu_interface()
    else:
        clear()
        print("กรุณาเลือก 1,2 หรือ m \n")
        menu()

def login_uservip():
        global Timer2,username,password,phonenumber
        t = datetime.datetime.now()
        Timer2 = str(t)
        username = input("กรุณาใส่ชื่อไอดีของท่าน :")
        password = input("กรุณาใส่รหัสของท่าน :")
        with It.connect(r"D:\Nitirat_Python\Project\Project4.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM nomalusers WHERE username = ? AND password = ?")
        cursor.execute(find_user,[ (username),(password) ])
        results = cursor.fetchall()

        if results:
            for row in results:
                print('ยินดีต้อบรับกลับ')
                choose_hours3()
                break
        else:
            clear()
            print('ไม่พบบัญชีผู้ใช้')

def insertvip(x,y):
        try :
            conn = It.connect (r"D:\Nitirat_Python\Project\Project4.db")
            c = conn.cursor()
            sql = ''' INSERT INTO nomalusers(VIP,username,password,timer,Phonenumber,Yourtime,key,price) VALUES (?,?,?,?,?,?,?,?) '''
            data = ('VIP',username,password,Timer,phonenumber,x,y,price)
            c.execute(sql,data)
            conn.commit()
            c.close()
        except It.Error as e:
            print('Failed to insert : ',e)
        finally :
            if conn : 
                conn.close()

def insertloginvip(x,y):
        try :
            conn = It.connect (r"D:\Nitirat_Python\Project\Project4.db")
            c = conn.cursor()
            sql = ''' INSERT INTO nomalusers(VIP,username,password,timer,Phonenumber,Yourtime,key,price) VALUES (?,?,?,?,?,?,?,?) '''
            data = ('VIP',username,password,Timer2,phonenumber,x,y,price3)
            c.execute(sql,data)
            conn.commit()
            c.close()
        except It.Error as e:
            print('Failed to insert : ',e)
        finally :
            if conn : 
                conn.close()
 
def insertnomal(x,y):
        try :
            conn = It.connect (r"D:\Nitirat_Python\Project\Project4.db")
            c = conn.cursor()
            sql = ''' INSERT INTO nomalusers(VIP,username,password,timer,Phonenumber,Yourtime,key,price) VALUES (?,?,?,?,?,?,?,?) '''
            data = ('-','-','-',Timer1,'-',x,y,price1)
            c.execute(sql,data)
            conn.commit()
            c.close()
        except It.Error as e:
            print('Failed to insert : ',e)
        finally :
            if conn : 
                conn.close()

def choose_hours3():
    global price3
    hours3 = float(input('กรอกจำนวนเวลาที่ต้องการเล่น หน่วยซม. : '))
    sum03 = (hours3*15)-((hours3*15)*(10/100))
    price3 = float(sum03)
    print('ราคาที่ต้องจ่าย',price3 , 'บาท')
    string_length=10
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) 
    random = random.upper() 
    random = random.replace("-","") 
    print ('คีย์ของคุณคือ ',random[0:string_length]) 
    insertloginvip(hours3,random[0:string_length])              
        
def choose_hours():
    global price
    hours = float(input('กรอกจำนวนเวลาที่ต้องการเล่น หน่วยซม. : '))
    sum01 =((hours*15)-(hours*15)*10/100)+100
    price = float(sum01)
    print('ราคาที่ต้องจ่าย',price , 'บาท')
    string_length=10
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) 
    random = random.upper() 
    random = random.replace("-","") 
    print ('คีย์ของคุณคือ ',random[0:string_length]) 
    insertvip(hours,random[0:string_length])
    
def choose_hours1():
    global price1
    hours1 = float(input('กรอกจำนวนเวลาที่ต้องการเล่น หน่วย ซม. : '))
    sum02 = hours1*15
    price1 = float(sum02)
    print('ราคาที่ต้องจ่าย',price1, 'บาท')
    string_length=10
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) 
    random = random.upper() 
    random = random.replace("-","") 
    print ('คีย์ของคุณคือ ',random[0:string_length]) 
    insertnomal(hours1,random[0:string_length])
    
def earnmoney():
    sum_l = 0
    conn = It.connect(r"D:\Nitirat_Python\Project\Project4.db")
    c = conn.cursor()
    c.execute('SELECT * From nomalusers')
    hee = c.fetchall()
    for x in hee:
        sum_l = float(x[8])+sum_l
    print('-'*95+'ยอดรวม','   ',sum_l,'บาท') 
    
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
def show_promotion():
    print("*****โปรโมชั่นร้านตอนนี้*****")
    print(" 1 ชั่วโมง 15 บาท\n 2 ชั่วโมง 30 บาท\n 3 ชั่วโมง 45 บาท\n 4 ชั่วโมง 60 บาท\n 5 ชั่วโมง 75 บาท ")
    print('สมัคร VIP เพียงเดือนละ 100')
    print("หากเป็นลูกค้า VIP มีส่วนลด 10%")

def show_user():
    print('\n\t\t\t*** แสดงข้อมูลลูกค้า ***\n')
    print('{0:<3}{1:<10}{2:<10}{3:<13}{4:<30}{5:<13}{6:<15}{7:<12}{8:<5}\n'.format('No','User','username','password','timer','Phonnumber','Yourtime','key','price'))
    with It.connect (r"D:\Nitirat_Python\Project\Project4.db") as con:
        con.row_factory = It.Row
        show1="SELECT * FROM nomalusers "
        for row in con.execute(show1):
            print('{0:<3}{1:<10}{2:<10}{3:<13}{4:<30}{5:<15}{6:<10}{7:<15}{8:<5}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
    earnmoney()
    
def delete():
    d = input('ลำดับที่ต้องการลบ : ')
    d = (d,)
    conn = It.connect(r"D:\Nitirat_Python\Project\Project4.db")
    c = conn.cursor()
    c.execute('''DELETE FROM nomalusers WHERE id = ?''',d)
    conn.commit()
    conn.close()
    print('แก้ไขข้อมูลเรียบร้อยแล้ว ')

while True:
    menu_interface()
    if choice == '1':
        clear()
        menu()
    elif choice == '2':
        clear()
        login_uservip()
    elif choice == '3':
        clear()
        show_promotion()
    elif choice == '4':
        clear()
        show_user()
    elif choice == '5':
        clear()
        delete()
    elif choice == 'x':
        clear()
        break
    else:
        clear()
        print("กรุณาเลือก 1,2,3,4,5 หรือ x \n")
