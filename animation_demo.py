import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

xs = [0, 1, 5, 3, 5, 7, 9, 5, 2, 1]
ys = [4, 5, 3, 3, 5, 7, 6, 4, 1, 5]

def animate(i):
    ax1.clear()
    ax1.scatter(xs[i], ys[i])

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
