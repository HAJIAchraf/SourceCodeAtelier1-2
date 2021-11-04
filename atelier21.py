l1=[3,6,9,12,15,18] #valeur initiale du liste 
a=len(l1)  #nombre d'elements
l2=[4,8,12,16,20,24,28] #valeur initiale du liste
b=len(l2)  #nombre d'elements
l3=[] #liste vide pour les resultats 
for i in l1:  #parcourir liste 1
  c=l1.index(i)
  if c%2==1 :  #verification du condition
    l3.append(l1[c]) #ajouter element apres verification
  else : continue

for i in l2 :  #parcourir liste 1
  d=l2.index(i)
  if d%2 ==0 :  #verification du condition
    l3.append(l2[d]) #ajouter element apres verification
  else : continue

print(l3)    #affichage du resultat