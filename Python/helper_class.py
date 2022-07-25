#!/opt/homebrew/bin/python3
'''
    Date:   07/18/2022
    Author: Martin E. Liza
    File:   helper_class.py
    Def:    Contains some helper functions 
            for data processing and manipulation.  

    Author		    Date		Revision
    ----------------------------------------------------
    Martin E. Liza	05/23/2022	Initial version.
    Martin E. Liza	07/18/2022	Added pickle_dict_add.
'''
import os 
import pickle 
import numpy as np 
import IPython 
from scipy.io import FortranFile  
from dataclasses import dataclass

@dataclass 
class Helper:  
    pass 

# Loading unformatted fortran data  
    def fortran_data_loader(self, variable_in, abs_path_in, d_type=float): 
        data_in = os.path.join(abs_path_in, f'{variable_in}')
        f_in    = FortranFile(data_in, 'r')
        data    = f_in.read_reals(dtype=d_type)
        f_in.close() 
        return data

# Save data as pickle and loads data as a pickle 
    def pickle_manager(self, pickle_name_file, pickle_path, data_to_save=None):
        # Loads pickle file if data_to_save is empty  
        if data_to_save is None:  
            file_in   = os.path.join(f'{pickle_path}',f'{pickle_name_file}.pickle') 
            pickle_in = open(file_in, 'rb')
            return pickle.load(pickle_in)
        # Creates pickle file if data_in has a path and saves it in that path  
        else:
            file_out   = os.path.join(f'{pickle_path}',f'{pickle_name_file}.pickle') 
            pickle_out = open(file_out, 'wb') 
            pickle.dump(data_to_save, pickle_out)
            pickle_out.close() 

# Opens pickle dictionary, adds a variable and saves it
    def pickle_dict_add(self, var_in_data, var_in_str, pickle_path, 
                        pickle_dict_in, pickle_dict_out):
        # Open pickle dictionary 
        dict_in = self.pickle_manager(pickle_dict_in, pickle_path) 
        dict_in[var_in_str] = var_in_data
        self.pickle_manager(pickle_dict_out, pickle_path, dict_in)
