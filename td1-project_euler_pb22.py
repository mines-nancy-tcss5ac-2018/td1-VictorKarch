#Problem 22

def score_name(name):  #On écrit une fonction qui retourne le score d'un nom
    alphabet=['"','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
    #on génère la liste des lettres latines dans l'ordre alphabétique et la valeur de chaque lettre sera son indice dans la liste (les guillemets comptant pour 0)
    res=0
    for x in name:
        res+=alphabet.index(x)
    return res
 
#---------------------------------------------------------------------------------------------------

assert score_name("COLIN") == 53 #on vérifie que la fonction renvoie le bon résultat pour l'exemple donné

#---------------------------------------------------------------------------------------------------
def solve(n): #On écrit la fonction qui calcule le score total d'une liste de noms donnée n
    Score_total=0
    for x in n:
        Score_total+=score_name(x)*(n.index(x)+1)  #on n'oublie pas de décaler les indices de +1
    return Score_total
#---------------------------------------------------------------------------------------------------


f = open('p022_names.txt', 'r') #on ouvre le fichier et on créée la liste de noms
g=f.read()
names=g.split(',')  #on sépare les noms au niveau des virgules
names=sorted(names) #on trie la liste par ordre alphabétique

#----------------------------------------------------------------------------------------------------

assert names.index('"COLIN"')+1 == 938 #On vérifie que la liste est correctement triée pour le nom COLIN

print(solve(names))

    
        
