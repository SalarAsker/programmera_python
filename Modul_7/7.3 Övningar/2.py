# Använd följande namnlista i ett program, 
# namnlista = ['olle', 'kalle', 'pelle', 'sara', 'petter']
# Du ordnar en fest och bjudar in personer som finns i namnlista. 
# Kostnaden till en person är 100kr. Du skriver ett program 
# som beräknar totala kostnaden på festen. 
# Programmet har en funktion som heter AntalPersoner(). 
# Funktionen tar emot namnlista som inparameter och returnerar 
# ett tal som motsvarar antal personer i listan. Använd det talet 
# som funktionen returnerar och beräkna kostnaden. 

def AntalPersoner(allapersoner):
    antal = len(allapersoner)
    return antal

namnlista = ['olle', 'kalle', 'pelle', 'sara', 'petter']
personer = AntalPersoner(namnlista)
kostnaden = personer * 100

print('Fest kostar', kostnaden)