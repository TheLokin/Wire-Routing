#program always.
% Posiciones válidas para moverse.
next(X,Y,X+1,Y) :- _column(X), _row(Y), not _obstacle(X,Y), not _obstacle(X+1,Y).
next(X,Y,X-1,Y) :- _column(X), _row(Y), not _obstacle(X,Y), not _obstacle(X-1,Y).
next(X,Y,X,Y+1) :- _column(X), _row(Y), not _obstacle(X,Y), not _obstacle(X,Y+1).
next(X,Y,X,Y-1) :- _column(X), _row(Y), not _obstacle(X,Y), not _obstacle(X,Y-1).

% Moverse de X,Y a X1,Y1.
1 {move(X,Y,X1,Y1,W): next(X,Y,X1,Y1)} 1 :- wire(X,Y,W), not _end(X,Y,W).

% No volver a una posición ya visitada.
:- move(X,Y,X1,Y1,W), move(X1,Y1,X,Y,W), 'next(X,Y,X1,Y1), 'next(X1,Y1,X,Y).

% Consideramos la primera posición como cableada.
wire(X,Y,W) :- _start(X,Y,W).

#program dynamic.
move(X,Y,X1,Y1,W) :- 'move(X,Y,X1,Y1,W).
wire(X1,Y1,W) :- 'move(X,Y,X1,Y1,W), 'next(X,Y,X1,Y1).

% No moverse en cuadrados o rectángulos.
:- wire(X,Y,W), wire(X+1,Y,W), wire(X-1,Y,W), wire(X,Y+1,W).
:- wire(X,Y,W), wire(X+1,Y,W), wire(X-1,Y,W), wire(X,Y-1,W).
:- wire(X,Y,W), wire(X,Y+1,W), wire(X,Y-1,W), wire(X+1,Y,W).
:- wire(X,Y,W), wire(X,Y+1,W), wire(X,Y-1,W), wire(X-1,Y,W).

% No puede haber dos cables en la misma posición.
:- wire(X,Y,W), wire(X,Y,S), W<S.

#program final.
:- _end(X,Y,W), not wire(X,Y,W).

#show wire/3.