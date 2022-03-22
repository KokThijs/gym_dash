'''
This module contains the class PlotData and uses several libraries to achieve the plotting.

version: 0.x
'''

import matplotlib.pyplot as plt

class PlotData():
    '''
    Contains methods used to plot the data.
    pass the ParseAndClean object to instanciate
    '''
    def __init__(self, name_object):
        self.name_object = name_object

    def plot_hist(self, column):
        pass