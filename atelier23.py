l=[11,45,8,11,23,45,23,45,89] #valeur initiale du liste
l1=[]
dict={}

for element in l :  #parcourir les elements du liste
  dict[element]=l.count(element)  #addition des elements 

print(dict)  #affichage du resultat