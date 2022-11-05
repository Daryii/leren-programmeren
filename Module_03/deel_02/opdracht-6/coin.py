# name of student: Daryi
# number of student: 99074464
# purpose of program: Wissel geld berekenen 
# function of program: Het berekend wisselgeld en het laat zien hoeveel je van een bepaalde munen 
# structure of program: if's while loops, inputs, variable's en exeptions.



vijfEuro = 500
tweeEuro = 200
eenEuro  = 100
vijftigCent = 50
twintigCent = 20
tienCent = 10
vijfCent = 5
eenCent = 1


toPay = int(float(input('Amount to pay: '))* 100) # Bedrag dat betaald moet worden.
paid = int(float(input('Paid amount: ')) * 100) # Bedrag dat betaald is.
change = paid - toPay # De wisselgeld .

if change > 0: # Als de change meer dan 0 is begint de programma.
  coinValue = 500 # begin value 
  
  while change > 0 and coinValue > 0: # Hier wordt een While voor de change en coinValue gedaan als het groter is dan 0
    nrCoins = change // coinValue # berekening van nrCoins to het geheel getale
    

    if nrCoins > 0: # als er nog coin gegeven moet worden start de IF
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #hier laat je zien hoeveel je munten van een coinvalue kan geven.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Hier vraagt die hoeveel coins je wilt geven
      change -= nrCoinsReturned * coinValue #Change is - De aantal coins dat ingevoerd is keer de coinvalue

      
# comment on code below: Hier gaat die langs alle coinvalue's
    if coinValue == vijfEuro:
      coinValue = vijfEuro
    elif coinValue == tweeEuro:
      coinValue = tweeEuro
    elif coinValue == eenEuro:
      coinValue = eenEuro
    elif coinValue == vijftigCent:
      coinValue = vijftigCent
    elif coinValue == twintigCent:
      coinValue = twintigCent
    elif coinValue == tienCent:
      coinValue = tienCent
    elif coinValue == vijfCent:
      coinValue = vijfCent
    elif coinValue == eenCent:
        coinValue = vijfCent
    else:
        coinValue = 0


  if change > 0: # Hier wordt gecontrollerd of de change groter is dan 0
      print('Change not returned: ', str(change) + ' cents')
  else:
    print("done")




