#program final.
% Obtener el camino óptimo.
wire(W) :- wire(X,Y,W).
count(C,W) :- C=#count{X,Y: move(X,Y,X1,Y1,W)}, wire(W).

#minimize{C,W: count(C,W)}.