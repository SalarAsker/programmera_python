#Skriv ett program som räknar portot för ett brev. Programmet ska 
# läsa in vikt på brevet och visa portot pris enligt följande, 
# om vikt är mindre än eller lika med 20 g, kostar portot 5 kronor.
# om vikt är större än 20g och mindre än eller lika med 50 g, kostar portot 15 kronor.
# om vikt är större än 50 g och mindre än eller lika med 100 g, kostar portot 30 kronor.
# För en vikt över 100g kostar portot 50 kronor. 

# läs in vikten på brevet
brevVikt = float(input('Ange vikt på brevet i gram : '))
#skapa en pris variabel
pris = 0

# utföra operationer

if brevVikt >0 and brevVikt <= 20:
    pris = 5
    print('Du betalar: ', pris , 'kr')
elif brevVikt >20 and brevVikt <=50:
    pris = 15
    print('Du betalar: ', pris , 'kr')
elif brevVikt >50 and brevVikt <=100:
    pris = 30
    print('Du betalar: ', pris , 'kr')
elif brevVikt > 100:
    pris = 50
    print('Du betalar: ', pris , 'kr')
else:
    print('ogiltig vikt')



    