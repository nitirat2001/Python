n=1
std=int(input("ใส่จำนวนนักเรียน(N):"))
stdlist=[0,0,0,0,0,0]
score_list=['90-100:','80-89:','70-79:','60-69:','50-59:','0-49:']
while n<=std:
    score=int(input("ใส่คะแนนนักเรียน(S):"))
    n+=1
    if score>=90 and score<=100:
        stdlist[0]+=1
    elif score>=80 and score<=89:
        stdlist[1]+=1
    elif score>=70 and score<=79:
        stdlist[2]+=1
    elif score>=60 and score<=69:
        stdlist[3]+=1
    elif score>=50 and score<=59:
        stdlist[4]+=1
    elif score>=0 and score<=49:
        stdlist[5]+=1
for n in range(0,6):
    print(score_list[n],'*'*stdlist[n])



