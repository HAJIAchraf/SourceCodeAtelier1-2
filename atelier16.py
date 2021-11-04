def bull(l1):  #creation du fonction
  n=len(l1)
  for j in range(n) :  #parcourir la liste
    for i in range(n-j-1):
      if l1[i]>l1[i+1]:  #comparaison des elements
        a=l1[i]
        l1[i]=l1[i+1]
        l1[i+1]=a  
  return l1
'''--------------------------------------------------------------------------'''
def selection(l1):  #creation du fonction
  n=len(l1)
  for i in range(n):   #parcourir la liste
    min = i
    for j in range(i+1, n):
      if l1[min] > l1[j]:  #comparaison des elements
          min = j
    tmp = l1[i]
    l1[i] = l1[min]
    l1[min] = tmp
  return l1
'''--------------------------------------------------------------------------'''
def insertion(l1):  #creation du fonction
  n=len(l1)
  for i in range(1,n):  #parcourir la liste
    k = l1[i] 
    j = i-1
    while j >= 0 and k < l1[j] :  #comparaison des elements
      l1[j + 1] = l1[j] 
      j -= 1
      l1[j + 1] = k
  return l1
'''--------------------------------------------------------------------------'''
l1=[10,3,2,7,0] #valeur initiale donné à la liste
print("--> pour tri a bull : 1 \n--> pour tri par selection : 2 \n--> pour tri par insertion : 3\n") #menu du choix du tri désiré
select=int(input("donnez votre choix :\n"))
if select==1 :  #choix du tri a bull
  print("votre nouvelle liste triee par bull est: ",bull(l1))
elif select ==2 : #choix du tri par selection
  print("votre nouvelle liste triee par selection est: ",selection(l1)) 
else :    #choix du tri par insertion
  print("votre nouvelle liste triee par insertion est: ",insertion(l1)) 

  


