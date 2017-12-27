function a = accuracyP(X,Theta,Y)
    
    p = predict(X,Theta);

    e = (sum((p - Y).^2 )/ size(p,1)) *100 ;
    
    a = 100.0 - e;

end