
#Problem 16

def solve(n):
    res=0    
    a=str(2**n)    #on transforme le nombre en chaîne de caractères
    for x in a:
        res+=int(x) #on retransforme chaque caractère chiffré en entier, et on somme le tout dans une boucle
    return res 

assert solve(15)==26  #on vérifie que cela marche bien pour n=15
print(solve(1000))  
        


 


        
        
    