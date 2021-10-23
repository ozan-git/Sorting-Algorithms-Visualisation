% Perform heap sorting algorithms.
% 22 October 2021.
% Matlab program for implementation of Heap Sort.

% Written by Orhan Ozan Yildiz.

% HeapSort(A)
% (1) Build-Max-Heap(A)
% (2) for i = A.length downto 2
% (3)     exchange A[1] with A[i]
% (4)     A.heap-size = A.heap-size - 1
% (5)     Max-Heapify(A,size_heap,1)
function [array, comp_heap] = heap(array)
    tic;
    len_array = length(array);
    array = build_max_heap(array,len_array);
    
    size = len_array;
    for i = len_array:-1:2
        array = swap(array,1,i);
        size = size - 1;
        array = heapify(array,1,size);
    end
    comp_heap = toc;
end

% Build-Max-Heap(A)
% (1) A.heap-size = A.length
% (2) for i = ⌊A.length/2⌋ down to 1
% (3)     Max-Heapify(A,i)
function array = build_max_heap(array,len_array)
    for i = floor(len_array / 2):-1:1
        array = heapify(array,i,len_array);
    end
end

% Max-Heapify(A,i)
% (1) l = LEFT(i)
% (2) r = RIGHT(i)
% (3) if l <= A.heap-size and A[l] > A[i]
% (4)     largest = l
% (5) else largest = i
% (6) if r <= A.heap-size and A[r] > A[largest]
% (7)     largest = r
% (8) if largest != i
% (9)     exchange A[i] with A[largest]
% (10)    Max-Heapify(A, largest)
function array = heapify(array,i,len_array)
    left = 2 * i;
    right = left + 1;
    
    if ((left <= len_array) && (array(left) > array(i)))
        largest = left;
    else
        largest = i;
    end
    if ((right <= len_array) && (array(right) > array(largest)))
        largest = right;
    end
    if (largest ~= i)
        array = swap(array,i,largest);
        array = heapify(array,largest,len_array);
    end
end

% Swap(A,i,j)
% Swap index values of array.
function array = swap(array,i,j)
    value = array(i);
    array(i) = array(j);
    array(j) = value;
end