import sqlite3 
import os
import datetime
import random 
import string
import random
import uuid

conn = sqlite3.connect (r"D:\Nitirat_Python\Project\Project4.db")
c = conn.cursor()

def menu_interface():
    global choice
    print('='*50)
    print('***ระบบจองเวลาร้าน ต.เต่าแฮปปี้เน็ตยินดีให้บริการ***')
    print('='*50)
    print("กด [1] สมัครเข้าใช้งาน\nกด [2] จองเวลา\nกด [3] ดูโปรโมชั่นต่างๆ\nกด [4] โชว์ข้อมูลลูกค้าที่กำลังใช้งาน")
    print("กด [5] ลบข้อมูลลูกค้าที่กำลังใช้งาน\nกด [6] โชว์ข้อมูลบัญชีVIP\nกด [7] เพื่อแก้ไขบัญชีVIP\nกด [8] ลบข้อมูลบัญชีVIP\nออกจากโปรแกรม [x]")
    choice = input('กรุณาเลือกรายการ : ')

def Menu_Register():
    pick = input('กด [1] สมัคร VIP \nกด [m] กลับสู่เมนูหลัก \nกรุณาเลือกรายการ : ')
    c.execute("SELECT UserID FROM UsersData")
    all_user = c.fetchall()
    users_list = []
    os.system('cls')
    for i in range(len(all_user)):
        users_list.append(all_user[i][0])
    if pick == '1' :
        while True:
            global Timer2,username,password,phonenumber
            t = datetime.datetime.now()
            Timer2 = str(t)
            print('โปรดกรอก USER AND PASS 6-10 ตัว')
            print('และกรอกเบอร์เฉพาะตัวเลขเท่านั้น')
            username = input('กรุณากรอก Username : ')
            password = input('กรุณากรอก Password : ')
            phonenumber = input('phonenumber :')
            
            try:
                int(phonenumber)
                print('ชำระค่าสมัคร VIP 100 บาท เรียบร้อย!!!')
            except:
                os.system('cls')
                print('กรอกเบอร์เฉพาะตัวเลข!!!')
                continue
            if len(username)< 6 :
                os.system('cls')
                print('โปรดใส่ชื่อ 6-10 ตัวอักษร!!!')
            elif len(username)>10:
                os.system('cls')
                print('โปรดใส่ชื่อ 6-10 ตัวอักษร!!!')
            elif len(password)< 6 :
                os.system('cls')
                print('โปรดใส่รหัส 6-10 ตัวอักษร!!!')  
            elif len(password)>10:
                os.system('cls')
                print('โปรดใส่รหัส 6-10 ตัวอักษร!!!')
            elif username in users_list:
                os.system('cls')
                print('มีบัญชีผู้ใช้งานแล้ว')
            else:
                insertvip()
                break
    elif pick == 'm':
        os.system('cls')
    else:
        os.system('cls')
        print("กรุณาเลือก 1 หรือ m \n")
        menu()

def login_uservip():
    global Timer,username,pay,status
    t = datetime.datetime.now()
    Timer = str(t)
    while True:
        pick = input('กด [1] ลูกค้า VIP \n'+'กด [2] จองแบบธรรมดา  \nกด [m] กลับสู่เมนูหลัก \nกรุณาเลือกรายการ : ')
        if pick == '1':
            os.system('cls')
            username = input("กรุณาใส่ชื่อไอดีของท่าน หรือ พิมพ์ exit เพื่อออก :")
            if username == 'exit' :
                os.system('cls')
                break
            password = input("กรุณาใส่รหัสของท่าน :")
            c.execute('''SELECT UserID FROM UsersData''')
            UserID = c.fetchall()
            c.execute('''SELECT UserPass FROM UsersData''')
            UserPass = c.fetchall()
            login = {}
            for i in range(len(UserID)) :
                login[UserID[i][0]] = UserPass[i][0]
            if username in login and login[username] == password :
                os.system('cls')
                print('ยินดีต้อนรับกลับ')
                pay = 1
                status = 'VIP'
                choose_hours()
                break
            elif username in login and login[username] != password :
                os.system('cls')
                print('รหัสผ่านไม่ถูกต้อง')
            elif not username in login :
                os.system('cls')
                print('ไม่พบบัญชีผู้ใช้')
        elif pick == '2' :
            pay = 0
            status= 'Guest'
            username, = ('Guest',)
            choose_hours()
            break
        elif pick == 'm' :
            os.system('cls')
            break
        else:
            os.system('cls')
            print("กรุณาเลือก 1,2 หรือ m \n")

