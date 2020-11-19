import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("euro.csv")
country='euro'
n=len(data[country])
days1=245
y=data[country][n-days1:n]
x=np.arange(n-days1,n)
valid = ~(np.isnan(x) | np.isnan(y))
model=np.poly1d(np.polyfit(x[valid],y[valid],10))
date=data['date'][n-1]
x1=np.arange(n-days1,n+7)
y1=model(x1)
plt.plot(x,y,'k')
plt.plot(x1,y1,'b')
days2=145
y=data[country][n-days2:n]
x=np.arange(n-days2,n)
import numpy as np
valid = ~(np.isnan(x) | np.isnan(y))
model=np.poly1d(np.polyfit(x[valid],y[valid],10))
x1=np.arange(n-days2,n+7)
y1=model(x1)
plt.plot(x1,y1,'r')
plt.legend(['daily deaths in '+str(country),str(days1)+' days from '+str(date),str(days2)+' days from '+str(date)])
plt.show()
