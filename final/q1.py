import math

file = open('final/input.txt')
lines = file.readlines()
file.close()


timeInt=int(input("Time interval:"))
speed=float(input("Fighter speed:"))

xb = [int(i) for i in lines[1].split(' ')[1:]]
yb = [int(i) for i in lines[2].split(' ')[1:]]



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




