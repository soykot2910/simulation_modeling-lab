#monte carlo for coin flipped game
import random
import math

pay_tk=1
diff=2
got_tk=8
h=[0,1,2,3,4]
t=[5,6,7,8,9]


n=int(input("Enter game number:"))

for i in range(n):
    print("================================= game no {0}=======================".format(i+1))
    print(" ")
    coin=""
    ch=0
    ct=0
    c_dif=0
    print("random number      coin          ch           ct          difference")
    while c_dif !=diff:

        rn= math.floor(random.uniform(0, 10))
        if rn<=4:
            coin="h"
            ch=ch+1
        else:
            coin="t"
            ct=ct+1
        c_dif=abs(ch-ct)
        print(rn,"                 ",coin,"           ",ch,"         ",ct,"                ",c_dif)




