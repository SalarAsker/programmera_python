# Kör flera input() och läs in personuppgifter förnamn, efternamn, 
# telefon och email. Programmet ska skriva ut en utskrift som följande, 
# Vi har tagit emot uppgifter: 
# Name: Salar Asker 
# Telefon: 0738000000 
# Email: salar@abc.com
# (för att införa en radbrytning lägg \n i strängen)

fnamn = input('Ange förnamn: ')
enamn = input('Ange efternamn: ')
tel = input('Ange telefon: ')
email = input('Ange email: ')
print('Vi har tagit emot uppgifter:\nName:',fnamn,enamn,'\nTelefon:',tel,'\nEmail',email)