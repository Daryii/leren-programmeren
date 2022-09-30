bedrag = int(input("voer bedrag in :"))

euro_2 = bedrag // 200
print (f"aantal 2 euro :{euro_2}")
restant= bedrag - 200 * euro_2

euro_1 = restant // 100 
print (f'aantal 1 euro:{euro_1}')
restant = bedrag - 100 * euro_1


euro_050 = bedrag // 50
print (f'aantal 50 cent :{euro_050}')
restant= bedrag - 50 * euro_050


print (restant)