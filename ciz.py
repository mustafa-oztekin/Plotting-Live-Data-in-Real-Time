import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from itertools import count

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv("data.csv")
    x = data["sira"]
    y = data["deger"]

    plt.cla()
    plt.plot(x, y)
    
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
