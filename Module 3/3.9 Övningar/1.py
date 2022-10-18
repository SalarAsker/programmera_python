# Skriv ett miniräknare program. Användaren matar in tal1, tal2 och 
# ett räknesätt (+, -, *, /). Programmet ska räkna ett resultat baserat på indata.

# läs in data
tal1 = float(input('Ange tal1: '))
tal2 = float(input('Ange tal2: '))
räknesätten = input('Ange räknesätten: ')

#skapa en result variabel
resultat = 0

# utföra operationer

if räknesätten == '+':
    resultat = tal1 + tal1
    print('Resultatet är ', resultat)
elif räknesätten == '-':
    resultat = tal1 - tal1
    print('Resultatet är ', resultat)
elif räknesätten == '*':
    resultat = tal1 * tal1
    print('Resultatet är ', resultat)
elif räknesätten == '/':
    resultat = tal1 / tal1
    print('Resultatet är ', resultat)
else:
    print('Okänd operation!!')

