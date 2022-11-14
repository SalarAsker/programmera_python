# Skriv en funktion som omvandlar en temperatur i grader Fahrenheit till grader Celsius. Funktionen ska returnera resultat tillbaka där anropet görs. 
# Använd formeln
# celsius = ( fahrenheit -32 ) / 1.8

# funktionen som omvandlar
def TemoOmvandlig():
    tempF = float(input('Ange temp i F: ?'))
    tempC = (tempF-32)/1.8
    return tempC

# program
temp = TemoOmvandlig() #anrop
print('Temp i Celsius: ', temp)

