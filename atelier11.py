
def fact(a):     #creation du fonction factorielle
  if  a==0 :return 1
  else:  return  a*fact(a-1)

def somme(a):   #creation du fonction somme
  if  a==0 :return 0
  else:  return  a+somme(a-1)

def exo1(b):    #fonction output exercice 
  c=int(somme(fact(b)/b))
  return c

a=int(input("donnez votre nombre \n"))  #input de l'utilisateur
print(exo1(a))    #affichage du resultat