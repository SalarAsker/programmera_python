# Skriv ett lotto program. En användare väljer tre favorita tal mellan 1 -35. 
# Programmet ska sedan köra 10000 dragningar (en loop). I varje dragning ska 
# det slumpas ett tal mellan 1-35. Programmet ska kolla hur många rätt träffar 
# man får gentemot angivna favorita talen. 

import random
# funktionen returnerar ett random tal mellan 1-35
def RandomLottoTal():
    return random.randint(1,35)

# mata in tre favorita talen
tal1 = int(input('Mata in favorit tal1: '))
tal2 = int(input('Mata in favorit tal2: '))
tal3 = int(input('Mata in favorit tal3: '))

# variabler för att hålla koll på antal träffar
antalTal1 = 0
antalTal2 = 0
antalTal3 = 0


# 10000 dragningar
for i in range(10000):
    drag = RandomLottoTal()
    if(drag == tal1):
        antalTal1 = antalTal1 +1
    if(drag == tal2):
        antalTal2 =  antalTal2 +1
    if(drag == tal3):
        antalTal3 =  antalTal3 +1

# printa ut resultatet
print(tal1, 'du får träffar: ', antalTal1)
print(tal2, 'du får träffar: ', antalTal2)
print(tal3, 'du får träffar: ', antalTal3)



