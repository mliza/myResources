#!/usr/local/bin/bash

# Author: Martin E. Liza 
# Date:   10/26/2019
# File:   sendEmailSetup.sh 
# Def:    This script checks for homebrew and installs it if missing; 
#         it install python3.7 using homebrew and installs python packages "smtplib"
#         and "schedule" using pip. Lastly it adds some aliases to the end of 
#         your bashrc 

# Check for homebrew and install if missing 
if test ! $(which brew); then 
    echo "Installing Homebrew" 
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 
fi 

echo "Installing python3.7" 
brew install python 

echo "Installing python packages" 
python3.7 -m pip install smtplib 
python3.7 -m pip install schedule  

echo "Modifying .bashrc" 
echo "alias python='python3.7' #python3.7 alias"  >> $HOME/.bashrc 
echo "alias pyInstall='python3.7 -m pip install' #install python packages" >> $HOME/.bashrc 
echo "export EMAIL_USER='myEmail@gmail.com' #gmail address use to to send emails using senEmail.py" >> $HOME/.bashrc  
echo "export EMAIL_PASS='myPassword' #gmail password" >> $HOME/.bashrc 
