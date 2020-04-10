#Python Packages 
import os 
import subprocess

#Note: 
#scriptsFolder, should be configure to where your matlab script lives 
#matlab path should be configure to where your matlab lives; this path can be found by 
# typing 'which matlab' in the matlab command line 

#Ex. myMatlab.m 
# call python 
# import productivity 
# productivity.matlabInPython('myMatlab') 

#This function allows you to call a matlab function using python 
def matlabInPython(matlabFunction):  #note matlabFunction = 'myFunction'
    scriptsFolder = os.path.abspath(os.path.join(__file__, '../../')) #go back one from my current directory 
    matlabFolder = os.path.join(scriptsFolder,'Matlab/') #go into the matlab folder path 
    matlabPath = '/Applications/Matlab.app/bin//matlab'   #Matlab's software path 
    matlabStr = f' "cd {matlabFolder}; {matlabFunction}; exit" '
    shellStr = matlabPath + ' -nodesktop -nosplash -r ' + matlabStr #string running in shell
    subprocess.call([shellStr], shell=True) #runs shell

def vData(inData, column): #Similar to A(indx,:) in matlab 
    outData = []
    for indx in range(len(inData)):
        outData.append(inData[indx][column])
    return outData 
