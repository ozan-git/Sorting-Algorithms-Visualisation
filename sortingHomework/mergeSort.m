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
function unsortedvariables = mergeSort(unsortedvariables,low,high,app,event)
    global projectspeed
    
    if(low < high)
        
        pause(projectspeed)
        
        middle = floor((low + high)/2);
        
        unsortedvariables = mergeSort(unsortedvariables,low,middle,app,event);
        
        unsortedvariables = mergeSort(unsortedvariables,middle + 1, high,app,event);
        
        unsortedvariables = merge(unsortedvariables, low, middle, high,app,event);
        
        bar(app.UIAxes2, unsortedvariables,'FaceColor',[0 .5 .5],'EdgeColor',[0 .9 .9],'LineWidth',1.5)
        text(app.UIAxes2,1:length(unsortedvariables),unsortedvariables,num2str(unsortedvariables'),...
            'HorizontalAlignment','center','VerticalAlignment','baseline','Color','r','FontWeight','bold')
        drawnow update
        
    end
end