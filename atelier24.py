s1={23, 42, 65, 57, 78, 83, 29} #valeur initiale du set
s2={57, 83, 29, 67, 73, 43, 48} #valeur initiale du set

print("intersection")
print(s1.intersection(s2)) #intersection des 2 sets

for element in s1.intersection(s2): #parcourir l'intersection
  s1.remove(element)  #suppression des elements

print("Set 1 apres suppression :")
print(s1) #affichage du resultat

