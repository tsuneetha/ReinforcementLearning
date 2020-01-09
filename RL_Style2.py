f=open("D/mystuff/rules2.txt")
lines=f.readlines()
prit(len(lines))
scnt=[]
acnt=[]
rewards=[]
for line in lines:
  w=line.strip().split(",")
  rewards.append(float(w[-1])
  scnt.append(w[0])
  acnt.append(w[1])
print(rewards)
ns=len(set(scnt))
na=len(set(acnt))
import numpy as np
E=np.array(rewards).reshape((ns,na))
print(E)
Q=np.zeros(E.shape)
print(Q)
