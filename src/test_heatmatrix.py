from heatmatrix import diffuse, set_heat_source, initialize_temp_matrix, plotheatmap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

print("2D heat equation solver")

plate_length = 50
max_iter_time = 200

alpha = 2
delta_x = 1

delta_t = (delta_x ** 2)/(4 * alpha)
gamma = (alpha * delta_t) / (delta_x ** 2)

u = initialize_temp_matrix(plate_length, plate_length, 0)

u = set_heat_source(u, 100, 25, 25)

frames = [u]

# Do the calculation here
for k in range(1, max_iter_time):
    u = diffuse(u, plate_length, plate_length, gamma)
    u = set_heat_source(u, 100, 25, 25)
    frames.append(u)

def animate(k):
    plotheatmap(frames[k], k, delta_t)

anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=max_iter_time, repeat=False)
plt.show()

print("Done!")