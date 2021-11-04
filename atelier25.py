dict={'Yassine':47,'Imane':69,'Mohammed':76,'Abir':97} #valeur initiale
l=[47, 64, 69, 37, 76, 83, 95, 97] #valeur initiale 
l1=[]
def check(a,dict):  #creation fonction de verification
  exist=False  
  for element in dict:  #parcourir la dictionnaire
    if a==dict[element]: exist=True #condition
    else: exist=False   
  return exist

print(dict) #affichage 
print(l)   #affichage 

for element in l: #parcourir la liste
  if check(element,dict)==False: #verification d'existence
    l.remove(element) #suppression

print("liste apres modification")
print (l) #afichage du resultat