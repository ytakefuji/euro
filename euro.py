import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
data=pd.read_csv("euro.csv")
n=len(data)
y=data["death"][120:n]
x=np.arange(120,n)
from scipy.optimize import curve_fit
def func(x,a,b,c,d):
 return a*x*x*x+b*x*x+c*x+d
param=curve_fit(func,x,y)
[a,b,c,d]=param[0]
print(a,b,c,d)
print(data["date"][n-1]+' after 1 week',int(func(n+6,a,b,c,d)))
print(data["date"][n-1]+' after 2 weeks',int(func(n+13,a,b,c,d)))
print(data["date"][n-1]+' after 3 weeks',int(func(n+20,a,b,c,d)))
plt.plot(x,y,'b')
x1=np.arange(120,n+25)
plt.plot(n+6,func(n+6,a,b,c,d),'ro')
plt.plot(n+13,func(n+13,a,b,c,d),'ro')
plt.plot(n+20,func(n+20,a,b,c,d),'ro')
plt.plot(x1,func(x1,a,b,c,d),'r')
plt.show()
