# Du har programmerat följande program i modul 4 (loopar)

# Utveckla tärningskast program . I programmet ska du göra tusen tärningsslag 
# och programmet ska visa antal sexor. 

# Nu ska du förvandla programmet så att det blir funktionsbaserat. 
# Slumpgeneratorn ska ligga i en funktion fåSlump. Vid anrop av funktionen 
# fåSlump får man ett slumpat tärningsslag. 

import random
# funktionsdefinition som returnerar ett tal mellan 1-6 vid varje anrop
def fåSlump():
    return random.randint(1,6)

antalSexor = 0

for i in range(1000):
    if(fåSlump() == 6):
        antalSexor = antalSexor +1

print('Antal sexor efter 1000 slag', antalSexor)
