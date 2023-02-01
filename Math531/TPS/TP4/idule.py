from ply import lex
from ply import yacc


###################################################
# LEXER
###################################################

reserved = {
    'get': 'GET',
    'and': 'AND',
    'or': 'OR',
    'contains': 'CONTAINS',
    'exclude': 'EXCLUDE',
    'union': 'UNION',
    'intersect': 'INTERSECT',
    'diff': 'DIFF'
}

tokens = ['URL', 'NAME', 'LIGNE'] + list(reserved.values())

t_ignore = ' \t\n'


def t_URL(t):
    r'(https://|http://)[A-Za-z0-9\./\?_]+'
    t.type = reserved.get(t.value, 'URL')
    return t


def t_NAME(t):
    r'[A-Za-z0-9][A-Za-z0-9]*'
    t.type = reserved.get(t.value, 'NAME')
    return t


def t_error(t):
    print("error")


lex.lex()

ressources = {"http://oui.non": ["babablalbbalbcbaalabalalabalab", "cbalablababalablabla", "analcncacalnalnblabla", "blabla"],
              "https://wikipedia.org": ["article1", "article2", "article3"],
              "ressource": ['1', '2', '3', '4', '5'],
              "pirate": ["crack1", "crack2", "crack3"]}

###################################################
# PARSER
###################################################


def p_expression(p):
    '''expression : expression LIGNE expression
    | GET URL
    | GET URL instruction
    | GET NAME
    | GET NAME instruction'''
    if len(p) == 3:
        try:
            p[0] = ressources[p[2]]
        except KeyError:
            print("cette ressource n'éxiste pas")
    elif not(isinstance(p[3][0], list)) and p[3][0] == "contains":
        try:
            count = 0
            for i in ressources[p[2]]:
                if i == p[3][1]:
                    count += 1
            ratio = None
            if count:
                ratio = count/len(ressources[p[2]])
            p[0] = f"Valeur recherché : {p[3][1]}, Nombre d'apparition : {count}, pourcentage de la ressource : {ratio}"
        except KeyError:
            print("cette ressource n'éxiste pas")
    elif not(isinstance(p[3][0], list)) and p[3][0] == "exclude":
        try:
            res = []
            for ressource in ressources[p[2]]:
                if ressource != p[3][1]:
                    res += ressource
            p[0] = res
        except KeyError:
            print("cette ressource n'éxiste pas")

    # print(list(p))


def p_instruction(p):
    '''instruction : instruction OR contrainte
    | instruction AND contrainte
    | contrainte'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == "and":
        p[0] = ([p[1], p[3]])
    elif p[2] == "or":
        p[0] = ([p[1]], [p[3]])


def p_contrainte(p):
    '''contrainte : CONTAINS NAME
    | EXCLUDE NAME'''
    p[0] = (p[1], p[2])


def p_error(p):
    print("error")


yacc.yacc()


if __name__ == "__main__":

    # while True:
    # 	i = input("Idule 1.0 >>> ")
    # 	if i == "quit()":
    # 		break
    # 	lex.input(i)
    # 	while True:
    # 		tok = lex.token() #lecture du prochain token ou none
    # 		if not tok: break
    # 		print(tok)

    print("########-----------------------------------########")
    print("le language ne gere actuellement qu'une instruction. ")
    print("les ressources disponibles sont :  https://oui.non, https://wikipedia.org, ressource, pirate")
    print("########-----------------------------------########")
    while True:
        i = input("Idule 1.0 >>> ")
        if i == "quit()":
            break
        print(yacc.parse(i))
        print("-----------------------------------")
