import numpy as np
import time,sys
size=1000
l1=range(size)
l2=range(size)

a1=np.arange(size)
a2=np.arange(size)

start =time.time()
result=[(x,y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)
start =time.time()
result=a1+a2

print((time.time()-start)*1000)

a=np.array([(1,2,3,4),(4,5,6)])
print(a.shape)