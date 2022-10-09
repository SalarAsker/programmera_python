# Studera och koda följande program. Programmet läser in 
# antal månader som indata och sedan konverterar månader i år och månader. 

numberOfMonths = int(input('skriv antal månader:'))
years = numberOfMonths // 12
months = numberOfMonths % 12
print( f' {numberOfMonths} is equal to: {years} years and {months} months')
