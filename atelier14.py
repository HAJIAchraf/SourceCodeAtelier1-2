def exo4(a):  #creation du fonction
  if a==0 :return 0
  elif a==1 :return 1
  else : return exo4(a-1)+exo4(a-2)

a=int(input("donnez votre nombre \n"))  #input de l'utilisateur
print(exo4(a))   #affichage du resultat 
