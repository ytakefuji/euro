import pandas as pd
import numpy as np
data=pd.read_csv("euro.csv")
y=data["death"][120:246]
x=np.arange(120,246)
from scipy.optimize import curve_fit
def func(x,a,b,c,d):
 return a*x*x*x+b*x*x+c*x+d
param=curve_fit(func,x,y)
[a,b,c,d]=param[0]
print(a,b,c,d)
import matplotlib.pyplot as plt
# you must modify the followings:
print("Nov. 28 after 1 week",int(func(270,a,b,c,d)))
print("Nov. 28 after 2 weeks",int(func(300,a,b,c,d)))
print("Nov. 28 after 3 weeks",int(func(300,a,b,c,d)))
plt.plot(x,y)
plt.plot(x,func(x,a,b,c,d))
plt.show()