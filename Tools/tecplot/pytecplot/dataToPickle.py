#!/opt/homebrew/bin/python3.9
'''
    Date:   06/27/2021
    Author: Martin E. Liza
    File:   dataToPickle.py
    Def:    loads a tecplot file and outputs a 
            dictionary pickle file 
            
            ./dataToPickle.py "data_folder_in" "data_file_in.ext"

    Author          Date        Revision
    ------------------------------------------ 
    Martin E. Liza  06/27/2021  Initial Version.
    Martin E. Liza  07/14/2021  Added the capability to store the  
                                multi-dimensional array per zone.
'''
import tecplot as tp 
import numpy as np
import pickle 
import os 
import sys 
import IPython

# Inputs 
data_folder_in = sys.argv[1] 
data_file_in   = sys.argv[2] 

# Data paths
abs_tools_path   = os.environ.get('TOOLS') 
abs_current_path = os.path.abspath(os.getcwd()) 
abs_data_in_path = os.path.join(abs_current_path, data_folder_in) 
file_name_in     = data_file_in.rsplit('.', 1)[0] 

# Load data (pytecplot functions) 
data_in = tp.data.load_tecplot(os.path.join(abs_data_in_path, data_file_in)) 
data_variable_name = data_in.variable_names
zone_names = data_in.zone_names 

# Loads the data in a  multi dimensional dictionary 
data_dict = { } 
for i in range(len(zone_names)):
    working_zone = zone_names[i] 
    data_dict[f'{working_zone}'] = { }
    for j in range(len(data_variable_name)):
        working_variable = data_variable_name[j] 
        data_dict[f'{working_zone}'][f'{working_variable}'] = data_in.zone(
                working_zone).values(working_variable)[:] 

# Store data in a dictionary 
pickle_out = open(os.path.join(abs_data_in_path, f'{file_name_in}.pickle'), 'wb')
pickle.dump(data_dict, pickle_out) 
pickle_out.close() 
