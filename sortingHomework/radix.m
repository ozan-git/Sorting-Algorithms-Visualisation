% Perform radix sorting algorithms.
% 01 November 2021.
% Matlab program for implementation of Radix Sort.

% Written by Orhan Ozan Yildiz.
function [array, comp_radix] = radix(array)
    tic;
    max_value = max(array);
    base = 1;
while max_value/base > 0
    array = counting(array,base);
    base = base * 10;
end
    function A = counting(array,base)
        B = zeros(1,11);
        A = zeros(1,numel(array));
        for j = 1:numel(array)
            B(rem(floor(array(j)/base),10)+1) = B(rem(floor(array(j)/base),10)+1) + 1;
        end
        for i = 2:11
            B(i) = B(i) + B(i-1);
        end
        for j = numel(array):-1:1
            A(B(rem(floor(array(j)/base),10)+1)) = array(j);
            B(rem(floor(array(j)/base),10)+1) = B(rem(floor(array(j)/base),10)+1) - 1;
        end
    end
    comp_radix = toc;
end

