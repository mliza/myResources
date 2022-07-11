#!/opt/homebrew/bin/python3
"""
    Date:    07/11/2022 
    Author:  Martin E. Liza 
    File:    latexProject.py 
    Def:     creates a latex project using 
             pre defined flags/imports
        
    Available flags: 
    -notes    = class notes project  
    -homework = homework project 
    -beamer   = beamer presentation project 
    -cheat    = cheat sheet project 

    ex: ./latexPoject.py 'projectFolderName' 'mainFileName'


    Author             Date           Revision  
    --------------------------------------------------
    Martin E. Liza     10/20/2019     Initial Version  
    Martin E. Liza     10/22/2019     Implemented Dictionaries in the code 
    Martin E. Liza     02/27/2020     Added cheat sheet option
    Martin E. Liza     06/23/2020     Modified beamer write up, added \TitlePage 
    Martin E. Liza     01/20/2020     Make a folder 'codes' in the project directory  
                                      added codeMacros to the preamble  
    Martin E. Liza     07/11/2022     Added draft watermark and bibliography as comments
                                      to homework flag.
""" 
import os
import subprocess 
import argparse 
import shutil 

# Creates an object (ags) w/ the inputs 
def argOptions():
    parser = argparse.ArgumentParser() #creates a parser obj  
    # Available projects 
    parser.add_argument('-notes', action='store_true',
                 help='class notes project')
    parser.add_argument('-homework', action='store_true',
                 help='homework project')
    parser.add_argument('-beamer', action='store_true',
                 help='beamer presentation project')
    parser.add_argument('-cheat', action='store_true',
                 help='cheat sheet project')
    # Add project arguments  
    parser.add_argument('flags', nargs='*')
    args = parser.parse_args() 

    return args 


# Get latex's paths and return them   
def getPaths(): 
    scriptsPath = os.path.abspath(os.path.join(__file__,"../../"))
    latexPath   = os.path.join(scriptsPath, 'Latex')               
    paths = {} 
    for keyName in ['templates', 'macros', 'images']:
        paths[keyName] = os.path.join(latexPath, keyName)

    return paths 


# Builds preamble and body to be written on the .txt files  
def preambleStr(args, paths): 
    # Define dictionaries 
    macros = {} 
    for macroName in ['equationMacros', 'mathMacros', 'pictureMacros', 'beamerMacros', 'codeMacros']:  
       macros[macroName] = os.path.join(paths['macros'], macroName) 

    templates = {}
    for tempName in ['notesTemplate', 'homeworkTemplate', 'beamerTemplate', 'cheatTemplate']:
        templates[tempName] = os.path.join(paths['templates'], tempName) 

    if args.notes: 
        title = '\\title{Class Name Title, [AME 634A]}\n\\author{Martin E. Liza}\n\date{Spring Semester,2020}' 
        preamble = f'\input{{{templates["notesTemplate"]}}}\n\input{{{macros["equationMacros"]}}}\n\input{{{macros["mathMacros"]}}}\n\input{{{macros["pictureMacros"]}}}\n\input{{{macros["codeMacros"]}}}\n{title}'
        body = '\n\n\\begin{document}\n\t\\maketitle\n\t\\tableofcontents\n\n\t% Classes\n\t\\input{lectures/class1}\n\end{document}'  

    if args.homework: 
        header = '\Header{\\today}{Document Name}{My Name}\n%\\usepackage[backend=biber, sorting=none]{biblatex}\n%\\addbibresource{bibliography.bib}\n%\\usepackage[text=Draft, colorspec=0.92, fontsize=7cm]{draftwatermark}'   
        preamble = f'\input{{{templates["homeworkTemplate"]}}}\n\input{{{macros["equationMacros"]}}}\n\input{{{macros["mathMacros"]}}}\n\input{{{macros["pictureMacros"]}}}\n\input{{{macros["codeMacros"]}}}\n{header}'
        body = '\n\n\\begin{document}\n%\printbibliography[heading=none]\n\end{document}' 

    if args.beamer: 
        header = '\\usetheme{UoA}\n\TitlePage{title}{author}{\\today}'   
        preamble = f'\input{{{templates["beamerTemplate"]}}}\n\input{{{macros["equationMacros"]}}}\n\input{{{macros["mathMacros"]}}}\n\input{{{macros["beamerMacros"]}}}\n\input{{{macros["codeMacros"]}}}\n{header}'
        body = '\n\n\\begin{document}\n\n\end{document}' 

    if args.cheat: 
        header = '\\title{Class Name}'   
        multicol = '\t\\begin{multicols}{3}\n\t\setlength{\premulticols}{1pt}\n\t\setlength{\postmulticols}{1pt}\n\t\setlength{\multicolsep}{1pt}\n\t\setlength{\columnsep}{2pt}\n\n\n\t\end{multicols}'
        preamble = f'\input{{{templates["cheatTemplate"]}}}\n\input{{{macros["equationMacros"]}}}\n\input{{{macros["mathMacros"]}}}\n{header}'
        body1 = '\n\n\\begin{document}\n\t\\raggedright\n\t\\footnotesize\n\t\\begin{center}\n\t\t\Large{\\textbf{}}\n\t\end{center}'  
        end = '\end{document}'
        body = f'{body1}\n\n{multicol}\n{end}'

    return preamble, body  


# Creates folders, subfolders and writes the .tex files 
def writeUp(args, preamble, body, paths): 
    folderName = args.flags[0] 
    fileName = args.flags[1]
    os.mkdir(folderName) 
    os.mkdir(os.path.join(folderName, 'figures'))
    os.mkdir(os.path.join(folderName, 'codes'))
    filePath = os.path.join(folderName, f'{fileName}.tex') 
    f = open(filePath, 'w') 
    f.write(preamble) 
    f.write(body) 
    f.close() 
    shutil.copy2(os.path.join(paths['images'], 'missing.png'), os.path.join(folderName, 'figures')) 
        
    # subfolder from classNotes imports 
    if args.notes: 
        os.mkdir(os.path.join(folderName, 'lectures'))
        classPath = os.path.join(os.path.join(folderName, 'lectures'), 'class1.tex') 
        f = open(classPath, 'w')
        f.write('\chapter{Class Title}\n\section{section one}')
        f.close() 
    shellCMD = f'vim {filePath}'
    subprocess.call([shellCMD], shell=True) 


# Calling functions 
if __name__ == "__main__":
    args = argOptions() 
    path = getPaths() 
    string = preambleStr(args, paths=path)
    writeUp(args, preamble=string[0], body=string[1], paths=path) 

