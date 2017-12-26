function [J,grad] = lrCostFunction(Theta,X,y,lambda)

%computes the cost of the error in logisstic regression
m = length(y);
J = 0;
grad = zeros(size(Theta));

% logistic regresiion cost function
% without regularization
J = sum( -y.*log( sigmoid(X*Theta) ) - (1-y).*log( 1 - sigmoid(X*Theta) ))/m;% + (lambda*sum(theta(2:end).^2))/(2*m);


grad =  (X'*(sigmoid(X*Theta)-y))/m ;%+ (lambda/m)*theta ;

%grad(1) = grad(1) - (lambda/m)*theta(1) ;

% =============================================

grad = grad(:);

end
