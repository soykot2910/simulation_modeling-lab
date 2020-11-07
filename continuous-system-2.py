#continuous system for pursuit problem
import math

# first_file = open("file.txt", "r")
# all_data=first_file.read()
# first_file.close()

timeInt=int(input("Time interval:"))
speed=float(input("Fighter speed:"))

xb=[]
yb=[]

# bomber position
print("Enter bommer position xb & yb:")
for i in range(0,10):
    bx=float(input("Enter xb:"))
    xb.append(bx)
    by=float(input("Enter yb:"))
    yb.append(by)

#fighter initial position
print("Enter fighter initial position:")
xf=float(input("Enter xf:"))
yf=float(input("Enter yf:"))

d=float(input("Enter distance:"))

print("time --xb  -- yb  --  xf   --   yf  --   dist   --   sinA   -- cosB")
for i in range(0,10,timeInt):
    dist=math.sqrt((yb[i]-yf)**2+(xb[i]-xf)**2)
    if dist>d:
        sinA=(yb[i] - yf)/dist
        cosB=(xb[i]-xf)/dist
        print(i,"  ",xb[i],"  ",yb[i],"  ","{:.3f}".format(xf),"  ","{:.3f}".format(yf),"  ","{:.3f}".format(dist),"  ","{:.3f}".format(sinA),"  ","{:.3f}".format(cosB))
        xf=xf+(speed*cosB)
        yf=yf+(speed*sinA)
    else:
        break



