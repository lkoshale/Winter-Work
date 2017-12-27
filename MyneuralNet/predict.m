function p = predict(X,all_Theta)

a = [ones(size(X,1),1),X];
p = sigmoid(a*all_Theta);

% 0 --> bike 1--> airoplane
for i = 1:length(p)
    
    if p(i) >= 0.5
        p(i) = 1;
    else
        p(i) = 0;
    end
    
end


end
