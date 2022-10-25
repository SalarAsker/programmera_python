# Skriv ett program som printar ut alla jämna tal i ett intervall. 
# Programmet ska läsa in ett tal från användaren och räknar ut 
# jämna talen mellan 0 till inlästa talet. 


# input från användaren och konvertera till ett heltal (int)
number = int(input("Ange ett tal: "))
# While-loopen
i = 0
while i <= number:
    if i % 2 == 0: # Om jämnt tal
        print(i)
    i = i + 1
