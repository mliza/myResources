%function 1d2tData() 

% Path access  
desktopPath = fullfile(getenv('HOME'), 'Desktop'); 
transferPath = fullfile(desktopPath, 'Transfer'); 

% Check if Transfer directory exist and if not make one
if ~exist(transferPath, 'dir') 
    mkdir(transferPath); 
end 

% Transfer data from the Grid to local computer  
system('scp -r mliza@filexfer.hpc.arizona.edu:/home/u22/mliza/Transfer/* $HOME/Desktop/Transfer');

% Add path to all subfolders 
addpath(genpath(transferPath));

%detectImportOptions('Tresult-ener.dat')

%end 
