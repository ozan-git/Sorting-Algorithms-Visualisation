% Performs quick sort algorithm.
% Quick sort algorithm, like merge sort, applies the dive-and-conquer paradigm.
% It was created on October 22, 2021.
% page 170, CLRS
% Written by Orhan Ozan Yildiz.
function unsortedvariables = QuickSort2(unsortedvariables,p,r,app)
    global projectspeed pausevalue
    if p < r
        
        [q,unsortedvariables] = partition2(unsortedvariables,p,r,app);
        unsortedvariables = QuickSort2(unsortedvariables,p,q-1,app);
        unsortedvariables = QuickSort2(unsortedvariables,q+1,r,app);
        pause(projectspeed)
        while pausevalue == true
            
            if app.Button_14.Value==0
                break;
            end
            pause(0.01);
        end
    end
end