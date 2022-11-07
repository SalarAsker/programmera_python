# Skriv ett program som kastar en tärning 10 gångar och skriver ut varje kast.

# importera random modul
import random
# while-loop som går 10 varv
antal = 1
while antal <=10:
    print(random.randint(1,6)) #kasta tärning samt printa ut
    antal = antal +1