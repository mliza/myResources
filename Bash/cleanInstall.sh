#!/usr/local/bin/bash

#run using sudo 

#Clean install packages for Mac 
echo "Check for Xcode" 
if test ! $(xcode-select -p); then 
	echo "Please install Xcode " 
	exit 
fi 

#Testing for homebrew installation 
if test ! $(which brew); then 
    echo "Installing Homebrew" 
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
fi 

#GNU core packages  
GNU=(
	coreutils #core utilities 
	gnu-sed   #sed 
	gnu-tar   #tar 
	gnu-which #which 
	findutils #find utilities 
)


#Homebrew packages to be install 
BREWPACKAGES=(
	python		    #install python 
	bash			#install bash 
    egrep       	#better than grep 
    htop        	#better than top 
    tldr        	#man examples 
    ccat        	#better than cat 
    ansiweather 	#weather app
    whereami    	#location 
    cask        	#package manager 
    git         	#installing git 
    dos2unix    	#converts dos files 
    vim         	#better vim 
	gdb				#C++ debugger 
	gcc				#C compiler 
    tree        	#tree application 
	qrecode 		#creates QR codes 
	mas				#install apps from the applestore 
	wifi-password   #display wifi password 
	speedtest-cli   #internet connection test 
	whereami 	    #location 
    ipython         #ipython
    thefuck         #installing thefuck 
    jp2a            #convert jpg to ascii
)


#Homebrew cask packages 
BREWCASK=(
	mactex-no-gui 	#mactex
	texmaker		#texmaker
	corelocationcli #better than whereami 
	iterm2			#better than terminal
    xquartz         #needed for X11 
)


#Python packages to be install  
PYTHONPACKAGES=(
	numpy 	    #dimensional array package 
	scipy 		#mathematics, science and engineering package
	matplotlib  #2D plotting package 
	sympy 		#symbolic mathematics package 
	pandas      #data structure & analysis package 
	pytecplot 	#python tecplot  
    schedule    #allows you to schedule jobs at specific time  
    virtualenv  #create isolated python environments
    ipython     #ipython 
)


echo "Installing GNU core utilities" 
brew install ${GNU[@]}

echo "Installing homebrew packages"
brew install ${BREWPACKAGES[@]}

echo "Installing casks" 
brew cask install ${BREWCASK[@]} 

echo "Installing python packages" 
python3.7 -m pip install ${PYTHONPACKAGES[@]}

echo "Modifying OSX properties" 
#Prevent apps from staying in dock after quitting 
defaults write com.apple.dock show-recents -bool no 
defaults write com.apple.dock recent-apps -array 
#Remove auto-hide dock delay 
defaults write com.apple.dock autohide-delay -float 0 && killall Dock
#Display extensions in finder 
defaults write NSGlobalDomain AppleShowAllExtensions -bool true && killall Finder 
#Exit Finder
defaults write com.apple.finder QuitMenuItem -bool true && killall Finder
#Allows to link all homebrew package
sudo install -d -o ${whoami} -g admin /usr/local/Frameworks


echo "installation complete!"  
