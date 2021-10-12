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

function [array, comp_merge] = merge_insertion(array,l,r)
% Measure the computational time of the method.
tic;   
if(l<r)
    % Finding the midpoint of the array.
    mid = floor((l+r)/2); 
    array = insertion(array,l,mid);
    array = merge_insertion(array,mid+1,r);
    array = merge_sort(array,l,r,mid);
    comp_merge = toc;
end

function array = merge_sort(array,l,r,mid)
% First half of array.
i = l;
% Second half of array.
j = mid+1;
% Combining the first and last half. 
k = 1;

% Data is copied to temporary arrays.
while i <= mid && j <= r        
        if array(i)<array(j)       
            temp(k) = array(i);
            i = i+1;
            k = k+1;
        else  
            temp(k) = array(j);
            j = j+1;
            k = k+1;
        end   
end

while i <= mid 
    temp(k) = array(i);
    i = i+1;
    k = k+1;
end

while j <= r
    temp(k) = array(j);
    j = j+1;
    k = k+1;
end

array(l:r) = temp(1:k-1);
