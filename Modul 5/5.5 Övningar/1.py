# Skriv ett program där användaren kan mata in både ett förnamn 
# och ett efternamn. Programmet ska visa vilka initialer personen har. 
# En körning på programmet ser ut som, 

#  Ange förnamn: Salar
#  Ange efternamn: Asker
#  Salar Asker har initialerna S.A

fnamn = input('Ange förnamn: ')
enamn = input('Ange efternamn: ')

print(fnamn, enamn , 'har initialerna', fnamn[0],'.',enamn[0])