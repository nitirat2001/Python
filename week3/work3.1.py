print('\tเลือกเมนูเพื่อทำรายการ')
print('##########################################')
print('กด 1 เลือกเหมาจ่าย')
print('กด 2 เลิอกจ่ายเพิ่ม')
choose=int(input('เลือกรายการที่คุณต้องการ:'))
if choose==1:
        buy=int(input('ใส่ระยะทางของคุณ:'))
        if buy<25:
            print('จ่าย 25 บาท')
        else:
            print('จ่าย 55 บาท')
if choose==2:
        buy=int(input('ใส่ระยะทางของคุณ:'))
        if buy<=25:
            print('จ่าย 25 บาท')
        else :
            print('จ่าย 55 บาท')
