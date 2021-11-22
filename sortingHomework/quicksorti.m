% Performs quick sort algorithm.
% Quick sort algorithm, like merge sort, applies the dive-and-conquer paradigm.
% It was created on October 22, 2021.
% page 170, CLRS
% Written by Orhan Ozan Yildiz.
function [arr] = quicksorti(arr,low,high)
    
    % If last item bigger than first item
    if low < high 
        [arr, pivot] = partition_v2(arr, low, high);    % Call function partition.
        arr = quicksorti(arr,low,pivot - 1);            % Recursive calling the itself.
        arr = quicksorti(arr,pivot + 1,high);           % Recursive calling the itself.
        
    end
end