import numpy as np
data_type=[('name','S15'),('ID',int),('phone no.',int)]
employees_details = [('Tim',2,3145678),('Tom',1,335461),('Tdm',4,5345211),('Tem',3,2133211)]
employees = np.array(employees_details,dtype=data_type)
print("Original Array:")
print(employees)
print("Sort by phone no.")
print(np.sort(employees,order='phone no.'))