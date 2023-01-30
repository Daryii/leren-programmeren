def fibonacci(aantal : int) -> float:
    lijst = [0,1]
    for i in range(2, aantal):
        lijst.append(lijst[-1] + lijst[-2])
    gulden_snede = ((lijst[-1]) / lijst[-2])
    return gulden_snede
    

print(fibonacci(5))
