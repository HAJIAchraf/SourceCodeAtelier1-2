def somme(a):   #creation du fonction
  if  a==0 :return 0
  else:  return  a+somme(a-1)

a=int(input("donnez votre nombre \n"))  #input de l'utilisateur
print(somme(a))  #affichage du resultat 