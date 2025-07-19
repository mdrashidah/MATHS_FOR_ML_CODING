import numpy as np
v=np.array([1,2,3])
w = np.array([2,1,-1])
print(v+w)
print(v-w)
print(v*w)
print(v,w)
print(3*v)
print(np.linalg.norm(v))  #this will give the value of the norm of the vector v
s=np.dot(v,w)
print(s)

