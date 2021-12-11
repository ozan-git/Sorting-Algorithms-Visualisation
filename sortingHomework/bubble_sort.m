% Perform bubble sorting algorithms.
% 5 October 2021.

% BUBBLESORT.A/
% (1) for i = 1 to A:length - 1
% (2)   for j = A:length downto i + 1
% (3)       if A[j] < A[j - 1]
% (4)           exchange A[j] with A[j] - 1"
% Matlab program for implementation of Bubble Sort

% Written by Orhan Ozan Yildiz.
function bubble_sort = bubble_sort(array)
    for i=1:length(array)-1
        for j=length(array):-1:i+1
            
            if array(j)>array(j-1)
                key=array(j-1);%saving our number in a constant
                array(j-1)=array(j);%replacing numbers in the array
                array(j)=key;%replacing numbers in the array
            end
        end
    end
    bubble_sort=array;
    
    
    

    
    
