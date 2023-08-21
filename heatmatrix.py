import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

class HeatMatrix():
    def __init__(self, amb_temp, size_x, size_y):
        """
            Initializes temperature matrix temp.

            Args:
            - amb_temp: the initial ambient temperature of the plate
            - size_x: the width of the plate
            - size_y: the height of the plate
        """
        pass

    def add_heat_source(self, source_temp, source_x, source_y, size):
        """
            Adds a heat source to the temperature matrix.

            Args:
            - source_temp: the temperature of the heat source
            - source_x: the x-coordinate of the center of the heat source
            - source_y: the y-coordinate of the center of the heat source
            - size: the size of the heat source
        """
        pass

    def diffuse(self):
        """Diffuses the HeatMatrix object according to the diffusion equation one time step."""
        pass

    def plot_heat_matrix(self, time):
        """Converts the heat matrix into a matplotlib pyplot."""
        # clear the plot
        plt.clf()

        # labels
        plt.title(f"Temperature at t = {time}")
        plt.xlabel("x")
        plt.ylabel("y")

        # colors
        plt.pcolormesh(self.temp, cmap=plt.cm.jet, vmin=0, vmax=200)
        plt.colorbar()

        return plt
