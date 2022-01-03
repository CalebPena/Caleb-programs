import random
add={'num1':0, 'num2':0}
answer=0
mid1={'m1':0,'m2':0,'m3':0}
guess=0
ll=[]
close=0
closelist=[]
big5=[]

for x in range(100):
    lines={'l11':random.randint(0,200)/100,'l12':random.randint(0,200)/100,'l22':random.randint(0,200)/100,'l23':random.randint(0,200)/100}
    ll.append(lines)
add['num1']=random.randint(0,100)
add['num2']=random.randint(0,100)
answer=add['num1']+add['num2']
print(answer)
for i in range(100):
    mid1['m1']=add['num1']*ll[i]['l11']
    mid1['m2']=add['num1']*ll[i]['l12']+add['num2']*ll[i]['l22']
    mid1['m3']=add['num1']*ll[i]['l23']
    guess=int(mid1['m1']+mid1['m2']+mid1['m3'])
    print(guess)
    close=abs(answer-guess)
    closelist.append(close)
for k in closelist:
    e=0
    if len(big5)<5:
        big5.append(k)
    else:
        for f in big5:
            if k<f:
                if e==0:
                    big5[big5.index(f)]=k
                    e=1
                
                

print(closelist)
print(big5)
