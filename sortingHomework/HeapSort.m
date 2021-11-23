% Perform heap sorting algorithms.
% 22 October 2021.
% Matlab program for implementation of Heap Sort.

% Written by Orhan Ozan Yildiz.
function unsorted_variables = HeapSort(unsorted_variables, app, ~)
    global projectspeed
    pause('on')
    function unsorted_variables = shiftDown(unsorted_variables,root,theEnd)
        while (root * 2) <= theEnd
            
            child = root * 2;
            if (child + 1 <= theEnd) && (unsorted_variables(child) < unsorted_variables(child+1))
                child = child + 1;
            end
            
            if unsorted_variables(root) < unsorted_variables(child)
                % Swap.
                unsorted_variables([root child]) = unsorted_variables([child root]);
                root = child;
                pause(projectspeed)
                b = bar(app.UIAxesVisualisation,unsorted_variables,'FaceColor','flat','EdgeColor',[0 1 0],'LineWidth',1.5);
                b.CData(root,:) = [1 0 0];
                b.CData(child,:) = [1 0 0];
                text(app.UIAxesVisualisation,1:length(unsorted_variables),unsorted_variables,num2str(unsorted_variables'),...
                    'HorizontalAlignment','center','VerticalAlignment','baseline','Color','r','FontWeight','bold')
                drawnow update
            else
                return
            end
            
        end %while
    end %siftDown
    
    count = numel(unsorted_variables);
    
    % Because heapify is called once in pseudo-code, it is inline here.
    start = floor(count/2);
    
    while start >= 1
        unsorted_variables = shiftDown(unsorted_variables, start, count);
        start = start - 1;
    end
    %End Heapify.
    
    while count > 1
        
        pause(projectspeed)
        unsorted_variables([count 1]) = unsorted_variables([1 count]); %Swap
        count = count - 1;
        unsorted_variables = shiftDown(unsorted_variables,1,count);
        b = bar(app.UIAxesVisualisation,unsorted_variables,'FaceColor','flat','EdgeColor',[0 1 0],'LineWidth',1.5);
        b.CData(count,:)=[1 0 0];
        text(app.UIAxesVisualisation,1:length(unsorted_variables),unsorted_variables,num2str(unsorted_variables'),...
            'HorizontalAlignment','center','VerticalAlignment','baseline','Color','r','FontWeight','bold')
        drawnow update
    end
end

