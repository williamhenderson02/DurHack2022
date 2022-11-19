import matplotlib.pyplot as plt
from itertools import count
import random 
from matplotlib.animation import FuncAnimation

time = [i for i  in range(0,20,1)]
val = [random.randint(0,200) for i in range(20) ]

plt.figure(figsize = (8,4))
plt.plot(time,val)

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



plt.show()