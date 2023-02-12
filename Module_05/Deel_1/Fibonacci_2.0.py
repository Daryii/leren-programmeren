def fibonacci(max: int):
    lijst = [0, 1]
    while len(lijst) < max:
        lijst.append(lijst[-1] + lijst[-2])
    return lijst

print(fibonacci(9))
