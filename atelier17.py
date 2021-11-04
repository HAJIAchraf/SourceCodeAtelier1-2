def exo7(a):  #creation du fonction
  inv_a=""
  for x in a:
    inv_a=x+inv_a  #concatination de la chaine 
  return inv_a 

a=input("donnez votre chaine \n") #input de l'utilisateur
print(exo7(a))  #affichage du resultat 



