# -*- coding: utf-8 -*-

import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2

"""Import matplotlib.pyplot as plt and set %matplotlib inline if you are using the jupyter notebook. What command do you use if you aren’t using the jupyter notebook?

"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

#If I not using the jupyter notebook we use: plt.show()

"""Exercise 1
Follow along with these steps:

Create a figure object called fig using plt.figure()
Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax.
Plot (x,y) on that axes and set the labels and titles to match the plot below:


"""

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Figure plt')

"""Exercise 2
Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.
"""

fig2 = plt.figure()

ax1 = fig2.add_axes([0,0,1,1])
ax2 = fig2.add_axes([0.2,0.5,.2,.2])

"""Now plot (x,y) on both axes. And call your figure object to show it.


"""

ax1.plot(x,y)
ax2.plot(x,y)

fig2

"""Exercise 3
Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]

"""

fig3 = plt.figure()
ax31 = fig3.add_axes([0,0,1,1])
ax32 = fig3.add_axes([0.2,0.5,.4,.4])

"""Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and ylimits on the inserted plot:"""

ax31.set_xlim(0,100)
ax31.set_ylim(0,10000)

ax32.set_xlim(20,22)
ax32.set_ylim(30,50)

ax31.plot(x,z)
ax32.plot(x,y)

ax31.set_xlabel('X')
ax31.set_ylabel('Z')

ax32.set_xlabel('X')
ax32.set_ylabel('Y')
ax32.set_title('zoom')

fig3

"""Exercise 4
Use plt.subplots(nrows=1, ncols=2) to create the plot below.
"""

fig4, ax4 = plt.subplots(nrows=1, ncols=2)

"""Now plot (x,y) and (x,z) on the axes. Play around with the linewidth and style"""

ax4[0].set_xlim(0,100)
ax4[0].set_ylim(0,200)
ax4[1].set_xlim(0,100)
ax4[1].set_ylim(0,10000)

ax4[0].plot(x,y,color='blue',lw="3",ls="--")
ax4[1].plot(x,z,color='red',lw="3",ls="-")

"""See if you can resize the plot by adding the figsize() argument in plt.subplots() are copying and pasting your previous code."""

fig5,ax5 = plt.subplots(nrows=1,ncols=2, figsize=(8,2))

ax5[0].plot(x,y,color='blue',lw="5",ls="-")
ax5[1].plot(x,z,color='red',lw="3",ls="--")
