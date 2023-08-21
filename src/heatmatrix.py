import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

class HeatMatrix():
    def __init__(self, amb_temp, size_x, size_y, diff_const):
        """
            Initializes temperature matrix temp.

            Args:
            - amb_temp: the initial ambient temperature of the plate
            - size_x: the width of the plate
            - size_y: the height of the plate
            - diff_const: the diffusion constant
        """
        self.temp = np.empty((size_x, size_y))
        self.temp.fill(amb_temp)
        self.temp_xlen = size_x
        self.temp_ylen = size_y
        self.diff_const = diff_const
        self.time = 0

    def init_heat_source(self, source_temp, source_x, source_y, size):
        """
            Saves heat source information to the object.
            
            Args:
            - source_temp: the temperature of the heat source
            - source_x: the x-coordinate of the center of the heat source
            - source_y: the y-coordinate of the center of the heat source
            - size: the size of the heat source
        """
        self.source_temp = source_temp
        self.source_x = source_x
        self.source_y = source_y
        self.source_size = size

    def add_heat_source(self):
        """Adds a heat source to the temperature matrix."""
        for i in range(self.source_x - self.source_size, self.source_x + self.source_size):
            for j in range(self.source_y - self.source_size, self.source_y + self.source_size):
                if i > 0 and i < self.temp_xlen and j > 0 and j < self.temp_ylen:
                    self.temp[i,j] = self.source_temp

    def diffuse(self):
        """Diffuses the HeatMatrix object according to the diffusion equation one time step."""
        for i in range(1, self.temp_xlen - 1):
            for j in range(1, self.temp_ylen - 1):
                self.temp[i,j] = self.diff_const * (self.temp[i+1, j] + self.temp[i-1, j] + self.temp[i, j+1], self.temp[i, j-1] - 4*self.temp[i,j]) + self.temp[i,j]


    def plot_heat_matrix(self):
        """Converts the heat matrix into a matplotlib pyplot."""
        # clear the plot
        plt.clf()

        # labels
        plt.title(f"Temperature at t = {self.time}")
        plt.xlabel("x")
        plt.ylabel("y")

        # colors
        plt.pcolormesh(self.temp, cmap=plt.cm.jet, vmin=0, vmax=200)
        plt.colorbar()

        return plt
