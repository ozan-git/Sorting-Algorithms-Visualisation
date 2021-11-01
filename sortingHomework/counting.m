% Perform bucket sorting algorithms.
% 01 November 2021.
% Matlab program for implementation of Counting Sort.

% Written by Orhan Ozan Yildiz.
function array = counting(array)
 
    min_value = min(array);
    max_value = max(array);
 
    count = zeros((max_value-min_value+1),1);
 
    for number = array
        count(number - min_value + 1) = count(number - min_value + 1) + 1;
    end
    
    k = 1;
    for i = (min_value:max_value)     
        while( count(i-min_value +1) > 0)
            array(k) = i;
            k = k+1;
            count(i - min_value + 1) = count(i - min_value + 1) - 1;
        end
    end
 
end 

