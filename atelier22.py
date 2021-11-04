l=[11,45,8,23,14,12,78,45,89] #valeur initiale a la liste
b=len(l) 
l1=[] #1iere division
l2=[] #2eme division
l3=[] #3eme division
for i in range(b/3) :  #parcourir la liste 
  l1.append(l[i])  #addition des elements
  l2.append(l[i+3])
  l3.append(l[i+6])

print(l1,l2,l3)  #affichage du resultat

