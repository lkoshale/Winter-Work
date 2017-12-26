%% Manage the Train Data

% command to resize bulk images
% mogrify -resize 100x100\! -quality 100 *.jpg

Tlen = 100*100;
m = 50;
right = 100;

[X,Y] = getDATA(Tlen,m,right);
X = double(X);
Y = double(Y);

save('X.mat','X');

%% Logistic Regression

% DATA has 10000 variable x1...x40000 as pixels
% need 40001 Theta theta0...theta40000
lrX = [ones(size(X,1),1),X];
initTheta = zeros(size(lrX,2),1);

options = optimset('GradObj','on','MaxIter',250);

%[optTheta,funVal,exitFlag] = fminunc( @(t)(lrCostFunction(t,lrX,Y,0) ),initTheta,options )

[ optTheta ] = fmincg( @(t)(lrCostFunction(t,lrX,Y,0) ),initTheta,options );

%size(optTheta)

[ J,grad ] = lrCostFunction(optTheta,lrX,Y,0);





