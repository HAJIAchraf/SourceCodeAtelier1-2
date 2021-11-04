def exo9(a,b):  #creation du fonction
  for i in range(0,len(a)):  #parcourir les lignes du matrice
    for j in range(0,len(a[0])) :  #parcourir le colenes du matrice
      if a[i][j]==b:  #comparaison 
        print(i,",",j)  #affichage des coordonnes

a=[[1,2,3],[1,3,1],[1,5,1]]  #valeur initiale du tableau 
b=input("donnez l'element que vous cherchez\n") #input de l'utilisateur

print(exo9(a,b))  #affichage du resultat




