import random
import math
from tabulate import tabulate

file = open('chi-square.txt')
lines = file.readlines()
file.close()

random_num = [int(i) for i in lines[0].split(' ')[1:]]

n=int(input('Enter Number of class:'))
N=len(random_num)

Ei=int(N/n)

data=[]

count=[0]*n

for i in range(n):
    for j in range(N):
        if random_num[j]>i*Ei and random_num[j]<=Ei*(i+1):
            count[i] +=1

total=0
for i in range(n):
    total +=((count[i]-Ei)**2)/Ei
    arr=[]
    arr.append(str(i*Ei)+'<r<='+str(Ei*(i+1)))
    arr.append(count[i])
    arr.append(abs(count[i]-Ei))
    arr.append((count[i]-Ei)**2)
    arr.append(((count[i]-Ei)**2)/Ei)
    data.append(arr)
print(tabulate(data,headers=["Class","Oi","Oi-Ei","(Oi-Ei)^2","((Oi-Ei)^2)/Ei"]))

print("Chi-square:",total)








