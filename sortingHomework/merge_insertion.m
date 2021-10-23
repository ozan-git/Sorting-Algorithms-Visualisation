% Perform merge sorting algorithms.
% 5 October 2021.

% MERGE(A, p, q, r)
% (1) n1 = q - p + 1
% (2) n2 = r - q
% (3) let L[1..n1 +1] and R[1..n2 + 1] be new arrays
% (4) for i = 1 to n1
% (5)   L[i] = A[p + i - 1]
% (6) for j = 1 to n2
% (7)   R[j] = A[q + j]
% (8) L[n1 + 1] = 1
% (9) R[n2 + 1] = 1
% (10) i = 1
% (11) j = 1
% (12) for k = p to r
% (13)  if L[i] <= R[j]
% (14)      A[k] D L[i]
% (15)      i = i + 1
% (16)  else A[k] = R[j]
% (17)      j = j + 1
% Matlab program for implementation of Bubble Sort

% Written by Orhan Ozan Yildiz.

function [array, comp_merge] = merge_insertion(array)
    % Measure the computational time of the method.
    tic;
    length_array = length(array);
    if(length_array < 2)
        return
    end
    
    % Finding the midpoint of the array.
    mid = floor(length_array/2);
    start_half = array(1:mid);
    end_half = array(mid + 1: length(array));
    
    [start_half, ~] = insertion(start_half);
    [end_half, ~] = insertion(end_half);
    
    array = merge_sort(array,start_half,end_half);
    comp_merge = toc;
    
    
function double_list = merge_sort(double_list,start_half,end_half)
    i = 1;
    j = 1;
    k = 1;
    
    length_part_left = length(start_half);
    length_part_right = length(end_half);
    while i <= length_part_left && j <= length_part_right
        if (start_half(i) >= end_half(j))
            double_list(k) = end_half(j);
            k = (k + 1);
            j = (j + 1);
        else
            double_list(k) = start_half(i);
            k = (k + 1);
            i = (i + 1);
        end
    end
    while (i <= length_part_left)
        double_list(k) = start_half(i);
        k = (k + 1);
        i = (i + 1);
    end
    while (j <= length_part_right)
        double_list(k) = end_half(j);
        k = (k + 1);
        j = (j + 1);
    end
    
    