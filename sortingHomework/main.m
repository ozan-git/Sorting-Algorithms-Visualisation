% Perform insertion, bubble and merge sorting algorithms.
% 5 October 2021.

% Written by Orhan Ozan Yildiz.

flag = true;
while flag
    %% Where the user is expected to decide how to enter the array of numbers.
    disp('Press 1 if you want to use a random array,')
    disp('press 2 if you want to decide the array, and')
    disp('press 3 if you want to compare sorting algorithms')
    disp('press 4 if you want to exit.')
    chosenInput = input('please select one: ');
    
    %% Controller section. Arrays are sorted according to the decision made by the user.
    if chosenInput == 1
        % The user has to decide the range of the array.
        array = randiArray();
        disp(array)
        
        % Calling sorting functions.
        callingSorting(array)
        
    elseif chosenInput == 2
        % The user creates the array.
        userArray = input('Please enter numbers using commas i.e [k,w,x,y,z]: ');
        disp(userArray)
        
        % Calling sorting functions.
        callingSorting(userArray)
    elseif chosenInput == 3
        
        elements = {};
        
        times_insertion = {};
        times_merge = {};
        times_merge_insert = {};
        times_bubble = {};
        for i = 1:10
            % Generate some integers.
            arr = randi([0,10000*i], 1000*i);
            
            elements = [elements, length(arr)];
            % For insertion sorting.
            [insertion_sorting, ins_comp_time] = insertion(arr);
            disp([length(arr), " Elements Sorted by InsertionSort in ", ins_comp_time])
            times_insertion = [times_insertion, ins_comp_time];
            
            % For bubble sorting.
            [bubble_sorting, bub_comp_time] = bubble(arr);
            disp([length(arr), " Elements Sorted by BubbleSort in ", bub_comp_time])
            times_bubble = [times_bubble, bub_comp_time];
            
            % For merge sorting.
            [merge_sorting, merg_comp_time] = merge(arr,1,length(arr));
            disp([length(arr), " Elements Sorted by MergeSort in ", merg_comp_time])
            times_merge = [times_merge, merg_comp_time];
        end
     
        plot(str2double(elements),str2double(times_insertion), 'b-','LineWidth', 2)
        plot(str2double(elements),str2double(times_bubble),'b-','LineWidth', 2)
        plot(str2double(elements),str2double(times_merge),'b-','LineWidth', 2)

        title('2-D Line Plot for Comparasion Sorting Algorithms')
        xlabel('computational time')
        ylabel('Length of array')
    elseif chosenInput == 4
        flag = false;
        break;
    else
        disp('This input not valid. Please try again.')
        break;
    end    
end

function callingSorting(array)
        % Calling sorting functions.
        [insertion_sorting, ins_comp_time] = insertion(array);
        disp('Insertion sort result: ');
        disp(insertion_sorting)
        
        [bubble_sorting, bub_comp_time] = bubble(array);
        disp('Bubble sort result: ');
        disp(bubble_sorting)
        
        [merge_sorting, merg_comp_time] = merge(array,1,length(array));
        disp('Merge sort result: ');
        disp(merge_sorting)
        
        fprintf('insertion sort computational time is %.4f \n',ins_comp_time)
        fprintf('bubble sort computational time is %.4f \n',bub_comp_time)
        fprintf('merge sort computational time is %.4f \n',merg_comp_time)
end