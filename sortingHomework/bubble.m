% Perform bubble sorting algorithms.
% 5 October 2021.

% BUBBLESORT.A/
% (1) for i = 1 to A:length - 1
% (2)   for j = A:length downto i + 1
% (3)       if A[j] < A[j - 1]
% (4)           exchange A[j] with A[j] - 1"
% Matlab program for implementation of Bubble Sort

% Written by Orhan Ozan Yildiz.

function [array, comp_bubble] = bubble(array)
    % Measure the computational time of the method.
    tic;
    arrayLength = size(array,2);
    
    for i = 1: (arrayLength+1)
        for j = arrayLength:-1:(i + 1)
            
            if array(j) < array(j - 1)
                
                temp = array(j);
                array(j) = array(j - 1);
                array(j-1) = temp;
            end
        end
    end
    comp_bubble = toc;
end