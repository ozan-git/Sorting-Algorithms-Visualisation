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
function unsortedvariables = insertionnsortfunction(unsortedvariables)
    
    for count = (2:numel(unsortedvariables))
        
        value = unsortedvariables(count);
        anothercount = count - 1;
        
        while (anothercount >= 1) && (unsortedvariables(anothercount) > value)
            unsortedvariables(anothercount+1) = unsortedvariables(anothercount);
            anothercount = anothercount-1;
        end
        
        unsortedvariables(anothercount+1)= value;
        
    end
end