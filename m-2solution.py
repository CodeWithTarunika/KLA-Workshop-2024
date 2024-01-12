import math
import numpy as np
import ast
import warnings
warnings.filterwarnings('ignore')

def points_with_steps_and_range(x_step, y_step, x_range, y_range):
    points = []
    for x in range(x_range[0], x_range[1] + 1, x_step):
        for y in range(y_range[0], y_range[1] + 1, y_step):
            points.append((x, y))
    return points

def isInside(circle_x, circle_y, rad, x, y):
    ans=[]
    if ((x - circle_x)**2 +(y - circle_y)**2 <= rad * rad):
        return 1
    else:
        return 0


file1=open("C:/Users/RAJAMOHAN.J/Downloads/Workshop2024/Milestone2/Input/Testcase4.txt","r")
content=file1.readlines()
val=[]
for line in content:
    word=line.split(':')
    val.append(word[-1])
dia=int(val[0].replace("\n", ""))
shift=val[2].replace("\n", "")
shift = tuple(ast.literal_eval(shift))
size=val[1].split('x')
x1=int(size[0])
y1=int(size[1].replace("\n", ""))
ref=val[-1]
ref = tuple(ast.literal_eval(ref))


x_step_size = x1
y_step_size = y1
x_value_range = (-dia//2, dia//2)
y_value_range = (-dia//2, dia//2)
result_points = points_with_steps_and_range(x_step_size, y_step_size, x_value_range, y_value_range)
cartesian_array = np.array(result_points) - np.array([(x_value_range[1] + x_value_range[0]) / 2, (y_value_range[1] + y_value_range[0]) / 2])

#all the lattice points of the grid
print(cartesian_array)
for i in cartesian_array:
    i[0]=i[0]+shift[0]
    i[1]=i[1]+shift[1]
print(cartesian_array)
file3ans = open('C:/Users/RAJAMOHAN.J/Downloads/Workshop2024/Milestone2/m2-output/m2-file4ans.txt',"w+")
file3ans.write("ALL POSSIBLE CORNERS OF DIE\n")
for i in cartesian_array:
    line = ','.join(str(x) for x in i)
    file3ans.write('('+line + ')'+'\n')
file3ans.close()

#all lattie points inside the grid
for i in cartesian_array:
    if not (isInside(shift[0],shift[1], dia/2, i[0], i[1])):
        ind = np.argwhere(cartesian_array==i)
        cartesian_array = np.delete(cartesian_array,ind)
print("The dies inside the wafer is:",cartesian_array)












    

