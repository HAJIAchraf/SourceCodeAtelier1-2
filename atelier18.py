def exo8(a,b):  #creation du focntion
  i=0
  for element in a:  #parcourire la chaine de caracteres
    if element==b:
      i+=1
    else :continue
  return i   
    
a=input("donnez votre chaine de caracteres \n") #input de la chaine
b=input("donnez votre caractere \n")  #input du caractere 
print(exo8(a,b))  #affichage du resultat