
#Problem 16

def solve(n):
    res=0    
    a=str(2**n)    #on transforme le nombre en cha�ne de caract�res
    for x in a:
        res+=int(x) #on retransforme chaque caract�re chiffr� en entier, et on somme le tout dans une boucle
    return res 

assert solve(15)==26  #on v�rifie que cela marche bien pour n=15
print(solve(1000))  
        


 


        
        
    