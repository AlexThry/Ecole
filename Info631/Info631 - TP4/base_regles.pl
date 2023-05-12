%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  Description des éléments du système                               %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

partition(x, [court, long], [(0, 50), (50, 100)]).
partition(y, [etroit, large], [(0, 50), (50, 100)]).

regle(xyr, court, etroit, petit).
regle(xyr, court, large, moyen).
regle(xyr, long, etroit, moyen).
regle(xyr, long, large, grand).

% A compléter






%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  Calcul                                                            %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

entre(X, Min, Max) :- X >= Min, X < Max.

appart(Val, Domaine) :- Domaine = (Min, Max), entre(Val, Min, Max).                                    
                                  
appartenance(Val, Symb, [Symb|_], [Domaine|_]) :- appart(Val, Domaine). 
appartenance(Val, Symb, [_|QSymb], [_|QDom]) :- appartenance(Val, Symb, QSymb, QDom).   

descrip(NomVar, ValNum, Symb) :- partition(NomVar, LS, LDomaine),
                                 appartenance(ValNum, Symb, LS, LDomaine).
description(NomVar, ValNum, LS) :- setof(Symb, descrip(NomVar, ValNum, Symb), LS).

infer1(NomRel, [Symb1|_], Symb2, SymbS) :- regle(NomRel, Symb1, Symb2, SymbS).
infer1(NomRel, [_|QS1], Symb2, SymbS) :- infer1(NomRel, QS1, Symb2, SymbS).

infer2(NomRel, LS1, [Symb2|_], SymbS) :- infer1(NomRel, LS1, Symb2, SymbS).
infer2(NomRel, LS1, [_|QS2], SymbS) :- infer2(NomRel, LS1, QS2, SymbS).

inference(NomRel, DS1, DS2, DescS) :- setof(SymbS, infer2(NomRel, DS1, DS2, SymbS), DescS).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  Structure du système                                              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

systeme(xyr, Numx, Numy, DLr) :- description(x, Numx, DLx),
                                 description(y, Numy, DLy),
                                 inference(xyr, DLx, DLy, DLr).



