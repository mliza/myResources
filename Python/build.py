#!/usr/local/bin/python3.7
"""
   Date:    10/20/2019 
   Author:  Martin E. Liza 
   File:    build.py 
   Def:     Allows to compile C++, LaTeX, C and Fortran 
            codes by specifying the proper flags 
      
   Available flags: 
   -tex = LaTeX compiler 
   -cpp = C++ compiler 
   -c   = C compiler 
   -f   = Fortran compiler 

   ex: ./build -flag myCode.*
        

   Author             Date           Revision  
   --------------------------------------------------
   Martin E. Liza     10/20/2019     Initial Version  
""" 

import argparse 
import subprocess 

#Ex. build -cpp "myFile.cpp myFile.hpp"
#NOTE: Requires, g++-9, pdflatex, gcc-9 and gfortran-9  

#Available compilers  
cppCopiler = 'g++-9 -std=c++17' 
texCopiler = 'pdflatex' 
cCopiler = 'gcc-9' 
fCopiler = 'gfortran-9' 

#Make parser object
parser = argparse.ArgumentParser() 

#Compiler selection flags 
parser.add_argument('-cpp', action='store_true', 
                             help='C++ compiler')

parser.add_argument('-tex', action='store_true',
                           help='LaTeX compiler') 

parser.add_argument('-c', action='store_true',
                             help='C compiler')

parser.add_argument('-f', action='store_true',
                       help='Fortran compiler')
#Add specific compiler arguments in quotes   
parser.add_argument('flags', nargs='*' )

#Needed for if statements and for building shell command   
args = parser.parse_args()
flags = (','.join(args.flags))  
flags = flags.replace(',', ' ') 

#Running commands 
if args.cpp: 
    cmd = f'{cppCopiler} {flags}'
if args.tex: 
    cmd = f'{texCopiler} {flags}' 
if args.c: 
    cmd = f'{cCopiler} {flags}'
if args.f: 
    cmd = f'{fCopiler} {flags}' 

#Running Shell 
subprocess.call([cmd], shell=True) 
