function [c,unsortedvariables] = partition2(unsortedvariables,p,q,app)
    global projectspeed pausevalue
    x = unsortedvariables(p);
    i = p;
    for j = p+1:q
        
        if unsortedvariables(j) <= x
            i = i+1;
            key = unsortedvariables(i);
            unsortedvariables(i) = unsortedvariables(j);
            unsortedvariables(j) = key;
            pause(projectspeed)
            while pausevalue == true
                if app.Button_14.Value == 0
                    break;
                end
                
                pause(0.01);
            end
            b = bar(app.UIAxesVisualisation,unsortedvariables,'FaceColor','flat','EdgeColor',[0 1 0],'LineWidth',1.5);
            b.CData(i,:) = [1 0 0];
            b.CData(j,:) = [1 0 0];
            text(app.UIAxesVisualisation,1:length(unsortedvariables),unsortedvariables,num2str(unsortedvariables'),...
                'HorizontalAlignment','center','VerticalAlignment','baseline','Color','r','FontWeight','bold')
            drawnow update
        end
    end
    
    key = unsortedvariables(p);
    unsortedvariables(p) = unsortedvariables(i);
    unsortedvariables(i) = key ;
    c = i;
    pause(projectspeed)
    while pausevalue == true
        if app.Button_14.Value == 0
            break;
        end
        
        pause(0.01);
    end
    b = bar(app.UIAxesVisualisation,unsortedvariables,'FaceColor','flat','EdgeColor',[0 1 0],'LineWidth',1.5);
    b.CData(p,:) = [1 0 0];
    b.CData(i,:) = [1 0 0];
    text(app.UIAxesVisualisation,1:length(unsortedvariables),unsortedvariables,num2str(unsortedvariables'),...
        'HorizontalAlignment','center','VerticalAlignment','baseline','Color','r','FontWeight','bold')
    drawnow update
end

