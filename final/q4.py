
# mam ay code ta ami tabulate libary use korci.apnar pc te ata na install dey thakle error dibe
from tabulate import tabulate
import random
import math

data=[]

demand_num=[]
demand_pro=[]
total_demand=int(input('Enter total demand value:'))
for i in range(total_demand):
    dn=input("Enter demand value:")
    demand_num.append(dn)
    dp=float(input("Enter demand problality:"))
    demand_pro.append(dp)

lead_num=[]
lead_pro=[]

total_lead_time=int(input("Enter total lead time:"))
for i in range(total_lead_time):
    dn=input("Enter lead time value:")
    lead_num.append(dn)
    dp=float(input("Enter lead time problality:"))
    lead_pro.append(dp)

init_stock=int(input('Enter inital stock:'))
#outstanding_unit=int(input('Enter outstanding_unit:'))
outstandin_R1=int(input("Enter outstanding for reorder 1:"))
outstandin_R2=int(input("Enter outstanding for reorder 2:"))

rp1=int(input('Enter reorder point one level:'))
rp2=int(input('Enter reorder point two level:'))
sim=int(input('Enter total simulation:'))

demand_per_num=[]
demand=[]
lead_per_num=[]
lead_time=[]


for i in range(len(demand_pro)):
    dem_num=int(demand_pro[i]*sim)
    demand_per_num.append(dem_num)

for i in range(len(lead_pro)):
    le_num=lead_pro[i]*sim/2
    lead_per_num.append(le_num)


for i in range(len(demand_per_num)):
    for j in range(int(demand_per_num[i])):
        rand_r1= int(random.uniform(0, sim))
        demand.insert(rand_r1,demand_per_num[i])

for i in range(len(lead_per_num)):
    for j in range(int(lead_per_num[i])):
        raddn_r2=int(random.uniform(0,sim/2))
        lead_time.insert(raddn_r2,lead_per_num[i])

stk=[0]*sim
cstk=[0]*sim
ord1=[0]*sim
ddate1=[0]*sim
cdmd=[0]*sim
ord2=[0]*sim
ddate2=[0]*sim
short=[0]*sim
cshort=[0]*sim


stk[0]=init_stock
cstk[0]=stk[0]
ord1[0]=outstandin_R1
lp=0
ddate1[0]=1+lead_time[lp]
cdmd[0]=demand[0]
total_stock=0

for i in range(1,sim):
    arr=[]
    prev=i-1
    s=stk[prev]-demand[prev]
    if s>=0:
        stk[i]=s

    if ddate1[prev]==i+1:
        stk[i]=stk[i]+ord1[prev]

    if ddate2[prev]==i+1:
        stk[i]=stk[i]+ord2[prev]

    if not ddate1[prev] and rp2<stk[i]<=rp1:
        lp +=1
        ddate1[i]=i+1+lead_time[lp]
        ord1[i]=outstandin_R1
    else:
        ddate1[i]=ddate1[prev]
        if ddate1[prev]:
            ord1[i]=outstandin_R1
    if ddate1[i]==i+1:
        ddate1[i]=0
        ord1[i]=0

    if not ddate2[prev] and 0<stk[i]<=rp2:
        lp +=1
        ddate2[i]=i+1+lead_time[lp]
        ord2[i]=outstandin_R2
    else:
        ddate2[i]=ddate2[prev]
        if ddate2[prev]:
            ord2[i]=outstandin_R2
    if ddate2[i]==i+1:
        ddate2[i]=0
        ord2[i]=0
    s=stk[i]-demand[i]
    if stk[i]<demand[i]:
        short[i]=demand[i]-stk[i]
    else:
        short[i]=0
    cstk[i]=cstk[prev]+stk[i]
    cdmd[i]=cdmd[prev]+demand[i]
    cshort[i]=cshort[prev]+short[i]

for i in range(sim):
    arr=[]
    arr.append(i+1)
    arr.append(stk[i])
    arr.append(int(cstk[i]))
    arr.append(ord1[i])
    arr.append(ddate1[i])
    arr.append(ord2[i])
    arr.append(ddate2[i])
    arr.append(demand[i])
    arr.append(cdmd[i])
    arr.append(short[i])
    arr.append(cshort[i])


    data.append(arr)


print(tabulate(data,headers=["day","stk","cstk","ord1","ddate1","ord2","Ddate2","dmd","cmd","short","cshort"]))

average_stock=cstk[sim-1]/sim

print(average_stock)

service_level=((cdmd[sim-1]-cshort[sim-1])/cdmd[sim-1])*100

print(service_level)
