import numpy as np
from matplotlib import pyplot as plt

def lineChart(xdata, ydata, xlabel, ylabel, title):
    plt.plot(xdata, ydata)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def barChart(xdata, ydata, xlabel, ylabel, title):
    y_pos = np.arange(len(xdata))

    plt.bar(y_pos, ydata, align='center', alpha=0.5)
    plt.xticks(y_pos, xdata)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()