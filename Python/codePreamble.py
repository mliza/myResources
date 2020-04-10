#!/usr/local/bin/python3.7
import argparse 
import subprocess 

# Available options 
def argOptions(): 
    parser = argparse.ArgumentParser() 
    parser.add_argument( '-cpp', action='store_true',
                         help='Create a c++ file' )

    parser.add_argument( '-py', action='store_true',
                         help='Create a python file' )


    parser.add_argument( 'flags', nargs='*' )

    args = parser.parse_args() 
    return args 

# Define and write the preamble string 
def fileOptions(args):
    authorName = args.flags[0] 
    fileName   = args.flags[1] 
    projectDef = args.flags[2]
  
    filePreamble = f'Date:   {Date}\n
                     Author: {authorName}\n
                     File:   {fileName}\n
                     Def:    {projectDef}\n\n
                     Author         Date        Revision 
                     ------------------------------------------ \n
                     {authorName}   {Date}      Initial Version '       
                    

    return filePreamble 



# Define the type of file, create and write the preamble string using the proper quotes 
def writeUp(args, filePreamble): 
    if args.cpp: 
        premable = '\endif\n {filePreamble} \n\'\'\'' 

    if args.py: 
        premable = '\'\'\'\n {filePreamble} \n\'\'\'' 
    
    f = open(args.flgas[1], 'w') 
    f.write(preamble) 
    f.close() 

# Call the functions 
if __name__=='__main__':
    args = argOptions() 
    filePreamble = fileOptions(args) 
    writeUp(args, filePreamble) 
    
