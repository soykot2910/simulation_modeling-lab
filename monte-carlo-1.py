#monte carlo for drunkard moves
from tabulate import tabulate
import random
import math

d=int(input('Enter total direction:'))

all_dir=[]
pro=[]
for i in range(d):
    d_name=input('Enter direction name:')
    p=int(input('Enter probability:'))
    all_dir.append(d_name)
    pro.append(p/100)

data1=[]

temp=0

f=[0,1,2,3,4]
l=[5,6,7]
r=[8,9]

print("Enter starting position: ")
x=int(input())
y=int(input())
d=""

n=int(input("Enter steps number:"))

for i in range(0,n):
    arr=[]
    rn= math.floor(random.uniform(0, 10))
    if rn<=4:
        d="f"
        y=y+1
    elif rn<=7:
        d="l"
        x=x-1
    else:
        d="r"
        x=x+1
    arr.append(i+1)
    arr.append(rn)
    arr.append(d)
    arr.append(x)
    arr.append(y)

    data2.append(arr)

print(tabulate(data2,headers=["step","Rn","Dir","x","y"]))

