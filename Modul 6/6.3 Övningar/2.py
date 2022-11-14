# Skriv en generell funktion som beräknar vad en vara kostar 
# efter rabatten. Som parametrar tar funktionen varans pris 
# och rabatt värde. Funktionen returnerar resultatet tillbaka.   

# funktionsdefinition
def RäknaPris(pris, rabatt):
    rabatt = rabatt / 100 # ändra rabatt till procent
    rabPris = pris * rabatt; # räkna rabatt värde
    return pris - rabPris # räkna rabattrat pris


# program
pris = float(input('Ange pris: '))
rabatt = float(input('Ange Rabatt(%): '))

rabatteratPris = RäknaPris(pris, rabatt)

print('Varan kostar', rabatteratPris, 'efter rabatten!!')