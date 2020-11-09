import pandas as pd
import numpy as np
data=pd.read_csv("euro.csv")
n=len(data["death"])
days=100
y=data["death"][n-days:n]
x=np.arange(n-days,n)
from scipy.optimize import curve_fit
def func(x,a,b,c,d,e,f,g):
 return a*x*x*x*x*x*x+b*x*x*x*x*x+c*x*x*x*x+d*x*x*x+e*x*x+f*x+g
param=curve_fit(func,x,y)
[a,b,c,d,e,f,g]=param[0]
print(a,b,c,d,e,f,g)
print(data['date'][n-1])
import matplotlib.pyplot as plt
print("Nov.4+7  deaths",int(func(n-1+7,a,b,c,d,e,f,g)))
print("Nov.4+10 deaths",int(func(n-1+10,a,b,c,d,e,f,g)))
print("Nov.4+14 deaths",int(func(n-1+14,a,b,c,d,e,f,g)))
plt.plot(x,y,'k')
plt.plot(x,func(x,a,b,c,d,e,f,g),'r')
x1=np.arange(n-days,n+15)
plt.plot(n-1+7,func(n-1+7,a,b,c,d,e,f,g),'ro')
plt.plot(n-1+10,func(n-1+10,a,b,c,d,e,f,g),'ro')
plt.plot(n-1+14,func(n-1+14,a,b,c,d,e,f,g),'ro')
plt.plot(x1,func(x1,a,b,c,d,e,f,g),'r')
days=220
y=data["death"][n-days:n]
x=np.arange(n-days,n)
from scipy.optimize import curve_fit
def func(x,a,b,c,d,e,f,g):
 return a*x*x*x*x*x*x+b*x*x*x*x*x+c*x*x*x*x+d*x*x*x+e*x*x+f*x+g
param=curve_fit(func,x,y)
[a,b,c,d,e,f,g]=param[0]
print(a,b,c,d,e,f,g)
print(data['date'][n-1])
import matplotlib.pyplot as plt
print("Nov.4+7  deaths",int(func(n-1+7,a,b,c,d,e,f,g)))
print("Nov.4+10 deaths",int(func(n-1+10,a,b,c,d,e,f,g)))
print("Nov.4+14 deaths",int(func(n-1+14,a,b,c,d,e,f,g)))
plt.plot(x,y,'k')
plt.plot(x,func(x,a,b,c,d,e,f,g),'b')
x1=np.arange(n-days,n+15)
plt.plot(n-1+7,func(n-1+7,a,b,c,d,e,f,g),'bo')
plt.plot(n-1+10,func(n-1+10,a,b,c,d,e,f,g),'bo')
plt.plot(n-1+14,func(n-1+14,a,b,c,d,e,f,g),'bo')
plt.plot(x1,func(x1,a,b,c,d,e,f,g),'b')
plt.legend(['last 200 days from Nov.4','last 100 days from Nov.4'])
plt.show()
