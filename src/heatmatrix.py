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