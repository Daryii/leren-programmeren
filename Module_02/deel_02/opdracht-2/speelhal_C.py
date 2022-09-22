# 3 vrienden , ppp betekent prijs per person = 7.45 euro 
# VR is 5 minuten 0.37 euro
# Er zijn negen 5 minutenn in 45 min je hebt negen 5 minuten in 45 min .

aantal = int(input("vul hier de aantal mensen ="))
ppp = float(input ("vul hier de prijs per person ="))
vip_vr = int(input("vul hier de prijs van de vip_vr="))

prijs =(aantal*ppp+ vip_vr*aantal)

print (f"Dit geweldige dagje-uit met {aantal} mensen in de Speelhal met 45 minuten VR kost je maar {prijs} euro")