#!/opt/homebrew/bin/python3.9
'''
    Date:   07/02/2021
    Author: Martin E. Liza
    File:   convergencePlot.py
    Def:    Parses the stagnation data from the output.plt 
            to a .dat file. 
            
            ./convergencePlot.py "data_folder_in" "data_path_out"


    Author          Date        Revision
    ------------------------------------------ 
    Martin E. Liza  07/02/2021  Initial Version
'''
import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *
import sys 
import os 

# Inputs 
data_folder  = sys.argv[1] 
abs_path_out = sys.argv[2] 

# Path modifications 
abs_tools_path   = os.environ.get('TOOLS') 
abs_current_path = os.path.abspath(os.getcwd())
abs_data_in_path = os.path.join(abs_current_path, data_folder) 


tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.active_page().name='Untitled'
tp.add_page()
tp.macro.execute_command('''$!Pick SetMouseMode
  MouseMode = Select''')
tp.load_layout('/Users/martin/Documents/Research/UoA/Tools/tecplot/layouts/convergence.lay')
tp.macro.execute_command(f"""$!ReadDataSet  '\"{abs_data_in_path}/convergence.plt\" '
  ReadDataOption = New
  ResetStyle = No
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"ITER\" \"MAX_RESIDUAL\" \"MAX_RES_CELL\" \"L2_RESIDUAL\" \"dt\" \"CFL\" \"time\" \"ablw\"'""")
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 4.24141048825
  Y = 4.92269439421
  ConsiderStyle = Yes''')
tp.active_frame().plot().view.fit()
tp.export.save_png(f'{abs_path_out}.png',
    width=622,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
# End Macro.
