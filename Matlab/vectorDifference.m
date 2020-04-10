function[diffMatrix] = vectorDifference( inputMatrix )
%Def: It only takes the difference between rows in a matrix; 
%          hence the input should be a column matrix 
%usage vectorDifference(inputMatrix)    

diffMatrix = []; 

for i=1:size(inputMatrix,2) 
    initialIteration = [0; inputMatrix(:,i)]; %append a 0 to the begining of the vector 
    finalIteration = [inputMatrix(:,1); 0]; %append a 0 to the end of the vector
    diffPerInteration = abs(initialIteration - finalIteration); %difference between 
																%each iteration 
    diffPerInteration(1) = [ ]; %removes first element 
    diffPerInteration(length(diffPerInteration)) = [ ]; %removes last element 
    diffMatrix(:,i) = diffPerIteration; %populate the difference iteration matrix 
end %for loop 
