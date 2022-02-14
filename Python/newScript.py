#!/opt/homebrew/bin/python3
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

    ex: ./newScript.py -flag 'fileName' 'authorName' 


    Author             Date           Revision  
    ------------------------------------------------------------
    Martin E. Liza     03/16/2021     Initial version.  
    Martin E. Liza     07/09/2021     Switch the arg.parser order
                                      and fixed the long string. 
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
    authorName = args.flags[1] 
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
    fileName   = args.flags[0] + extension
    tab        = '    '
        
    # Write file preamble     
    preamble1    = (f'{tab}Date:   {date}\n' 
                    f'{tab}Author: {authorName}\n' 
                    f'{tab}File:   {fileName}\n' 
                    f'{tab}Def:')
    preamble2    = f'{tab}Author\t\tDate\t\tRevision' 
    preamble3    = f'{tab}----------------------------------------------------' 
    preamble4    = f'{tab}{authorName}\t{date}\tInitial version.' 
    filePreamble = f'{preamble1}\n\n{preamble2}\n{preamble3}\n{preamble4}' 

    return filePreamble, fileName 



# Define the type of file, create and write the preamble string using the proper quotes 
def writeUp(args, filePreamble, fileName): 
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
   
    f = open(fileName, 'w') 
    f.write(preamble) 
    f.close() 

# Call the functions 
if __name__=='__main__':
    args = argOptions() 
    filePreamble, fileName = fileOptions(args) 
    writeUp(args, filePreamble, fileName) 
    
