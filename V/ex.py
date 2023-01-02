import random

names = []

# Keep asking for names until there are at least 3
while len(names) < 3:
    name = input("Enter a name: ")
    if name in names:
        print("That name has already been entered. Please enter a different name.")
    else:
        names.append(name)

# Assign each name a unique gift
gifts = {}
for name in names:
    gift = random.choice(names)
    while gift == name:
        gift = random.choice(names)
    gifts[name] = gift

# Print the results
print("Here are the gift assignments:")
for name, gift in gifts.items():
    print(f"{name} -> {gift}")
