def exo2(a):  #creation du fonction
  if  a>1 : 
    exo2(a//2)
    print (a%2,end="")  #affichage du reste de division

a=int(input("donnez votre nombre \n")) #input de l'utilsateur
print(exo2(a))    #affichage du resultat
