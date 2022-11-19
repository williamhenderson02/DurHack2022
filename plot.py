import matplotlib.pyplot as plt
from itertools import count
import random 
from matplotlib.animation import FuncAnimation
import pandas as pd

time = [i for i  in range(0,20,1)]
val = [random.randint(0,200) for i in range(20) ]

prices = pd.DataFrame({'open': [random.randint(0,200) for i in range(20) ],
'close': [random.randint(0,200) for i in range(20) ],
'high': [200 for i in range(20) ],
'low': [0 for i in range(20) ]})

up = prices[prices.close >= prices.open]
print(up.index)
down = prices[prices.close < prices.open]
col1= "red"
col2 = "green"

index = count()

def candle(i):
    time.append(next(index))
    time.pop(0)
    prices.append({'open': [random.randint(0,200) for j in range(20) ],
'close': [random.randint(0,200) for j in range(20) ],
'high': [200 for j in range(20) ],
'low': [0 for j in range(20) ]}, ignore_index = True)
    prices.T.pop(0)
    

    plt.bar(up.index,up.close-up.open,w,bottom = up.open, color = col2)
    plt.bar(up.index,up.high-up.close,w2,bottom = up.close, color = col2)
    plt.bar(up.index,up.low-up.open,w2,bottom = up.open, color = col2)

    plt.bar(down.index,down.close-down.open,w,bottom = down.open, color = col1)
    plt.bar(down.index,down.high-down.open,w2,bottom = down.open, color = col1)
    plt.bar(down.index,down.low-down.close,w2,bottom = down.close, color = col1)
    
    plt.cla()
    

w = 0.80
w2= 0.03

print(prices)

plt.figure(figsize =(8,4))

candleAni = FuncAnimation(plt.gcf(),candle,interval = 1000)

plt.show()

'''
plt.figure(figsize = (8,4))
plt.plot(time,val)

#global index
index = count()
for i in range(20): next(index)



def scatter(i):
    time.append(next(index))
    time.pop(0)
    val.append(random.randint(0,200))
    val.pop(0)
    
    plt.cla()
    plt.plot(time,val)

scatAni = FuncAnimation(plt.gcf(),scatter,interval = 1000)

def candle(i):
    time.append(next(index))
    time.pop(0)
    val.append(random.randint(0,200))
    val.pop(0)



plt.show()'''