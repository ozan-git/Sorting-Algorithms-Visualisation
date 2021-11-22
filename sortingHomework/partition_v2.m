%The key to the algorithm is the PARTITION procedure, which rearranges
%the subarray A[p....r] in place.
%PARTITION(A, p, r)
% (1) x = A[r]
% (2) i = p - 1
% (3) for j = p to r - 1
% (4)     if A[j] <= x
% (5)         i = i + 1
% (6)         exchange A[i] with A[j]
% (7) exchange A[i + 1] with A[r]
% (8) return i + 1

% It was created on November 13, 2021.
% Written by Orhan Ozan Yildiz.
function [arr, i ] = partition_v2(arr, low, high)
    
    pivot = arr(high); %pivot is last of the array
    
    i = low -1;
    for j = low:high-1
        % If pivot bigger than array's j item.
        if arr(j)<=pivot
            i = i+1;            % 'i' is increased by 1.
            % If i is not equal j.
            if i~=j 
                key = arr(i);   % Swap arr(i) and arr(j).
                arr(i) = arr(j);
                arr(j) = key;
            end
        end
    end
    i = i+1;                    % 'i' is increased by 1/
    key = arr(i);               % Swap arr(i) and arr(high).
    arr(i) = arr(high);
    arr(high) = key;
end