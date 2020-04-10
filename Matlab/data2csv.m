function [] = data2csv(fileName, yourData, cHeader) 
%Def: Creates a .csv file with a header from a matrix data

%Example of how inputs should look like 
%fileName = 'input';
%yourData = rand(3);
%cHeader = {'a' 'b' 'c'}; %header 

commaHeader = [cHeader; repmat({','}, 1, numel(cHeader))]; %add commas 
commaHeader = commaHeader(:)';
textHeader = cell2mat(commaHeader); %cHeader in text with commas 

%write header to file 
fID = fopen(sprintf('%s.csv', fileName), 'w');
fprintf(fID, '%s\n', textHeader);
fclose(fID); 

%write data to end of the file 
dlmwrite(sprintf('%s.csv', fileName), yourData, '-append'); 

end
