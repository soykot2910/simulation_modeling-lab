import random
import numpy
import math
from tabulate import tabulate

def chemical_reaction():
     # constant
     k1=float(input("First constant:"))
     k2=float(input("second constant:"))


     #time
     st=float(input("initial time:"))

     ch1=float(input("Enter first chemical amount: "))
     ch2=float(input("Enter second chemical amount: "))
     ch3=float(input("Enter third chemical amount: "))

     delt=float(input("time interval:"))
     ft=float(input("finished time:"))


     total=ch1+ch2
     data=[]

     for i in numpy.arange(st,ft+delt,delt):
          arr=[]
          arr.append(i)
          arr.append(ch1)
          arr.append(ch2)
          arr.append(ch3)
          data.append(arr)
          temp1=ch1
          temp2=ch2
          temp3=ch3
          ch1=ch1+(k2*temp3-k1*temp1*temp2)*delt
          ch2=ch2+(k2*temp3-k1*temp1*temp2)*delt
          ch3=total-(ch1+ch2)

     print(tabulate(data,headers=["Time","c1","c2","c3"]))

chemical_reaction();


