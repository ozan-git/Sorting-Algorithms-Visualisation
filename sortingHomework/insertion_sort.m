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
function insertion_sort = insertion_sort(array)
    for j=2:length(array)
        
        % Save A[j] element to a temporary constant.
        key = array(j);
        
        i = j-1;
        % Move the elements of array A if
        % it is greater than key.
        while i > 0 && array(i) > key
            array(i+1) = array(i);
            i = i-1;
            array(i+1) = key;
        end
    end
    insertion_sort = array;