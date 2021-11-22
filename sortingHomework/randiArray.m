% Perform random array generation according to user decisions.
% 5 October 2021.

% Written by Orhan Ozan Yildiz.
function randomArray = randiArray()
    
    size_array = input('How many numbers should the array consist of: ');
    imin = input('What is the smallest value: ');
    imax = input('What is the largest value: ');
    
    % Generating a random array based on user inputs.
    randomArray =  randi([imin imax],1, size_array);
end