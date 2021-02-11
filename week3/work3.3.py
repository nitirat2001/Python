print('ป้อนชื่ออาหารโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม')
mlist=[]
i=0
while i>=0:
    i=i+1
    print('ป้อนชื่ออาหารโปรดของคุณ:',i,end='')
    food=input('  คือ\t')
    mlist.append(food)
    if food=='exit':
        break
print('รายการอาหารของคุณคือ :',end=' ')
for x in range(1,i):
    print(x,'.',mlist[x-1],end=' ')



