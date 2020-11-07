from tabulate import tabulate
import math
import random
data=[]
customer=int(input('Enter totla customer:'))
at=8
tst=6
ran_r1=[]#random for time between arrival
ran_r2=[]#random for service time

for i in range(customer):
    r1=math.floor(random.uniform(0, 1000))
    ran_r1.append(r1)
    r2=math.floor(random.uniform(0,100))
    ran_r2.append(r2)

# print(ran_r1)
# print(ran_r2)

s_t_p=[.10,.20,.30,.25,.10,.05]

#time between arrival
d_arrival={}
cp=0
for i in range(at):
    pro=1/at
    cp=cp+pro
    d_arrival[i]=round(cp,3)*1000

#print(d_arrival)

#service time
service_time={}
scp=0
for i in range(tst):
    scp=scp+s_t_p[i]
    service_time[i]=round(scp,2)*100

#print(service_time)

# iat and
iat=[]
st=[]
for i in range(customer):
    for j in range(len(d_arrival)):
        if d_arrival[j]>=ran_r1[i]:
            iat.append(j+1)
            break
    for j in range(len(service_time)):
        if service_time[j]>=ran_r2[i]:
            st.append(j+1)
            break
# print(st)
# print(iat)

se=0
cat=0
for i in range(customer):
    arr=[]
    cat=cat+iat[i]
    sb=max(se,cat)
    if se-cat>0:
        wt=se-cat
    else:
        wt=0
    if cat-se>0:
        it=cat-se
    else:
        it=0
    se=sb+st[i]
    ts=st[i]+sb
    arr.append(i+1)
    arr.append(iat[i])
    arr.append(cat)
    arr.append(st[i])
    arr.append(sb)
    arr.append(wt)
    arr.append(se)
    arr.append(ts)
    arr.append(it)
    data.append(arr)

print(tabulate(data,headers=["i","iat","cat","st","sb","wt","se","ts","it"]))
