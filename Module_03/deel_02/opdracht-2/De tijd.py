r = 1

while r <= 24:
    if r < 13:
        print(f"{r} uur in am")
    else:
        print(f"{r-12} uur in pm")
    r= r+1
