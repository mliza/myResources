#!/opt/homebrew/bin/python3.9
'''
    Date:   06/26/2021
    Author: Martin E. Liza
    File:   stagnationParser.py
    Def:    Parses the stagnation data from the output.plt 
            to a .dat file. 
            
            ./stagnationParser.py "data_folder_in"


    Author          Date        Revision
    ------------------------------------------ 
    Martin E. Liza  06/26/2021  Initial Version
'''
import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *
import sys 
import os

# Inputs 
data_folder = sys.argv[1] 

# Path modifications 
abs_tools_path = os.environ.get('TOOLS') 
abs_current_path = os.path.abspath(os.getcwd())
abs_data_in_path = os.path.join(abs_current_path, data_folder)

tp.macro.execute_command(f"""$!ReadDataSet  '\"{abs_data_in_path}/output.plt\" '
  ReadDataOption = New
  ResetStyle = No
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"x\" \"y\" \"rho_N2\" \"rho_O2\" \"rho_NO\" \"rho_N\" \"rho_O\" \"U\" \"V\" \"T\" \"Tv\" \"rho\" \"P\" \"H\" \"tau\" \"gamma\" \"kappa_tr\" \"mu\" \"index\"'""")
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 2.88043478261
  Y = 3.17391304348
  ConsiderStyle = Yes''')
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 7.64130434783
  Y = 2.64130434783
  ConsiderStyle = Yes''')
tp.macro.execute_extended_command(command_processor_id='Extract Precise Line',
    command=f"XSTART = -0.015 YSTART = 0 ZSTART = 0 XEND = 0 YEND = 0 ZEND = 0 NUMPTS = 1000 EXTRACTTHROUGHVOLUME = F EXTRACTTOFILE = T EXTRACTFILENAME = '{abs_data_in_path}/stagnationData.dat' ")
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 5.6847826087
  Y = 0.869565217391
  ConsiderStyle = Yes''')
# End Macro.

