# Skriv ett simpelt inloggningsprogram. Programmet ska läsa in ett 
# användarnamn och ett lösenord. I programmet finnas en fördefinierad användare som,

# system_user = 'abc'
# system_passwd = 'xyz'

# När indata kommer in i programmet ska du jämföra den 
# med fördefinierade användaren. Vid rätt inmatning ska programmet 
# skriva ut , du är inloggad. Annars skrivs det ut, felaktigt användarnamn eller lösenord.

# användaren i systemet
system_user = 'abc'
system_passwd = 'xyz'

# läsa in ett användarnamn och ett lösenord
namn = input('Ange användarnamn: ')
lösen = input('Ange lösenord: ')

# jämför
if system_user == namn and system_passwd == lösen:
    print('Du är inloggat!!')
else:
    print('felaktigt användarnamn eller lösenord')