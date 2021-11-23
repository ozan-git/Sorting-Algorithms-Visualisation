% Perform radix sorting algorithms.
% 01 November 2021.
% Matlab program for implementation of Radix Sort.

% Written by Orhan Ozan Yildiz.
function unsortedvariables = radixsortfunction(unsortedvariables,app)
    global projectspeed
    lesssignificant = max(unsortedvariables);
    base = 1;
    while lesssignificant/base > 1
        unsortedvariables = counting_sort(unsortedvariables,base,app);
        base = base * 10;
    end
    function B = counting_sort(unsortedvariables,base,app)
        
        C = zeros(1,11);
        B = zeros(1,numel(unsortedvariables));
        for j = 1:numel(unsortedvariables)
            C(rem(floor(unsortedvariables(j)/base),10)+1) = C(rem(floor(unsortedvariables(j)/base),10)+1) + 1;
            
        end
        for i = 2:11
            C(i) = C(i) + C(i-1);
        end
        for j = length(unsortedvariables):-1:1
            B(C(rem(floor(unsortedvariables(j)/base),10)+1)) = unsortedvariables(j);
            C(rem(floor(unsortedvariables(j)/base),10)+1) = C(rem(floor(unsortedvariables(j)/base),10)+1) - 1;
            
            pause(projectspeed)
            bar(app.UIAxesVisualisation, unsortedvariables,'FaceColor',[0 .5 .5],'EdgeColor',[0 .9 .9],'LineWidth',1.5)
            text(app.UIAxesVisualisation,1:length(unsortedvariables),unsortedvariables,num2str(unsortedvariables'),...
                'HorizontalAlignment','center','VerticalAlignment','baseline','Color','r','FontWeight','bold')
            drawnow update
        end
    end
end