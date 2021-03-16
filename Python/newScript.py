#!/usr/local/bin/python3.9
import argparse 
import subprocess 
import datetime 
import IPython 

"""
    Date:    03/16/2021 
    Author:  Martin E. Liza 
    File:    newScript.py 
    Def:     creates a new script with preambles  
        
    Available flags: 
    -cpp    = cpp files  
    -py     = python scripts 
    -sh     = bash files 
    -m      = matlab files 

    ex: ./newScript.py -flag 'authorName' 'fileName'


    Author             Date           Revision  
    --------------------------------------------------
    Martin E. Liza     03/16/2019     Initial Version  
""" 
# Available options 
def argOptions(): 
    parser = argparse.ArgumentParser() 
    parser.add_argument( '-cpp', action='store_true',
                         help='Create a c++ file' )

    parser.add_argument( '-py', action='store_true',
                         help='Create a python file' )

    parser.add_argument( '-sh', action='store_true',
                         help='Create a bash file' )
                
    parser.add_argument( '-m', action='store_true',
                         help='Create a matlab file' )

    parser.add_argument( 'flags', nargs='*' )

    args = parser.parse_args() 
    return args 

# Define and write the preamble string 
def fileOptions(args):
    authorName = args.flags[0] 
    date = datetime.datetime.now().strftime("%m/%d/%Y")

    # Add the file extension 
    if args.cpp: 
        extension  = '.cpp'
    if args.py:
        extension  = '.py'
    if args.sh:
        extension  = '.sh'
    if args.m:
        extension  = '.m'

    # Add the file extension and tab before printing the information  
    fileName   = args.flags[1] + extension
    tab        = '    '
        
    # Write file preamble     
    filePreamble = f'{tab}Date:   {date}\n{tab}Author: {authorName}\n{tab}File:   {fileName}\n{tab}Def:               \n\n{tab}Author         Date        Revision\n{tab}------------------------------------------ \n{tab}{authorName}   {date}      Initial Version'       
                    
    return filePreamble 



# Define the type of file, create and write the preamble string using the proper quotes 
def writeUp(args, filePreamble): 
    if args.cpp: 
        preamble   = f'/*\n{filePreamble}\n*/' 
        extension  = '.cpp'

    if args.py: 
        program    = subprocess.check_output(["which", "python3.9"]).decode("utf-8") 
        preamble   = f'#!{program}\'\'\'\n{filePreamble}\n\'\'\'' 
        extension  = '.py'
    
    if args.sh: 
        program    = subprocess.check_output(["which", "bash"]).decode("utf-8") 
        preamble   = f'#!{program}: \'\n{filePreamble}\n\'' 
        extension  = '.sh'

    if args.m: 
        preamble   = f'%{{\n{filePreamble}\n%}}' 
        extension  = '.m'
   
    f = open( args.flags[1]+extension, 'w') 
    f.write(preamble) 
    f.close() 

# Call the functions 
if __name__=='__main__':
    args = argOptions() 
    filePreamble = fileOptions(args) 
    writeUp(args, filePreamble) 
    
