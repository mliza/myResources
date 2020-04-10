function dataParser(myDat) 
    % Def: This function parses a .xlsm file into cells  
    %       look for the row number in which index -1 
    %       is repeated on column 1 and parses the rest 
    %       of the columns at this specific index 

    data = readtable(myDat); %Import data as a table  
    data = table2array(data); %Convert table to a matrix 
    [row, column] = size(data); %Matrixsize 
    dataLimit = find(data(:,1)==-1); %find row number where data is -1 
    dataLimit = [1, dataLimit']; %for looping Purpose  

    for colIndx = 2:column %This is a check for data longer than 3 columns 
        colParsing = data(:,colIndx); %Select the column to be parse         
        matrixCol = sprintf('myMatrix%s', num2str(colIndx(1))); 
        varName = genvarname(matrixCol(1:length(matrixCol)));

        for indx = 2:length(dataLimit)
            dataParse = colParsing(dataLimit(indx-1):dataLimit(indx));
            storageData{(indx-1)} = dataParse;
        end %end indx  
       
        eval([varName '= storageData']);
    end %end colIndx  
    keyboard 

    %example to generate plots 
    %num = the number of data you want to plot 
    %plot(cell2mat(myMatrix2(num)), cell2mat(myMatrix3(num)))
    %xlabel('Temperature [\circ K]') 
    %ylabel('Heat Capacity [J/(molK)]') 
    %grid on 

end %end function 

