#!/usr/local/bin/python3
"""
   Date:    02/15/2021 
   Author:  Martin E. Liza 
   File:    bibTex.py 
   Def:     Allows to compile LaTeX files with bibliographies 
      

   ex: ./bibTex *.tex 
        

   Author             Date           Revision  
   --------------------------------------------------
   Martin E. Liza     12/15/2021     Initial Version  
""" 

import subprocess 
import sys 

commands = [
            ['pdflatex', sys.argv[1] + '.tex'], 
            ['bibtex', sys.argv[1] + '.aux'], 
            ['pdflatex', sys.argv[1] + '.tex'], 
            ['pdflatex', sys.argv[1] + '.tex']
] 

for c in commands: 
    subprocess.call(c) 
