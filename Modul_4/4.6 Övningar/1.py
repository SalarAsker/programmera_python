#Skriv ett program som läser in ett tal och printar ut multiplikationstabell av talet.

tal = int(input('ange ett tal: '))

for k in range(10):
  print(tal,'*',(k+1),'=',tal * (k+1))