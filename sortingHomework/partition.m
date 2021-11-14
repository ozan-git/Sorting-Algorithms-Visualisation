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
function [i,A] = partition(A,p,r)
    % (1)
    x = A(r);
    % (2)
    i = p-1;
    
    % (3)
    for j = p:r-1
        
        % If current element is smaller than or equal to pivot x.
        % (4)(5)(6)(7)
        if A(j)<=x
            i = i+1;
            a = A(i);
            b = A(j);
            A(i) = b;
            A(j) = a;
        end
    end
    % (8)
    c = A(i+1);
    d = A(r);
    A(i+1) = d;
    A(r) = c;
    % (9)
    i=i+1;
    
end