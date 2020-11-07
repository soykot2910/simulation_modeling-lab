
import random
import math

customer=int(input("Enter customer: "))
a_mean=float(input("Enter arival mean:"))
a_sd=float(input("Enter arival standard deviation:"))
s_mean=float(input("Enter service mean:"))
s_sd=float(input("Enter service standard deviation: "))

arrival_time=[]
service_time=[]

for i in range(customer):
    R1= round((random.uniform(-1, 1)),2)
    arrival_time.append(R1)
    R2=round((random.uniform(-1, 1)),2)
    arrival_time.append(R2)

iat=0
cat=0
se=0
wt=0
total_wating_time=0
total_time_elapsed=0
server_idle_time=0
print("AT   R1     IAT     CAT      SB    R2    ST     SE      WT     IT ")
for i in range(customer):
    arr=[]
    iat=a_mean+a_sd*arrival_time[i]
    cat=cat+iat
    sb=max(se,cat)
    st=s_mean+s_sd*service_time[i]
    if se-cat>0:
        wt=se-cat
    else:
        wt=0
    if cat-se>0:
        it=cat-se
    else:
        it=0
    se=sb+st
    total_time_elapsed +=st
    total_wating_time +=wt
    server_idle_time +=it
    print(i+1,"{:.2f}".format(arrival_time[i])," ","{:.2f}".format(iat)," ",
           "{:.2f}".format(cat)," ","{:.2f}".format(sb)," ","{:.2f}".format(service_time[i])," ",
           "{:.2f}".format(st)," ","{:.2f}".format(se)," ","{:.2f}".format(wt)," ","{:.2f}".format(it))


print("Total time elapsed:",total_time_elapsed)
print("Total customer waiting time:",total_wating_time)
print("Total server idl time: ",server_idle_time)

average_waiting_time=total_wating_time/customer

print(average_waiting_time)
