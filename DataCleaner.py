'''
This module contains the class DataCleaner that's used to open and clean the dataframe. 
The class will be used by the final program to 'stream' the data.

version: 0.x
'''
import pandas as pd


class ParseAndClean():
    '''
    This class will find the datafile and open it. 
    uses Pandas
    '''
    def __init__(self, file_path):
        self.file_path = file_path


    def get_df(self):
        '''
        open the excel file (.xlsx)
        store the dataframe to self
        '''
        try:
            self.data_frame = pd.read_excel(self.file_path)
        except Exception as e:
            print(f'Error: {e}')


    def clean_file(self):
        '''
        This function is used to clean the dataframe.
        cleaning:
            -   remove: 'ID', 'Begintijd', 'E-mail', 'Naam'
        '''


    def select_name(self, name = 'Thijs'):
        '''
        Select subject from the dataframe
        input: self.dataframe > the actual complete dataframe
        
        returns: slice of the dataframe in a new variable > data_frame_slice
        '''
        self.data_frame_slice = self.data_frame[self.data_frame['Wie ben je ?'] == name]
        return self.data_frame_slice


    def __str__(self):
        print(self.data_frame['Wie ben je ?'])
        # print(self.data_frame.info())