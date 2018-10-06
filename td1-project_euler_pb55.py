#Problem55

def reverse(N):  #Fonction qui nous permet de renverser un nombre
    M=0
    while N>0:
        M=M*10+N%10 #A chaque itération on ajoute le dernier chiffre de N et la multiplication de M par 10 "décale" les termes vers la gauche
        N=N//10
    return M
#---------------------------------------------------------------------------------------
def palindrome(N):  #Fonction qui vérifie si N est un palindrome
    return N==reverse(N)
#-------------------------------------------------------------------------------------

assert palindrome(3773) and palindrome(1234321) and not palindrome(1234)  #on teste la fonction pour certains nombres

#---------------------------------------------------------------------------------------

def Lychrel(N): #Fonction qui indique si un nombre est un nombre de Lychrel d'après les conditions de l'énoncé
    j=0
    P=N
    while j<50 and not palindrome(P):
        P+=reverse(P)
        j+=1
    return j>=50

#--------------------------------------------------------------------------------------
assert Lychrel(196) and Lychrel(10677) and not Lychrel(47) and not Lychrel(349) #On teste la fonction avec les nombres de l'énoncé
#--------------------------------------------------------------------------------------

def solve(n): #Fonction finale
    res=0
    for i in range(n):
        if Lychrel(i):
            res+=1
    return res
#--------------------------------------------------------------------------------------
print(solve(10000))
