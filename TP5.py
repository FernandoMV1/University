#Exercice 1
def remplace(message, abreviation):
    s = ''
    mots = message.split()
    for i in range(len(mots)):
        if mots[i] in abreviation:
              if i==(len(mots)-1):
               s+=abreviation[mots[i]]
              else:
               s+=abreviation[mots[i]]+" "
    print(s)
#####################################################
#Exercice 2
def get_country(l,name):
   for i in l:
      if i["City"] == name:
         return i["Country"]
    
   return False
      
##################################################

#Exercice 3
def ad(dic, mot):
   if mot in dic:
      dic[mot] += 1
   else:
      dic[mot] = 1

def predict(lst, mot):
   dic2 = {}
   for i in lst:
      message = i.split()
      for j in range(len(message)):
         if j!=len(message)-1:
            if message[j]==mot:
               ad(dic2, message[j+1])
   return 

         

