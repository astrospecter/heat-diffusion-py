import numpy as np
import matplotlib.pyplot as plt

def initialize_temp_matrix(plate_x, plate_y, amb_temp):
    temp_matrix = np.empty((plate_x, plate_y))
    temp_matrix.fill(amb_temp)
    return temp_matrix

def diffuse(temp_matrix, plate_x, plate_y, diff_const):
    prev_temp_matrix = np.copy(temp_matrix)
    for i in range(1, plate_x-1, 1):
        for j in range(1, plate_y-1, 1):
            temp_matrix[i, j] = diff_const * (prev_temp_matrix[i+1][j] + prev_temp_matrix[i-1][j] + prev_temp_matrix[i][j+1] + prev_temp_matrix[i][j-1] - 4*prev_temp_matrix[i][j]) + prev_temp_matrix[i][j]
    return temp_matrix

def set_heat_source(temp_matrix, source_temp, x, y):
    # this is temporary
    temp_matrix[x][y] = source_temp
    return temp_matrix

def temp_to_rgba(temp_matrix, size_x, size_y):
    rgba = []
    for i in range(size_x):
        for j in range(size_y):
            curr_color = temp_matrix[i][j]
            if curr_color > 150 and curr_color <= 200:
                r = 255
                g = (200 - curr_color) * (255 / 50)
                b = 0
            elif curr_color > 100 and curr_color <= 150:
                r = (curr_color - 100) * (255 / 50)
                g = 255
                b = 0
            elif curr_color > 50 and curr_color <= 100:
                r = 0
                g = 255
                b = (100 - curr_color) * (255/50)
            elif curr_color > 0 and curr_color <= 50:
                r = 0
                g = curr_color * (255/50)
                b = 255
            elif curr_color > 200:
                r = 255
                g = 255
                b = 255
            else:
                r = 0
                g = 0
                b = 0
            rgba.extend([r,g,b,255])
    return rgba

# for debugging
def plotheatmap(u_k, k, delta_t):
    # Clear the current plot figure
    plt.clf()

    plt.title(f"Temperature at t = {k*delta_t:.3f} unit time")
    plt.xlabel("x")
    plt.ylabel("y")

    # This is to plot u_k (u at time-step k)
    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)
    plt.colorbar()

    return plt