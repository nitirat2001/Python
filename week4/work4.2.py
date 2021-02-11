import os
x=5
dictionary={
    'actor':'{0:<17}{1:<17}'.format('n.','นักแสดงชาย'),
    'anywhere':'{0:<17}{1:<17}'.format('adv.','ที่ใดก็ตาม'),
    'boil':'{0:<17}{1:<17}'.format('v.','ต้ม,ทำให้เดือด'),
    'book':'{0:<17}{1:<17}'.format('n.','หนังสือ'),
    'dangerous':'{0:<17}{1:<17}'.format('adj.','ซึ่งเป็นอันตราย')
}
def menu():
    global choice
    print('-----------------พจนานุกรม-----------------\n1)เพิ่มคำศัพท์\n2)แสดงคำศัพท์\n3)ลบคำศัพท์\n4)ออกจากโปรแกรม')
    choice=int(input('Input choice '))

def add():
    word=input('พิมพ์คำศัพท์ที่ต้องการเพิ่ม: ')
    types=input('ประเภทของคำศัพท์: ')
    meaning=input('ความหมาย: ')
    dictionary[word]='{0:<17}{1:<17}'.format(types,meaning)
    print('Added!')

def show():
    print('-'*45)
    print('\t\tคำศัพท์ทั้งหมด',x,'คำ')
    print('-'*45)
    print('{0:<17}{1:<17}{2:<17}'.format('คำ','ประเภท','ความหมาย'))
    for C,L in dictionary.items():
        print('{0:<17}{1:<17}'.format(C,L))
def remove():
    delete=input('พิมพ์คำศัพท์ที่ต้องการลบ : ')
    d=input('ต้องการลบ'+delete+'ใช่หรือไม่y/n: ')
    if d== 'y':
        dictionary.pop(delete)
        print('removed')
    else:
        print('')
  
while(True):
    menu()
    if choice== 1:
        add()
        x=x+1
    elif choice== 2:
        show()
    elif choice== 3:
        remove()
        x=x-1
    else:
        Exit=input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n: ')
        if Exit== 'y':
            break
        else:
            continue