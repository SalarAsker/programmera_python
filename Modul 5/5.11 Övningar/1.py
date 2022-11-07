# Skriv ett program som läser in två meningar genom att använda 
# två olika input() metoder. Programmet ska först sammanfoga 
# båda meningar och sedan leta efter tecken a och d i texten. 
# Programmet ska skriva ut hur många av varje finns i texten. 

mening1 = input('Ange mening1: ')
mening2 = input('Ange mening2: ')

enMening = mening1 + mening2 # + sammanfogar sträng variabler

antal_a = 0
antal_d = 0

for i in range(len(enMening)):
    if enMening[i] == 'a':
        antal_a = antal_a + 1
    if enMening[i] == 'd':
        antal_d = antal_d + 1

print('Antal a:', antal_a)
print('Antal d:', antal_d)