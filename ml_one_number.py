import random
import matplotlib.pyplot as plt
m=0
c=1
inp=0
ans=0
guess=0
Mvalues=[]
Xvalue=[]
end=0
randomNum=1
close=0
close_old=100000000

for i in range(10000):
    inp=random.randint(0,100)
    ans=c*inp
    guess=round(m)*inp
    Xvalue.append(i)
    Mvalues.append(m)
    if guess==ans:
        print(m)
        if end==10:
            break
        else:
            end=end+1
    else:
        close=abs(c-m)
        if close_old<close:
            randomNum=randomNum*-1
        close_old=abs(c-m)
        m=m+(randomNum*close)
        end=0
print(c)
print(m)
print(Xvalue[-1])

x = Xvalue
y = Mvalues

plt.plot(x, y)

plt.xlabel('x - axis')

plt.ylabel('y - axis')

plt.title('m value vs. time')

plt.show()
