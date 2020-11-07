#random number for pi value
import random
import math


INTERVAL=int(input("Enter Number of simulation:"))
diameter=int(input("Enter Number of diameter:"))

circle_points= 0
square_points= 0

for i in range(INTERVAL):

    # Randomly generated r1 and r2 values from a
    # uniform distribution
    # Rannge of r1 and r2 values is -1 to 1
    rand_r1= random.uniform(-3, 3)
    rand_r2= random.uniform(-3,3)
    #r2_squre=9-math.pow(rand_r2,2)
    calculate_r1= math.sqrt(9-math.pow(rand_r2,2))

    if rand_r1<=calculate_r1:
        circle_points+=1

    square_points+= 1

    print("r1=","{:.3f}".format(rand_r1),"r2=","{:.3f}".format(rand_r2),"calculate r1=","{:.3f}".format(calculate_r1),"M=",circle_points,"N=",square_points)
    pi = 4* circle_points/ square_points



print("Final Estimation of Pi=", pi)
