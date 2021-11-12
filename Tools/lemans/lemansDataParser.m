%{ 
   Date:    06/22/2020
   Author:  Martin E. Liza
   File:    lemansDataParser.m
   Detail:  Parsers the data from LeMaNs/tecPlot output files, and
            returns the data as a structure of matrices. 

   Ex.      [ dataOutStruct ] = lemansDataParser('fileName.dat') 

   Author              Date            Revision
   -------------------------------------------------------------------
   Martin E. Liza      06/03/2020      Initial version
   Martin E. Liza      06/18/2020      Added flags to allow output.plt 
                                       and convergence.plt to work 
   Martin E. Liza      06/20/2020      Added the helper function (dataSplit.m) 
   Martin E. Liza      06/30/2020      Deleted the dataSplit function, and modified 
                                       to work with .dat, after using the python macro 
                                       from tecplot and get rid of dataSplit 
   Martin E. Liza      01/18/2021      Rename the file from dataParser 
                                       to lemansDataParser 
%}

function [ dataOutStruct ] = lemansDataParser( filename )
    inFile = importdata( filename );
    numDataIn = inFile.data; 
    [ rows, columns ] = size( numDataIn );

    % Put all the header in one array  
    for i = 1:length( inFile.textdata ) - 2
        headerMultiple{i} = inFile.textdata{i};
    end 

    % Clean out input data header 
    % Removes the words VARIABLES and = from data file 
    headersIn = erase( convertCharsToStrings(headerMultiple), "VARIABLES" ); 
    headersIn = erase( headersIn, "=" );
    headersIn = erase( headersIn, "ZONE" );

    % Removes the double quotes and spacing after single quote  
    headers = strrep( headersIn, '"', '' );
    headers = strrep( headers, ' ', '' );

    % Remove empty strings from the header 
    if headers(1) == ""
        headers(1) = [];
    end
    if headers(end) == ""
        headers(end) = [];
    end

    % Creates a data structure using header's names
    for i = 1:columns
        headerName = headers(i); 
        dataOutStruct.( headerName ) = [ numDataIn(:,i) ];
    end 
end 
