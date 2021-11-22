% Perform bucket sorting algorithms.
% 01 November 2021.
% Matlab program for implementation of Bucket Sort.

% Written by Orhan Ozan Yildiz.
function array = bucketsortfunction(array,app)
    global projectspeed
    x = max(array);
    bucket = zeros(1,x+1);
    
    for j = 1:numel(array)
        bucket(array(j)) = bucket(array(j)) + 1;
        pause(projectspeed)
        b=bar(app.UIAxes2,bucket,'FaceColor','flat','EdgeColor',[0 1 0],'LineWidth',1.5);
        b.CData(j,:)=[1 0 0];
        %b.CData(anothercount-1,:)=[1 0 0];
        
        drawnow update
    end
    index = 1;
    for i = 1:x+1
        for j = 1:bucket(i)
            array(index) = i;
            index = index + 1;
            pause(projectspeed)
            b=bar(app.UIAxes2,array,'FaceColor','flat','EdgeColor',[0 1 0],'LineWidth',1.5);
            b.CData(index,:)=[1 0 0];
            b.CData(index+1,:)=[1 0 0];
            %text(app.UIAxes2,1:length(unsortedvariables),unsortedvariables,num2str(unsortedvariables'),'HorizontalAlignment','center','VerticalAlignment','baseline','Color','r','FontWeight','bold')
            drawnow update
        end
    end
end
