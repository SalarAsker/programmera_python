# Skapa en lista med 10 heltal. Programmet ska loopa 
# igenom listan och adderar alla talen som finns i listan. 
# Programmet ska i slutet skriver ut summan. 

tallist = [1,2,3,4,5,6,7,8,9,10]
summa = 0
for index in range(len(tallist)):
    summa = summa + tallist[index]

print('Summa är', summa)