#!/opt/homebrew/bin/python3.9
import tecplot as tp 
import numpy as np
import matplotlib.pyplot as plt
import IPython 

# Load data 
dataIn = tp.data.load_tecplot("wall_data1.plt") 

# Import X and Y as arrays 
dataX = dataIn.zone('ZONE 001').values('X')[:] 
dataY = dataIn.zone('ZONE 001').values('Y')[:] 
dataKappa = dataIn.zone('ZONE 001').values('kappa_tr')[:] 

# Shift data on X and Y  
shiftX  = np.min(dataX) * np.ones( np.size(dataX) ) 
xOrigin = dataX - shiftX 
shiftY  = np.min(dataY) * np.ones( np.size(dataY) ) 
yOrigin = dataY - shiftY 

# Sort the Y axis in Descending way 
yOrigin[::-1].sort()

# Create theta 
theta = np.rad2deg( np.arctan2(yOrigin, xOrigin) )
theta = np.float32(theta) 

# Add data to the original file and save it 
dataIn.add_variable('theta')
dataIn.zone('ZONE 001').values('theta')[:] = theta.tolist() 
tp.data.save_tecplot_plt( 'test.plt' )

#IPython.embed(colors='Linux') 

