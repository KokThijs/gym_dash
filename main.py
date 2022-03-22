'''
Name: Dashboard for gymmoe
Author: Thijs Kok
e-mail: thijs-kok@live.nl
Version: 0.x
Date: 21-03-22

DATA: Gathered from the microsoft forms we filled in during our gym times.

purpose: Plot and visualize our progression in the gym.

NOTE: I want to implement a logger, use bokeh, and panel.
'''

import pandas as pd
from filepath import FILEPATH as path
import matplotlib.pyplot as plt
from DataCleaner import ParseAndClean
import logging


def main():
    '''
    initialize logger and call the classes
    '''
    test = ParseAndClean(path)
    test.get_df()
    print(test.select_name('Lennard'))
    # print(test)
    

if __name__ == '__main__':
    main()