% Perform bucket sorting algorithms.
% 01 November 2021.
% Matlab program for implementation of Bucket Sort.

% Written by Orhan Ozan Yildiz.
function array = bucket_sort(array)
    %% Constants
    max_array = max(array); %find max array
    bucket = zeros(1,max_array+1); %create bucket
    %% For Loop
    for j = 1:numel(array)
        bucket(array(j)) = bucket(array(j)) + 1;
    end
    index = 1;
    for i = 1:max_array+1
        for j = 1:bucket(i)
            array(index) = i;
            index = index + 1;
        end
    end
end
