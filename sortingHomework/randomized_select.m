% RANDOMIZED-SELECT(A,p,r,i)
% (1) if p == r
% (2)     return A[p]
% (3) q = RANDOMIZED-PARTITION(A,p,r)
% (4) k = q - p + 1
% (5) if i==k          // the pivot value is the answer
% (6)     return A[q]
% (7) elseif i < k
% (8)     return RANDOMIZED-SELECT(A,p,q-1,i)
% (9) else return RANDOMIZED-SELECT(A,q+1,r,i-k)

% Perform randomized-Select algorithm. The algorithm RANDOMIZED-SELECT
% is modeled after the quicksort algorithm.
% 13 November 2021.

% Written by Orhan Ozan Yildiz.
function [A] = randomized_select(A,p,r,i)
    % (1), (2)
    if p == r
        output = A(p);
        display(output)
    end
    % (3)
    [q,A] = partition(A,p,r);
    % (4)
    k = q-p+1;
    % (5), (6)
    if i==k
        output=A(q);
        display(output)
        % (7)
    elseif i<k
        A=randomized_select(A,p,r,i);
        % (8),(9)
    else
        A=randomized_select(A,q+1,r,i-k);
    end
end

