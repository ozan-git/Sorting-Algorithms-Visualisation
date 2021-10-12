% Perform insertion sorting algorithms.
% 5 October 2021.

% (1) for j = 2 to A.length
% (2)     key = A[j]
% (3)     // Insert A[j] into the sorted sequence A[1..j - 1].
% (4)     i = j - 1
% (5)     while i > 0 and A[i] and A[i] > key
% (6)         A[i + 1] = A[i]
% (7)         i = i - 1
% (8)     A[i + 1] = key
% Matlab program for implementation of Insertion Sort

% Written by Orhan Ozan Yildiz.

function [array, comp_insertion] = insertion(array)
% Measure the computational time of the method.
tic;                  
    arrayLength = size(array,2);
    for i = 2:arrayLength
        key = array(i);
        j = i - 1;

        while j > 0 && array(j) > key
            array(j+1) = array(j);
            j = j - 1;
        end
        array(j + 1) = key;
    end
    comp_insertion = toc;
end