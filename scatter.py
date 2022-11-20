import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd



'''time = [i for i  in range(0,20,1)]
val = [random.randint(0,200) for i in range(20) ]
print(time,val)


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

plt.show()'''


fieldNames =['Time', 'Price']

fig, ax = plt.subplots()
ax.ticklabel_format(style = 'plain')

def scatter(i):
    data = pd.read_csv('scatter.csv')

    time_arr = data['Time']
    price_arr = data['Price']
    plt.cla()
    ax.ticklabel_format(style = 'plain')
    plt.plot(data.index, price_arr)
    plt.savefig('scatter.png')

scatAni = FuncAnimation(plt.gcf(),scatter,interval = 1000)
plt.show()
    

'''
while True:
    time_arr = []
    val_arr = []


    response = ws.recv()
    data = json.loads(response)

    

    plt.figure(figsize = (8,4))
    #lt.plot(time_arr,val_arr)
    
    index = count()

    def scatter(i):
        time = data["T"]
        val = float(data["p"])
        time_arr.append(time)
        time_arr.pop(0)
        val_arr.append(val)
        val_arr.pop(0)
        
        plt.cla()
        plt.plot(time_arr,val_arr)

        sleep(1)
    scatAni = FuncAnimation(plt.gcf(),scatter,interval = 1000)

    plt.show()
    


    '''