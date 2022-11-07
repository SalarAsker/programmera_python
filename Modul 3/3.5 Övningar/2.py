# Skriv ett program som beräknar kostnaden för att ringa med en 
# mobiltelefon med ett enkelt abonnemang. Programmet ska läsa in 
# hur många minuter man ringer per månad. I abonnemanget kostar 
# en minut 2 kr. Programmet ska läsa totala priset och man får 
# 10% rabatt om man ringer för minst 300kr. 

minuter = int(input('Ange minuter ? '))
pris = minuter * 2; # en minut kostar 2kr
if pris >= 300:
    rabatt = pris * 0.1 # beräkna 10% rabatt av priset.
    pris = pris - rabatt # ge rabatt
print('Du ska betala ',pris,'kr')
