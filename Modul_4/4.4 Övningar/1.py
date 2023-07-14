# Du ska programmera gissa mitt tal spel. Programmet ska ta fram 
# ett slumptal mellan 1 till 20. Spelaren som kör programmet 
# har 5 försök på sig för att gissa talet. Gissar man fel 
# anger programmet om det tal man gissar är för litet eller 
# för stort. Om spelaren lyckas gissa talet skriver programmet 
# Grattis och avbryts loopen genast.  Annar löper loopen igenom alla varven. 

# importera random
import random
print('Gissa talet mellan 1 - 20')
print('Du har 5 försök!!!')
försök = 0
# ta fram ett tal mellan 1 till 20
tal = random.randint(1,20)
# starta spelet
while försök <=5:
    f = int(input('Gissa talet?: '))
    if f == tal:
        print('Grattis!! Rätt Gissat')
        break
    if f > tal:
        print('För stort')
    if f < tal:
        print('För litet')
    
    # öka försök med ett
    försök = försök + 1
