# -*- coding: utf-8 -*-
"""SineRBF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1flTR8tH7LHZp70xxHWbv8rDC-y7_aNPd
"""

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
x = np.linspace(-2, 2, 21)  
y = np.sin((np.pi/4)*x)                
obb=KMeans(4)
obb=KMeans(4)
obb.fit(x[:,np.newaxis])
km = np.reshape(obb.cluster_centers_,(4,))
b=np.ones(4)
class RBF:
  def __init__(self,input,target,neurons=4,centers=km,bias=b):
    self.input=input
    self.target=target
    self.neurons=neurons
    self.centers=centers
    self.bias=bias
  
  def distance(self,a,b):
    if(np.ndim(a)==0 and np.ndim(b)==0):
      return np.abs(a-b)
    else:
      sum=0
      for i in range(len(a)):
        sum += pow(a[i]-b[i],2)
      return np.sqrt(sum)
    
  def predict(self,input):
    x2=[]
    for i in range(self.input.shape[0]):
      a1=np.zeros(self.neurons)
      for j in range(self.neurons):
        a1[j]=np.exp(-((self.distance(self.input[i],self.centers[j])*self.bias[j])**2))
      x2.append(a1)     
    model=Sequential()
    model.add(Dense(1,activation='linear'))
    model.compile(loss='mse',optimizer='adam')
    model.fit(np.array(x2),self.target,epochs=2000)
    return model.predict(np.array(x2))
#m=RBF(x,y)    
m=RBF(x,y,3,np.array([-2,0,2]),np.array([1,1,1]))
plt.figure()
plt.plot(x,y,'r--x',x,m.predict(x),'b--o')
plt.show()