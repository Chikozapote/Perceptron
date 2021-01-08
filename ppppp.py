import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as math
import random

w1=round(random.uniform(-1, 1),4)
w2=round(random.uniform(-1, 1),4)
w3=round(random.uniform(-1, 1),4)
w=[w1,w2,w3]
w=np.array(w)

def funcion(i,w):
    return (-w[0] * (i) - w[2])/w[1]
def actualiza(pos):
    w1 = x[pos][0] * x[pos][2] + w[0]
    w2 = x[pos][2] * x[pos][2] + w[1]
    w3 = w[2]
    print(f"nuevaw1={w1}    nuevaw2={w2}    nuevaw3={w3}")
    w[0] = w1
    w[1] = w2
    w[2] = w3

x = genfromtxt('datasets.csv', delimiter=',')
for dato in x:
    color=''
    if dato[2]==-1: color='r'
    else: color='b'
    math.scatter(dato[0],dato[1],marker='o',color=color)
math.show()

print("Valores de inicio w:")
print(w)
conta=1
axe=0
pos=0
err=0
termina = False

while not termina:
   print(f"Actualizacion no.{conta}")
   cont=0
   con = 0
   if err==1:
       cont=pos
   for data in  x:
       if(err==0 or (err==1 and con==cont)):
           ax = [data[0], data[1], 1]
           fx = np.dot(ax, w)
           if fx > 0:
               fx = 1
           else:
               fx = -1
           if data[2] != fx:
              actualiza(con)
              pos = con
              err=1
           else: err=0
       con += 1
   conta+=1
   if err== 0 or con >= 100:
        termina = True

for dato in x:
    color=''
    if dato[2]==-1: color='r'
    else: color='b'
    math.scatter(dato[0],dato[1],marker='o',color=color)
x=range(1,5)
math.plot(x,[funcion(i,w) for i in x])
math.show()
