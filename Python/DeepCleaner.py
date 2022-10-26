#**************************************************************************************************
# DeepCleaner.py
#
# Author: Peter R. Olejnik
# Write Start Date: 18/05/2022
#
# Objective: Clean out excess Files and folder Recursivly from top directory. Targets LaTeX, 
#            Matlab, Simulink, and Empty Folders
#
#**************************************************************************************************

#**************************************************************************************************
# <Function Name>
#
# Inputs:   1) Top directory to clean out
#
#**************************************************************************************************

import sys
import os
import glob
import send2trash

def RemoveFile(FileOI):
    # print("Deleting: " + FileOI)
    # os.remove(FileOI)
    send2trash.send2trash(FileOI)


folders = []

# r=root, d=directories, f = files
for r, d, f in os.walk(sys.argv[1]):
    for folder in d:
        folders.append(os.path.join(r, folder))

#**************************************************************************************************
# Clean out for Latex
#**************************************************************************************************    

ClearFiles = [".aux",               \
              ".bbl",               \
              ".blg",               \
              ".idx",               \
              ".ind",               \
              ".lof",               \
              ".lot",               \
              ".out",               \
              ".toc",               \
              ".acn",               \
              ".acr",               \
              ".alg",               \
              ".glg",               \
              ".glo",               \
              ".gls",               \
              ".fls",               \
              ".log",               \
              ".fdb_latexmk",       \
              ".snm",               \
              ".synctex(busy)",     \
              ".synctex.gz(busy)",  \
              ".nav" ,              \
              ".synctex.gz" ,       \
              ".tex.backup" ,       \
              ".spl" ,              \
              ".run.xml" ,          \
              "-blx.bib"]      

ClearFolders = ["_minted*"]      

for f in folders:
    fileList = glob.glob(f + "/*.tex")
    for trueFile in fileList:
        DeleteFiles = []
        for CheckFile in ClearFiles:
            if os.path.exists(trueFile[:-4] + CheckFile):
                DeleteFiles.append(trueFile[:-4] + CheckFile)

        for CheckFolder in ClearFolders:
            FolderExist = glob.glob(f + "/" + CheckFolder + "/")
            if FolderExist:
                DeleteFiles.append(FolderExist)
            

        if len(DeleteFiles) != 0:
            print("")
            print(*DeleteFiles, sep = "\n")
            Input = input('Send to trash above? [y/yes to delete, anything else to skip] ')
            if (Input.upper().lower() == 'y') or (Input.upper().lower() == 'yes'):
                for DeleteThis in DeleteFiles:
                    RemoveFile(DeleteThis)

#**************************************************************************************************
# Clean out for "word" docs autosaves
#**************************************************************************************************    

for f in folders:
    DeleteFiles = []
    fileList = glob.glob(f + "/~*")
    for trueFile in fileList:
        DeleteFiles.append(trueFile)
            
    if len(DeleteFiles) != 0:
        print("")
        print(*DeleteFiles, sep = "\n")
        Input = input('Send to trash above? [y/yes to delete, anything else to skip] ')
        if (Input.upper().lower() == 'y') or (Input.upper().lower() == 'yes'):
            for DeleteThis in DeleteFiles:
                    RemoveFile(DeleteThis)

#**************************************************************************************************
# Clean out for Matlab
#**************************************************************************************************    

ClearFiles = [".asv"]        

for f in folders:
    fileList = glob.glob(f + "/*.m")
    for trueFile in fileList:
        DeleteFiles = []
        for CheckFile in ClearFiles:
            if os.path.exists(trueFile[:-2] + CheckFile):
                DeleteFiles.append(trueFile[:-2] + CheckFile)
            
        if len(DeleteFiles) != 0:
            print("")
            print(*DeleteFiles, sep = "\n")
            Input = input('Send to trash above? [y/yes to delete, anything else to skip] ')
            if (Input.upper().lower() == 'y') or (Input.upper().lower() == 'yes'):
                for DeleteThis in DeleteFiles:
                    RemoveFile(DeleteThis)

#**************************************************************************************************
# Clean out for Simulink
#**************************************************************************************************    

ClearFiles = ["_sfun.mexa64"]

ClearFolders = ["slprj" , \
                "*_grt_rtw"]      

for f in folders:
    fileList = glob.glob(f + "/*.slx")
    for trueFile in fileList:
        DeleteFiles = []
        for CheckFile in ClearFiles:
            if os.path.exists(trueFile[:-4] + CheckFile):
                DeleteFiles.append(trueFile[:-4] + CheckFile)

        for CheckFolder in ClearFolders:
            FolderExist = glob.glob(f + "/" + CheckFolder + "/")
            if FolderExist:
                DeleteFiles.append(FolderExist)
            

        if len(DeleteFiles) != 0:
            print("")
            print(*DeleteFiles, sep = "\n")
            Input = input('Send to trash above? [y/yes to delete, anything else to skip] ')
            if (Input.upper().lower() == 'y') or (Input.upper().lower() == 'yes'):
                for DeleteThis in DeleteFiles:
                    RemoveFile(DeleteThis)

#**************************************************************************************************
# Clean out empty folders
#**************************************************************************************************   

DeleteFiles = []
for f in folders:
    if len(os.listdir(f) ) == 0:
        DeleteFiles.append(f)

print("")
print(*DeleteFiles, sep = "\n")
Input = input('Folder above is empty. Send to trash? [y/yes to delete, anything else to skip] ')
if (Input.upper().lower() == 'y') or (Input.upper().lower() == 'yes'):
    RemoveFile(DeleteFiles)

#**************************************************************************************************
# End of File
#**************************************************************************************************