def insertvip():
    try :
        sql = ''' INSERT INTO UsersData (UserID,UserPass,Timer,PhoneNumber,Status,Apply) VALUES (?,?,?,?,?,?) '''
        data = (username,password,Timer2,phonenumber,'VIP','100')
        c.execute(sql,data)
        conn.commit()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)

def insertloginvip(x,y):
    try :
        sql = ''' INSERT INTO UsersLogin (UserID,Timer,Yourtime,Key,Price,Status) VALUES (?,?,?,?,?,?) '''
        data = (username,Timer,x,y,price,status)
        c.execute(sql,data)
        conn.commit()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
 
def choose_hours():
    global price
    hours = float(input('กรอกจำนวนเวลาที่ต้องการเล่น หน่วยชม. : '))
    try :
        float(hours)
    except :
        os.system('cls')
        print('กรุณากรอกเฉพาะตัวเลข')
        choose_hours()
    if float(hours) < 10 :
        if pay == 1 :
            sum0 = (float(hours)*15)*0.9
        else:
            sum0 = float(hours)*15
    else:
        sum0 = (float(hours)*15)*0.9
    price = float(sum0)
    print('ราคาที่ต้องจ่าย',price , 'บาท')
    string_length=10
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) 
    random = random.upper() 
    random = random.replace("-","") 
    print ('คีย์ของคุณคือ ',random[0:string_length]) 
    insertloginvip(hours,random[0:string_length])              
        
def show_promotion():
    print("****โปรโมชั่นร้านตอนนี้****")
    print(" 1 ชั่วโมง 15 บาท\n 2 ชั่วโมง 30 บาท\n 3 ชั่วโมง 45 บาท\n 4 ชั่วโมง 60 บาท\n 5 ชั่วโมง 75 บาท ")
    print('สมัคร VIP เพียงเดือนละ 100')
    print("หากเป็นลูกค้า VIP มีส่วนลด 10%")
    print('หากซื้อเวลา 10 ชม.ขึ้นไป ลด 10% หมายเหตุ:สมาชิกVIP จะไม่ได้ลดเพิ่มเป็น20%\n***ขอบคุณที่ใช้บริการครับ^^***')

def show_customer(test) :
    print('{0:<5}{1:<15}{2:<30}{3:<10}{4:<15}{5:<10}{6:<10}\n'.format('No','UserID','Timer','YourTime','Key','Price','Status'))
    c.execute("SELECT ID,UserID,Timer,YourTime,Key,Price,Status FROM UsersLogin")
    all_data = c.fetchall()
    for i in range(len(all_data)):
        print('{0:<5}{1:<15}{2:<30}{3:<10}{4:<15}{5:<10}{6:<10}'.format(all_data[i][0],all_data[i][1],all_data[i][2],all_data[i][3],all_data[i][4],all_data[i][5],all_data[i][6]))
    if test == 1:
        c.execute("SELECT Price FROM UsersLogin")
        all_price = c.fetchall()
        sum_price = 0
        for i in range(len(all_price)):
            sum_price += float(all_price[i][0])
        print(' '*74,'รวม ',sum_price,' บาท')

def del_customer() :
    show_customer(0)
    d = input('ลำดับที่ต้องการลบ หรือ กด 0 เพื่อลบทั้งหมด หรือ กด m เพื่อกลับสู่เมนูหลัก: ')
    if d == '0' :
        c.execute('''DELETE FROM UsersLogin''')
    elif d == 'm':
        os.system('cls')
        menu_interface()
    else :
        c.execute('''DELETE FROM UsersLogin WHERE ID = ?''',(d,))
    conn.commit()
    os.system('cls')
    print('แก้ไขข้อมูลเรียบร้อยแล้ว ')

def show_user(test):
    print('{0:<5}{1:<15}{2:<15}{3:<30}{4:<15}{5:<10}{6:<10}\n'.format('No','UserID','Password','Timer','PhoneNumber','Status','Apply'))
    c.execute("SELECT ID,UserID,UserPass,Timer,PhoneNumber,Status,Apply FROM UsersData")
    all_data = c.fetchall()
    for i in range(len(all_data)):
        print('{0:<5}{1:<15}{2:<15}{3:<30}{4:<15}{5:<10}{6:<10}'.format(all_data[i][0],all_data[i][1],all_data[i][2],all_data[i][3],all_data[i][4],all_data[i][5],all_data[i][6]))
    if test == 1:
        c.execute("SELECT Apply FROM UsersData")
        all_price = c.fetchall()
        sum_price = 0
        for i in range(len(all_price)):
            sum_price += float(all_price[i][0])
        print(' '*89,'รวม ',sum_price,' บาท')

