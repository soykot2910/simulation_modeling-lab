import random
import math
from tabulate import tabulate


file = open('kolmogorov.txt')
lines = file.readlines()
file.close()

alphas=[float(i) for i in lines[0].split(' ')[1:]]
alpha_1 = [float(i) for i in lines[1].split(' ')[1:]]
alpha_2 = [float(i) for i in lines[2].split(' ')[1:]]

print(alphas,alpha_1,alpha_2)

n=int(input("Enter  total random number:"))

alpha=float(input("Enter alpha value:"))
random_num=[]
data=[]

for i in range(n):
    rn=round(random.uniform(0, 1),2)
    random_num.append(rn)


random_num.sort()

d_plus=0
d_minus=0
d_alph=0

for i in range(n):
    arr=[]
    arr.append(random_num[i])
    arr.append((i+1)/n)
    if (i+1)/n-random_num[i]>=0:
        arr.append((i+1)/n-random_num[i])
        if (i+1)/n-random_num[i]>d_plus:
            d_plus=(i+1)/n-random_num[i]

    if random_num[i]-((i)/n)>=0:
        arr.append(random_num[i]-((i)/n))
        if (random_num[i]-(i/n)):
            d_minus=(random_num[i]-(i/n))


    data.append(arr)

print(tabulate(data,headers=["Ri","i/n","(i/n)-ri","Ri-(i-1)/n"]))

d=max(d_plus,d_minus)

for i in range(2):
    if alpha==alphas[i]:
        d_alph=alpha_1[n-1]
    else:
        d_alph=alpha_2[n-1]

print("\n\n")
print("D+ value:",d_plus)
print("D- value:",d_minus)
print("D value:",d)
print("Critical value D alpha value:",d_alph)
if d<d_alph:
    print("Given random number are uniform")
else:
    print("Given random number are not uniform")

