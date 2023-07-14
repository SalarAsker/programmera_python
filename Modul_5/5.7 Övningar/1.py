# Skriv ett program som läser in en text. Programmet ska
#  undersöka om textens första och sista bokstav är samma eller inte. 

text = input('Ange en valfri text: ')

if text[0] == text[len(text)-1]:
    print('Samma')
else:
    print('Inte samma')