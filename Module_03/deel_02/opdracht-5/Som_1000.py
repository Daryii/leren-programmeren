s = 50
w = 50
ans= 50

while ans < 1000:
    s = s + 1
    w = f"{s}+{w}"
    ans= ans + s
    print(f"{w}={ans}")