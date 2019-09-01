import numpy as np
import matplotlib.pyplot as plt

import subprocess
import shlex


A=np.array([-2,-2])
B=np.array([1,3])
len=10

x_AB=np.zeros((2,len))
lam=np.linspace(0,1,len)
for i in range(len)
   temp1=A+lam[i]*(B-A)
   X-AB[:,i]=temp1.T

plt.plot(x_AB[0,:],x_AB[1,:],label=$AB$)
plt.grid()

plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1+0.1),A[1]*(1-0.1),'A')

plt.plot(B[0],B[1],'0')
plt.text(B[0]*(1-0.1),B[1]*(1+0.1),'B')

plt.show()
