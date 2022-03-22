'''
Name: Dashboard for gymmoe
Author: Thijs Kok
e-mail: thijs-kok@live.nl
Version: 0
Date: 21-03-22

DATA: Gathered from the microsoft forms we filled in during our gym times.

purpose: Plot and visualize our progression in the gym.

NOTE: I want to implement a logger, use bokeh, and panel.
'''

import pandas as pd
from filepath import FILEPATH as path
import logging

class DataFinder():
    '''
    This class will find the datafile and open it. 
    uses Pandas
    '''
    def __init__(self, file_path):
        self.file_path = file_path

    def make_df(self):
        '''
        open the excel file (.xlsx)
        store the dataframe to self
        '''
        try:
            self.df = pd.read_excel(self.file_path)
        except Exception as e:
            print(f'Error: {e}')

def main():
    '''
    initialize logger and call the classes
    '''
    

if __name__ == '__main__':
    main()