def del_user():
    show_user(0)
    d = input('ลำดับที่ต้องการลบ หรือ กด 0 เพื่อลบทั้งหมด หรือ กด m เพื่อกลับสู่เมนูหลัก: ')
    if d == '0' :
        c.execute('''DELETE FROM UsersData''')
    elif d == 'm':
        os.system('cls')
        menu_interface()
    else :
        c.execute('''DELETE FROM UsersData WHERE ID = ?''',(d,))
    conn.commit()
    print('แก้ไขข้อมูลเรียบร้อยแล้ว ')

def modify_user() :
    c.execute('SELECT ID FROM UsersData')
    userID = c.fetchall()
    all_ID = []
    for i in range(len(userID)):
        all_ID.append(str(userID[i][0]))
    while True:
        err = 0
        show_user(0)
        choose = input('เลือกลำดับที่ต้องการแก้ไข กด 0 เพื่อออก : ')
        try :
            int(choose)
        except:
            err = 1
        if choose == '0':
            os.system('cls')
            break
        elif err == 1:
            os.system('cls')
            print('กรุณากรอกเฉพาะตัวเลข') 
        elif not choose in all_ID:
            os.system('cls')
            print('ไม่มีลำดับที่เลือก')
        elif err == 0 and choose in all_ID :
            update = input('กด [1] เพื่อแก้ไขรหัสผ่าน\nกด [2] เพื่อแก้ไขหมายเลขโทรศัพท์\nพิมพ์ m เพื่อออก\nกรุณาเลือกบริการที่ต้องการ (สามารถคีย์พร้อมกันได้ เงื่อนไข คั่นด้วย : ) : ')
            text = ['','','']
            split = update.split(":")
            for  i in range(len(split)):
                text[i] = split[i]
            if text[0] == '1' and text[1] == '2' and text[2] == 'm':
                os.system('cls')
                print('กรอก m พร้อม 1,2 ไม่ได้')
            elif text[0] == '1' and text[1] == '2' and text[2] == '':
                password = input('รหัสผ่านใหม่ : ')
                phonenumber = input('หมายเลขโทรศัพท์ใหม่ : ')
                c.execute('UPDATE UsersData SET UserPass = ?, PhoneNumber = ? WHERE ID = ? ',(password,phonenumber,choose,))
                conn.commit()
                os.system('cls')
                print('เปลี่ยนรหัสผ่านและเบอร์เรียบร้อยแล้วครับ!!!')
                break
            elif text[0] == '1' and text[1] == '' and text[2] == '':
                password = input('รหัสผ่านใหม่ : ')
                c.execute('UPDATE UsersData SET UserPass = ? WHERE ID = ? ',(password,choose,))
                conn.commit()
                os.system('cls')
                print('เปลี่ยนรหัสผ่านเรียบร้อยแล้วครับ!!!')
                break
            elif text[0] == '2' and text[1] == '' and text[2] == '' :
                phonenumber = input('หมายเลขโทรศัพท์ใหม่ : ')
                c.execute('UPDATE UsersData SET PhoneNumber = ? WHERE ID = ? ',(phonenumber,choose,))
                conn.commit()
                os.system('cls')
                print('เปลี่ยนเบอร์โทรศัพท์ผ่านเรียบร้อยแล้วครับ!!!')
                break
            elif text[0] =='m' and text[1] == '' and text[2] == '' :
                os.system('cls')
                break
            else:
                os.system('cls')
                print('กรุณากรอกแค่ 1,2 หรือ m')

while True:
    menu_interface()
    if choice == '1':
        os.system('cls')
        Menu_Register()
    elif choice == '2':
        os.system('cls')
        login_uservip()
    elif choice == '3':
        os.system('cls')
        show_promotion()
    elif choice == '4':
        os.system('cls')
        print('\n\t\t\t*** แสดงข้อมูลลูกค้าที่กำลังใช้งาน ***\n')
        show_customer(1)
    elif choice == '5':
        os.system('cls')
        del_customer()
    elif choice == '6':
        os.system('cls')
        print('\n\t\t\t*** แสดงข้อมูลลูกค้าVIP ***\n')
        show_user(1)
    elif choice == '7':
        os.system('cls')
        modify_user()
    elif choice == '8':
        os.system('cls')
        del_user()
    elif choice == 'x':
        os.system('cls')
        break
    else:
        os.system('cls')
        print("กรุณาเลือก 1,2,3,4,5,6,7,8 หรือ x \n")
