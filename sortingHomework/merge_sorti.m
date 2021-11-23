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

function array = merge_sorti(array)
    array = mergesort(array,1,length(array));
end

% Dividing the list into 2 halfes.
function array = mergesort(array,first,last)
    if first < last
        % Calculate middle index.
        mid = floor((first + last)/2);
        array = mergesort(array,first,mid);
        array = mergesort(array,mid + 1,last);
        % Combining sorted lists.
        array = merge(array,first,mid,last);
    end
end

function array = merge(array, first, mid, last)
    n1 = mid - first + 1;
    n2 = last - mid;
    L = zeros(1, n1+1); % Left side of list.
    R = zeros(1, n2+1); % Right side of list.
    for i=1:n1
        L(i) = array(first+ i - 1);
    end
    for j=1:n2
        R(j) = array(mid+j);
    end
    L(n1+1) = inf;      % Adding the last index infinite number.
    R(n2+1) = inf;      % Adding the last index infinite number.
    i=1;
    j=1;
    
    for k=first:last
        
        if L(i)<=R(j)   % Comparison between righ and left side of lists and
                        % ordering them.
            array(k)=L(i);
            i=i+1;
        else
            array(k)=R(j);
            j=j+1;
        end
    end
end
