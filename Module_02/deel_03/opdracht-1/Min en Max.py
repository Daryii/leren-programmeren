a = int(input("Typ hier een getal:"))
b = int(input("Typ hier een getal:"))

Max = a
Min = b

if a > b:
    print(f"a is het grootste getal{Max}")
elif a < b:
    print(f"a is het kleinste getal{Min}")       
else:
    print("Max en Min zijn even groot")

print (f"Het minimum is:{Min}")
print (f"Het maximun is:{Max}")




