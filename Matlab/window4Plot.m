function window4Plot(myMatrix, plotTitle, subTitle, xAxis, yAxis, folderPath) 

% Makes a plot with 4 figures 
% myMatrix = matrix with 5 columns, column one is the x-axis; 
%	     columns 2,3,4 and 5 are y axis 
% plotTitle = string, is the figure title and the name of the file 
% subTitle = string, title of each plot 
% xAxis = string, x-label 
% yAxis = string, y-label 
% folderPath = string, path where figure will be save


format long 
% Check optional path 
if ~exist('folderPath', 'var') 
	folderPath = pwd; 
end %end existence of optional variable 


% Loop that generates all the plots 
figure('NumberTitle', 'off', 'Name', sprintf('%s', plotTitle)) 
for indx=1:4
	subplot(2,2,indx)
	plot(myMatrix(:,1), myMatrix(:,indx+1), '-') 
	title(sprintf('%s, %s', subTitle, num2str(indx)))
	xlabel(sprintf('%s', xAxis)) 
	ylabel(sprintf('%s', yAxis))
end %end plots loop  

%Save all the plots 
saveas(gcf, fullfile(folderPath, sprintf('/%s.png', plotTitle))); 

clear all;

end %end window4Plot 
