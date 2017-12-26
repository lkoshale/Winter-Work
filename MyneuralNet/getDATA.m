function [X,Y] = getDATA(len,m,right) 

% get DATA for matrix in form of X and Y

carDir = 'motorbikes_side/0';
airDir = 'airplanes_side/0';

% each 200x200 px jpg image has been made into 4000*1 row vector
% and stored in respective matrix of siize where each row is a image
% len = 100*100;
% m = 50;
% right=100;

CAR = uint8(zeros(m,len));
AIR = uint8(zeros(m,len));
wDATA = uint8(zeros(m*2,len+1));
j= 1;
for i = (right+1):(100+m)
     
    k = imread( strcat(carDir,int2str(i),'.jpg' ) );
    
    % Get the number of rows and columns, 
	% and, most importantly, the number of color channels.
    [~, ~, numberOfColorChannels] = size(k);
    if numberOfColorChannels > 1
    % It's a true color RGB image.  We need to convert to gray scale.
        k = rgb2gray(k);
    end
        
    CAR(i-right,:) = k(:)';
    l = rgb2gray(imread(strcat(airDir,int2str(i),'.jpg' ) ));

    % Get the number of rows and columns, 
	% and, most importantly, the number of color channels.
    [~, ~, numberOfColorChannels] = size(l);
    if numberOfColorChannels > 1
    % It's a true color RGB image.  We need to convert to gray scale.
        l = rgb2gray(l);
    end
    
    AIR(i-right,:) = l(:)';
    % 0->BIKE and 1-> AEROPLANE
    wDATA(j,:) = [0,k(:)'];
    wDATA(j+1,:)=[1,l(:)'];
    j=j+2;
end

wDATA = wDATA(randperm( size(wDATA,1)),:);
X = wDATA(:,2:end);
Y = wDATA(:,1:1);
end

