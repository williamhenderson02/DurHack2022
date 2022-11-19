import matplotlib.pyplot as plt
import random 
from matplotlib.animation import FuncAnimation
import pandas as pd

time = [i for i  in range(0,20,1)]
val = [random.randint(0,200) for i in range(20) ]

#prices = pd.DataFrame({'Time':[], 'Open': [],'Close': [], 'High': [],'Low': []})

#up = prices[prices.close >= prices.open]
#down = prices[prices.close < prices.open]
col1= "red"
col2 = "green"


def candle(i):
    data = pd.read_csv('candle.csv')


    time_arr = data['Time']
    open_arr = data['Open']
    close_arr = data['Close']    
    high_arr = data['High']
    low_arr = data['Low']

    prices = pd.DataFrame({'time':time_arr, 'open': open_arr,'close': close_arr , 'high': high_arr,'low': low_arr})
    up = prices[prices.close >= prices.open]
    down = prices[prices.close < prices.open]


    plt.cla()
    
    plt.bar(up.index,up.close-up.open,w,bottom = up.open, color = col2)
    plt.bar(up.index,up.high-up.close,w2,bottom = up.close, color = col2)
    plt.bar(up.index,up.low-up.open,w2,bottom = up.open, color = col2)

    plt.bar(down.index,down.close-down.open,w,bottom = down.open, color = col1)
    plt.bar(down.index,down.high-down.open,w2,bottom = down.open, color = col1)
    plt.bar(down.index,down.low-down.close,w2,bottom = down.close, color = col1)
    
    
    

w = 0.80
w2= 0.03

#print(prices)

plt.figure(figsize =(8,4))

candleAni = FuncAnimation(plt.gcf(),candle,interval = 1000)

plt.show()