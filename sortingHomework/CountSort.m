% Perform bucket sorting algorithms.
% 01 November 2021.
% Matlab program for implementation of Counting Sort.

% Written by Orhan Ozan Yildiz.
function sortedArray = CountSort(unsortedvariables,app, ~)
    global projectspeed
    
    pause('on')
    arrayBiggest = max(unsortedvariables);
    thirdArray = zeros(1,arrayBiggest);
    for j = 1:numel(unsortedvariables)
        thirdArray(unsortedvariables(j)) = thirdArray(unsortedvariables(j)) + 1;
    end
    for i = 2:arrayBiggest
        thirdArray(i) = thirdArray(i) + thirdArray(i-1);
    end
    for j = numel(unsortedvariables):-1:1
        
        pause(projectspeed)
        sortedArray(thirdArray(unsortedvariables(j))) = unsortedvariables(j);
        bar(app.UIAxesVisualisation, sortedArray,'FaceColor',[0 .5 .5],'EdgeColor',[0 .9 .9],'LineWidth',1.5)
        
        drawnow update
        thirdArray(unsortedvariables(j)) = thirdArray(unsortedvariables(j)) - 1;
        
    end
    bar(app.UIAxesVisualisation, sortedArray,'FaceColor',[0 .5 .5],'EdgeColor',[0 .9 .9],'LineWidth',1.5)
    
    drawnow update
end
