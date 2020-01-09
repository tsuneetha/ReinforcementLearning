f=open("D:/mystuff/rules1.txt")
lines=f.readlines()
print(len(lines))
e=[]
for line in lines:
  w=line.strip().split(",")
  W=[int(v) for v in w]
  e.append(W)
print(e)
import numpy as np
E=np.array(e)
Q=np.zeros(E.shape)
print(Q)
