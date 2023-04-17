from functions import print_colorvars
from functions import getEarnigs


testMainCharacter1 = {
    'name' : 'TestChar1',
    'cash' : {
        'platinum' : 0,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
}

inverstorsTestList1 = [{
    'name' : 'TestInvestor1',
    'profitReturn' : 5,
    'adventuring' : True,
    'cash' : {
        'platinum' : 5,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
}]



friendsTestList2 = [{
    'name' : 'TestFriend1',
    'adventuring' : False,
    'shareWith' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 20,
        'silver' : 0,
        'copper' : 0
    }
},{
    'name' : 'TestFriend2',
    'adventuring' : True,
    'shareWith' : False,
    'cash' : {
        'platinum' : 0,
        'gold' : 15,
        'silver' : 0,
        'copper' : 0
    }
}]

result6 = [
    {'name': 'TestChar1', 'start': 0.0, 'end': 237.5}, 
    {'name': 'TestFriend1', 'start': 20.0, 'end': 20.0}, 
    {'name': 'TestFriend2', 'start': 15.0, 'end': 15.0}, 
    {'name': 'TestInvestor1', 'start': 125.0, 'end': 387.5}
]
if getEarnigs(500, testMainCharacter1, friendsTestList2, inverstorsTestList1) != result6:
    print_colorvars(vars=['Test 6 is False'], color='red')
else:
    print_colorvars(vars=['Test 6 is correct'], color='green')

inverstorsTestList2 = [{
    'name' : 'TestInvestor1',
    'profitReturn' : 10,
    'adventuring' : False,
    'cash' : {
        'platinum' : 10,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'name' : 'TestInvestor2',
    'profitReturn' : 5,
    'adventuring' : False,
    'cash' : {
        'platinum' : 5,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'name' : 'TestInvestor3',
    'profitReturn' : 15,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 100,
        'silver' : 0,
        'copper' : 0
    }
}]

result7 = [
    {'name': 'TestChar2', 'start': 30.0, 'end': 455.0}, 
    {'name': 'TestFriend1', 'start': 20.0, 'end': 20.0}, 
    {'name': 'TestFriend2', 'start': 15.0, 'end': 15.0}, 
    {'name': 'TestInvestor1', 'start': 250.0, 'end': 300.0}, 
    {'name': 'TestInvestor2', 'start': 125.0, 'end': 150.0}, 
    {'name': 'TestInvestor3', 'start': 100.0, 'end': 100.0}
]

# if getEarnigs(500, testMainCharacter2, friendsTestList2, inverstorsTestList2) != result7:
#     print_colorvars(vars=['Test 7 is False'], color='red')
# else:
#     print_colorvars(vars=['Test 7 is correct'], color='green')

inverstorsTestList3 = [{
    'name' : 'TestInvestor1',
    'profitReturn' : 10,
    'adventuring' : True,
    'cash' : {
        'platinum' : 10,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'name' : 'TestInvestor2',
    'profitReturn' : 5,
    'adventuring' : False,
    'cash' : {
        'platinum' : 5,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'name' : 'TestInvestor3',
    'profitReturn' : 15,
    'adventuring' : False,
    'cash' : {
        'platinum' : 0,
        'gold' : 100,
        'silver' : 0,
        'copper' : 0
    }
}]

result8 = [
    {'name': 'TestChar2', 'start': 30.0, 'end': 75.5}, 
    {'name': 'TestFriend1', 'start': 20.0, 'end': 35.5}, 
    {'name': 'TestFriend2', 'start': 15.0, 'end': 30.5}, 
    {'name': 'TestInvestor1', 'start': 250.0, 'end': 287.5}, 
    {'name': 'TestInvestor2', 'start': 125.0, 'end': 131.0}, 
    {'name': 'TestInvestor3', 'start': 100.0, 'end': 100.0}
]

# if getEarnigs(120, testMainCharacter2, friendsTestList1, inverstorsTestList3) != result8:
#     print_colorvars(vars=['Test 8 is False'], color='red')
# else:
#     print_colorvars(vars=['Test 8 is correct'], color='green')
