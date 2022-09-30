def get_bool(karakter: str) -> bool:
    print(f"ik ben nu bezig met: {karakter}")
    reactie = False
    if karakter == "a":
        reactie = True
    elif karakter == "b":
        reactie = False
    print(reactie)
    return reactie

if get_bool("a") or get_bool("b"):
    print("Het is waar")



    
x = 3
y = 4
aap = x == 4 or y == 4
noot = x == 3 and y == 5
if x == 4 or y == 4:
    print("aap lust noot")
print(aap)
print(noot)