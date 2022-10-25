# Utveckla tärningskast program vidare. Nu ska det vara 
# tusen tärningsslag och programmet ska visa antal sexor. 

# importera random modul
import random
# while-loop som går 10 varv
antal = 1
sexor = 0
while antal <=1000:
    t = random.randint(1,6) #kasta en tärning
    if t == 6: # kollar om den blir en sexa
        sexor =  sexor +1
    antal = antal +1

print('Antal sexor i 1000 slag', sexor)