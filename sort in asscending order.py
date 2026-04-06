import numpy as np
data_type=[('name','S15'),('class',int),('height',float)]
students_details = [('Tim',5,3.1),('Tom',6,3.1),('Tdm',7,5.1),('Tem',9,21.1)]
students = np.array(students_details,dtype=data_type)
print("Original Array:")
print(students)
print("Sort by height")
print(np.sort(students,order='height'))