#Problem 22

def score_name(name):  #On �crit une fonction qui retourne le score d'un nom
    alphabet=['"','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
    #on g�n�re la liste des lettres latines dans l'ordre alphab�tique et la valeur de chaque lettre sera son indice dans la liste (les guillemets comptant pour 0)
    res=0
    for x in name:
        res+=alphabet.index(x)
    return res
 
#---------------------------------------------------------------------------------------------------

assert score_name("COLIN") == 53 #on v�rifie que la fonction renvoie le bon r�sultat pour l'exemple donn�

#---------------------------------------------------------------------------------------------------
def solve(n): #On �crit la fonction qui calcule le score total d'une liste de noms donn�e n
    Score_total=0
    for x in n:
        Score_total+=score_name(x)*(n.index(x)+1)  #on n'oublie pas de d�caler les indices de +1
    return Score_total
#---------------------------------------------------------------------------------------------------


f = open('p022_names.txt', 'r') #on ouvre le fichier et on cr��e la liste de noms
g=f.read()
names=g.split(',')  #on s�pare les noms au niveau des virgules
names=sorted(names) #on trie la liste par ordre alphab�tique

#----------------------------------------------------------------------------------------------------

assert names.index('"COLIN"')+1 == 938 #On v�rifie que la liste est correctement tri�e pour le nom COLIN

print(solve(names))

    
        
