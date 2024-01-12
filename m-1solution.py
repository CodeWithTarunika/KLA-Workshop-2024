import math
import numpy as np

def extremes(c,dia,angle):
    x1=c[0]+(dia/2)*math.cos(math.radians(angle))
    x2=c[0]+(dia/2)*math.cos(math.radians(angle+180))
    y1=c[1]+(dia/2)*math.sin(math.radians(angle))
    y2=c[1]+(dia/2)*math.sin(math.radians(angle+180))
    return x1,x2,y1,y2
    
def equally_spaced_points_on_line(x1, y1, x2, y2, n):
    x = np.linspace(x1, x2, n)
    y = np.linspace(y1, y2, n)
    return [(x[i], y[i]) for i in range(n)]


file1=open("C:/Users/RAJAMOHAN.J/Downloads/Workshop2024/Milestone1/Input/Testcase3.txt","r")
content=file1.readlines()
val=[]
for line in content:
    word=line.split(':')
    val.append(int(word[-1].replace("\n", "")))
print(val)
c=(0,0)
dia=val[0]
num=val[1]
angle=val[-1]
x1,x2,y1,y2=extremes(c,dia,angle)
ans=equally_spaced_points_on_line(x1, y1, x2, y2, num)
print(ans)
file1ans = open('C:/Users/RAJAMOHAN.J/Downloads/Workshop2024/Milestone1/output/file3ans.txt',"w+")
for i in ans:
    line = ','.join(str(x) for x in i)
    file1ans.write('('+line + ')'+'\n')
file1ans.close()
