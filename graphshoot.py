import matplotlib.pyplot as plt
import numpy as np 
import math


x=np.arange()
y=4.66*(1-np.exp(-3.77*x))

plt.figure(1)
plt.ylim(ymin=0, ymax=15)
plt.plot(x,y)
plt.xlabel('distance aux buts')
plt.ylabel('vitesse du shoot')
plt.title('Fonction Shoot')
plt.show