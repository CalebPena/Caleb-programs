import matplotlib.pyplot as plt
pi=0
n=1
pon=1
print('ctrl+c to stop')
while True:
    try:
        pi=pi+pon*(1/n) 
        n=n+2
        pon=pon*-1
    except:
        break
print(pi*4)
