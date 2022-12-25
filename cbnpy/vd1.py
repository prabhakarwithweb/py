#numpy is a extremely popular python module. it is heavily used in scienticfic coputing
import numpy as np
import time
import sys
#numpy's mostuseful feature is n dimensional array ndarray
#it is look like list
#three main enifit of numpy:
# 1.less memory 2. Fast 3. Convinient
l=range(1000)
#print(l)
print(sys.getsizeof(5)*len(l))
array = np.arange(1000)
#print(array)
print(array.size*array.itemsize)

# Showing Fast
size=1000000
l1= range(size)
l2= range(size)
a1=np.arange(size)
a2=np.arange(size)
#python list
start=time.time()
result=[(x+y) for x,y in zip(l1,l2)]
print("python list took : " , (time.time()-start)*1000)
#numpy array
start=time.time()
result= a1+a2
print("numpy took: ", (time.time()-start)*1000)

# adding is simple
a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(a1+a2)
print(a2-a1)
print(a1*a2)
print(a1/a2)

 

