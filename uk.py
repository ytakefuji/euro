import pandas as pd
import numpy as np
data=pd.read_csv("death.csv")
y=data["uk"][99:299]
x=np.arange(99,299)
from scipy.optimize import curve_fit
def func(x,a,b,c,d,e,f,g):
 return a*x*x*x*x*x*x+b*x*x*x*x*x+c*x*x*x*x+d*x*x*x+e*x*x+f*x+g
param=curve_fit(func,x,y)
[a,b,c,d,e,f,g]=param[0]
print(a,b,c,d,e,f,g)
import matplotlib.pyplot as plt
print("Nov. 3 deaths",int(func(308,a,b,c,d,e,f,g)))
print("Nov. 13 deaths",int(func(318,a,b,c,d,e,f,g)))
print("Dec. 23 deaths",int(func(358,a,b,c,d,e,f,g)))
plt.plot(x,y)
plt.plot(x,func(x,a,b,c,d,e,f,g))
x1=np.arange(99,360)
plt.plot(308,func(308,a,b,c,d,e,f,g),'ro')
plt.plot(318,func(318,a,b,c,d,e,f,g),'ro')
plt.plot(358,func(358,a,b,c,d,e,f,g),'ro')
plt.plot(x1,func(x1,a,b,c,d,e,f,g))
plt.show()
