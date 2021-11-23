function unsortedvariables = merge2(unsortedvariables,low,middle,high,app,~)
    global projectspeed
    pause('on')
    size1 = middle - low + 1;
    size2 = high - middle;
    left = zeros(1,size1+1);
    right = zeros(1,size2+1);
    pause(projectspeed)
    for i=1:size1
        left(i) = unsortedvariables(low+i-1);
    end
    for j=1:size2
        right(j) = unsortedvariables(middle+j);
    end
    left(size1+1) = inf;
    right(size2+1) = inf;
    i = 1;
    j = 1;
    for k=low:high
        
        pause(projectspeed)
        if left(i)<= right(j)
            unsortedvariables(k) = left(i);
            i = i + 1;
            b=bar(app.UIAxesVisualisation,unsortedvariables,'FaceColor','flat','EdgeColor',[0 1 0],'LineWidth',1.5);
            %b.CData(i,:)=[1 0 0];
            b.CData(k,:)=[1 0 0];
            text(app.UIAxesVisualisation,1:length(unsortedvariables),unsortedvariables,num2str(unsortedvariables'),'HorizontalAlignment','center','VerticalAlignment','baseline','Color','r','FontWeight','bold')
            drawnow update
        else
            unsortedvariables(k) = right(j);
            j = j + 1;
            b=bar(app.UIAxesVisualisation,unsortedvariables,'FaceColor','flat','EdgeColor',[0 1 0],'LineWidth',1.5);
            
            b.CData(k,:)=[1 0 0];
            text(app.UIAxesVisualisation,1:length(unsortedvariables),unsortedvariables,num2str(unsortedvariables'),'HorizontalAlignment','center','VerticalAlignment','baseline','Color','r','FontWeight','bold')
            drawnow update
        end
        
    end
end