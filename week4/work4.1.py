import os
choice = 0
listdogs = [0,0,0,0,0,]
pick = 0
def menu():
    global choice
    print('\tโปรแกรมร้านขายสุนัข\n++++++++++++++++++++++++++++++++++++++++++++++++++++++\n','1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม')
    choice = input('กรุณาเลือกทำรายการ : ')
    clear_screen()

def showmenu(): 
    print('\tรายการสุนัขและราคา')
    print('\t1.บลูด็อก 30k บาท\n','\t2.พูเดิล 20k บาท\n','\t3.ไซบีเรียนฮัสกี้ 65k บาท\n','\t4.โกลเดน 44k บาท\n','\t5.ชิบะ 100k บาท')

def pickmenu():
    global pick
    print('\tรายการสุนัข\n 1.บลูด็อก\n 2.พูเดิล\n 3.ไซบีเรียนฮัสกี้\n 4.โกลเดน\n 5.ชิบะ')
    pick = int(input('เลือกหยิบสินค้าหมายเลข :'))
    if pick == 1:
        listdogs[0] += 1
    elif pick == 2:
        listdogs[1] += 1
    elif pick == 3:
        listdogs[2] += 1
    elif pick == 4:
        listdogs[3] += 1
    elif pick == 5:
        listdogs[4] += 1
    clear_screen()

def show_pick():
    list_score = ['บลูด็อก','พูลเดิล','ไซบีเรียนฮัสกี้','โกลเดน','ชิบะ']
    list_price = [30000,20000,65000,44000,100000]
    print('{0:-<13}{1:-<13}{2:-<13}{3}'.format('สินค้า','ราคา','จำนวน','ราคารวม'))
    for i in range(0,5):
        print('{0:-<13}{1:-<13}{2:-<13}{3}'.format(list_score[i],list_price[i],listdogs[i],listdogs[i]*list_price[i]))

def deleteurpick():
    print('\t\nรายการสินค้า\n 1.บลูด็อก\n 2.พูลเดิล\n 3.ไซบีเรียนฮัสกี้\n 4.โกลเดน\n 5.ชิบะ')
    depick = int(input('เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก'))
    if depick == 1:
        listdogs[0] -= 1
    elif depick == 2:
        listdogs[1] -= 1
    elif depick == 3:
        listdogs[2] -= 1
    elif depick == 4:
        listdogs[3] -= 1
    elif depick == 5:
        listdogs[4] -= 1

def clear_screen():
    clearscreen = os.system('cls')

while True:
    menu()
    if choice == '1':
        clear_screen()
        showmenu()
    elif choice == '2':
        clear_screen()
        pickmenu()
    elif choice == '3':
        clear_screen()
        show_pick()
    elif choice == '4':
        deleteurpick()
        clear_screen()
    elif choice == '5':
        c = input('ต้องการปิดโปรแกรมต่อหรือไม่ n/y: ')
        if c.lower() == 'n':
            clear_screen()
        elif c.lower() == 'y':
            clear_screen()
            print('THX BRO')
            break