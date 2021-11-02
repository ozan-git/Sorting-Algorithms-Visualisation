% Perform bucket sorting algorithms.
% 01 November 2021.
% Matlab program for implementation of Bucket Sort.

% Written by Orhan Ozan Yildiz.
function [array, comp_bucket] = bucket(array)
    tic;
    % (1) (2) Find maximum value in the list and use length of the list to determine which value in the
	% list goes into which bucket.
    A = max(array);
    bucket = zeros(1,A+1);
    
    for j = 1:numel(array)
        bucket(array(j)) = bucket(array(j)) + 1;
    end
    
    index = 1;
    for i = 1:A+1
        for j = 1:bucket(i)
            array(index) = i;
            index = index + 1;
        end
    end
    comp_bucket = toc;
end

