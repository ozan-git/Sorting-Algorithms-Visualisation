% Performs quick sort algorithm.
% Quick sort algorithm, like merge sort, applies the dive-and-conquer paradigm.
%
% Divide: Partition the array Array[p..r] into two (possibly empty)
% subarrays Array[p..(q-1)] and Array[(q+1)..r]
% such that each element of Array[p..(q-1)] is less than or equal to
% Array[q], which is, in turn, less than or equal to each element of
% Array[(q+1)..r]. Compute the index q as part of this partitioning procedure.
%
% Conquer: Sort the two subarrays Array[p..(q-1)] and Array[(q+1)..r] by
% recursive calls to quicksort.
% Combine: Because the subarrays are already sorted, no work is needed to
% combine them: the entire array Array[p..r]
% is now sorted.
% It was created on October 22, 2021.
% page 170, CLRS
% Written by Orhan Ozan Yildiz.

function [array, comp_quick] = quick(array)
    tic;
    % vectors with one or less elements are sorted
    if numel(array) <= 1
        return
    else
        pivot=array(1);     % Take first value as pivot element
                            % randomization would help avoiding worst case
                            % runtime.
        % We need three partitions in order to make use of Matlabs
        % in-place processing feature.
        array = [ quick( array(array < pivot))...
            array(array == pivot)...
            quick(array(array > pivot)) ];
    end
    comp_quick = toc;
end

