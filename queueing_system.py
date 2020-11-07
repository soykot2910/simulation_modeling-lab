from tabulate import tabulate

customer=15
a_mean=10
a_sd=1.5
s_mean=9.5
s_sd=1.0

arrival_time=[-0.46, -1.15, 0.15, 0.81, 0.74, -0.39, 0.45, 2.44, 0.59, -0.06, 0.09, 0.56, 0.65, 3.10, -0.44]
service_time=[0.59, -0.67, 0.41, 0.51, 1.53, -0.37, -0.27, -0.15, -0.02, -1.60, -0.19, 0.16, -0.07, 0.24, -1.76]


iat=0
cat=0
se=0
wt=0
data=[]
#print("i   r    IAT    CAT     SB  r    ST    SE     WT     IT ")
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
    #arr.append((i+1,arrival_time[i],iat,cat,sb,service_time[i],st,se,wt,it))
    arr.append(i+1)
    arr.append(arrival_time[i])
    arr.append(iat)
    arr.append(cat)
    arr.append(sb)
    arr.append(service_time[i])
    arr.append(st)
    arr.append(se)
    arr.append(wt)
    arr.append(it)
    data.append(arr)
    # print(i+1,"{:.2f}".format(arrival_time[i]),"=","{:.2f}".format(iat),"=",
    #        "{:.2f}".format(cat),"=","{:.2f}".format(sb),"=","{:.2f}".format(service_time[i]),"=",
    #        "{:.2f}".format(st),"=","{:.2f}".format(se),"=","{:.2f}".format(wt),"=","{:.2f}".format(it))

print(tabulate(data,headers=["i","r","iat","cat","sb","R","st","se","wt","it"]))
