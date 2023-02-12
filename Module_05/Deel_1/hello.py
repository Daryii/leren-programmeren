def function_town(num):
    zin = ""
    for i in range(1,num + 1):
        zin += f"Hello from function town {i}! \n"
    return zin

f = function_town(12)
print(f)