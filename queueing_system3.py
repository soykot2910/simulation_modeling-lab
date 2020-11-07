
import random
import math
from tabulate import tabulate

file = open('final/input.txt')
lines = file.readlines()
file.close()

P_arrival_time=[float(i) for i in lines[0].split(' ')[1:]]
A_service_p = [float(i) for i in lines[1].split(' ')[1:]]
B_service_p = [float(i) for i in lines[2].split(' ')[1:]]

customer=int(input("Enter total customer:"))
at=int(input("Enter total time between call range time:"))
A_tst=int(input("Enter service start time for Abel:"))
B_tst=int(input("Enter service start time for Baker:"))



arrival_time=[]
random_value=[]

for i in range(customer):
    r1=math.floor(random.uniform(0, 100))

    arrival_time.append(r1)
    r2=math.floor(random.uniform(0, 100))
    random_value.append(r2)


#time between arrival

d_arrival={}
cp=0
for i in range(at):
    cp=cp+P_arrival_time[i]
    d_arrival[i]=round(cp,2)*100

print(d_arrival)

#service time
A_service_time={}
A_scp=0
for i in range(A_tst):
    A_scp=A_scp+A_service_p[i]
    A_service_time[i]=round(A_scp,2)*100

B_service_time={}
B_scp=0
for i in range(B_tst):
    B_scp=A_scp+B_service_p[i]
    B_service_time[i]=round(B_scp,2)*100



print(B_service_time)

iat=[]

for i in range(customer):
    for j in range(at):
        if d_arrival[j]<arrival_time[i]:
            iat.append(j+1)
            break

s_t_a=[]
s_t_b=[]

for i in range(customer):
    for j in range(A_tst):
        if A_service_time[j]<random_value[i]:
            s_t_a.append(j+1)
            break
    for j in range(B_tst):
        if B_service_time[j]<random_value[i]:
            b_t_a.append(j+1)
            break

data=[]

c_a_t=0
for i in range(customer):
    arr=[]
    arr.append(i)
    arr.append(arrival_time[i])
    arr.append(iat[i])
    c_a_t +=iat[i]
    arr.append(c_a_t)
    arr.append(random_value[i])
    arr.append(s_t_a[i])




print(tabulate(data,headers=["cus","Rn_A","IAT","CAT","Rn_s","SB_A","ST_A","SE_T","SB_B","ST_B","SE_B","WT","TS","IT"]))





