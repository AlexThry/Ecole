solution :- ordre(Cadeaux),
	membre(cadeau(_,poisson-rouge,_,grand-pere), Cadeaux),
	membre(cadeau(_,_,bonne-note,_), Cadeaux),
	membre(cadeau(_,chien,_,_), Cadeaux),
	membre(cadeau(_,_,vacances,_), Cadeaux),
	cadeau(_,_,_,pere),
	cadeau(claude,_,_,_),
    cadeau(rose,_,_,_),

    
    recu_avant(cadeau(alain,_,_,_), cadeau(_,chat,_,_), Cadeaux),
    recu_avant(cadeau(_,_,bonne-note,_), cadeau(alain,_,_,_), Cadeaux),
    recu_avant(cadeau(_,_,_,marraine), cadeau(_,chien,—,—), Cadeaux),
    recu_avant(cadeau(_,chien,—,—), cadeau(_,_,vacances,_), Cadeaux), 
    
    recu_par_femme(cadeau(_,poisson-rouge,_,grand-pere)),
    recu_par_femme(cadeau(_,chat,_,_)),
    recu_par_femme(cadeau(cadeau(_,_,noel,_)),
    
    recu_par_homme(cadeau(_,_,bonne-note,_)),
    
    offert_par_femme(cadeau(rose,_,_,_)),
    offert_par_femme(cadeau(_,_,noel,_)),
    
    not(occasion(anniversaire, cadeau(_,poisson-rouge,_,grand-pere))),
    not(animal(chat, cadeau(alain,_,_,_))),
        
    Cadeaux = [_,_,_,_,cadeau(_,_,noel,_)],
    
    printC(Cadeaux).

ordre([cadeau(_,_,_,_),
      cadeau(_,_,_,_),
      cadeau(_,_,_,_),
      cadeau(_,_,_,_),
      cadeau(_,_,_,_)]).

recu_avant(X, Y, [X, Y | _]).
recu_avant(X, Y, [_, K]) :- recu_avant(X, Y, K).

homme(grand-pere).
homme(pere).
homme(oncle).
homme(alain).
homme(claude).
homme(thierry).
femme(tante).
femme(marraine).
femme(beatrice).
femme(rose).

cadeau(_,_,_,_).

membre(X, [X|_]).
membre(X, [_|Y]) :- membre(X, Y).

enfant(X, cadeau(X,_,_,_)).
animal(X, cadeau(_,X,_,_)).
occasion(X, cadeau(_,_,X,_)).
offert_par(X, cadeau(_,_,_,X)).

offert_par_homme(cadeau(_,_,_,X)) :- homme(X).
offert_par_femme(cadeau(_,_,_,X)) :- femme(X).

recu_par_femme(cadeau(X,_,_,_)) :- femme(X).
recu_par_homme(cadeau(X,_,_,_)) :- homme(X).

printC([]).
printC([X|R]) :- writeln(X), print(R).