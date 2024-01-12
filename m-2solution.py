import math
import numpy as np
file1=open("C:/Users/RAJAMOHAN.J/Downloads/Workshop2024/Milestone2/Input/Testcase4.txt","r")
content=file1.readlines()
val=[]
for line in content:
    word=line.split(':')
    val.append(word[-1])
print(val)
dia=int(val[0].replace("\n", ""))
shift=val[2].replace("\n", "")
shift=(shift[1],shift[3])
size=val[1].split('x')
x1=int(size[0])
y1=int(size[1].replace("\n", ""))
reference=val[-1]
print(dia,x1,y1,reference,shift)
import numpy as np

def points_with_steps_and_range(x_step, y_step, x_range, y_range):
    points = []
    for x in range(x_range[0], x_range[1] + 1, x_step):
        for y in range(y_range[0], y_range[1] + 1, y_step):
            points.append((x, y))
    return points

x_step_size = x1
y_step_size = y1
x_value_range = (-dia//2, dia//2)
y_value_range = (-dia//2, dia//2)
result_points = points_with_steps_and_range(x_step_size, y_step_size, x_value_range, y_value_range)
cartesian_array = np.array(result_points) - np.array([(x_value_range[1] + x_value_range[0]) / 2, (y_value_range[1] + y_value_range[0]) / 2])
#all the lattice points of the grid
print(cartesian_array)
file3ans = open('C:/Users/RAJAMOHAN.J/Downloads/Workshop2024/Milestone2/output/m2-file4ans.txt',"w+")
file3ans.write("ALL POSSIBLE CORNERS OF DIE\n")
for i in cartesian_array:
    line = ','.join(str(x) for x in i)
    file3ans.write('('+line + ')'+'\n')
file3ans.close()
