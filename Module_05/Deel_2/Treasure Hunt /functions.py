import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_FOOD_HORSE_COPPER_PER_DAY 
from data import COST_TENT_GOLD_PER_WEEK 
from data import COST_HORSE_SILVER_PER_DAY
from data import COST_INN_HUMAN_SILVER_PER_NIGHT 
from data import COST_INN_HORSE_COPPER_PER_NIGHT 

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    zilver = amount / 10
    return float(zilver)

def silver2gold(amount:int) -> float:
    goud = amount / 5
    return float(goud)

def copper2gold(amount:int) -> float:
    ans = amount / 50
    return float(ans)


def platinum2gold(amount:int) -> float:
    platinum = amount * 25
    return float(platinum)

def getPersonCashInGold(personCash:dict) -> float:
    platinum = personCash["platinum"] * 25
    copper = personCash["copper"] / 50
    silver = personCash["silver"] / 5
    goud = personCash["gold"] 
    totaal = platinum + copper + silver + goud
    return totaal
##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    people_kosten =  people * COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS
    horses_kosten =  horses * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS
    totaal = people_kosten + horses_kosten
    return copper2gold(totaal)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    lijst = []
    for d in list:
        if key in d and d[key] == value:
            lijst.append(d)
    return lijst    
            
def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people,"adventuring",True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends,"shareWith",True)

def getAdventuringFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'adventuring', True)

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)


def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    horses_s = horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS
    tents_s = tents * COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7 )
    totaal = horses_s + tents_s
    return float(totaal)

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    text = []
    for i in items:
        text.append (f"{i['amount']}{i['unit']} {i['name']}")
    return ", ".join(text) 

def getItemsValueInGold(items: list) -> float:
    items_value = []
    for j in items:
            if j['price']['type'] == "copper":
                type_copper = j['price']['amount'] * j["amount"]
                type_gold = copper2gold(type_copper)
                items_value.append(type_gold)
            elif j['price']['type'] == "silver":
                type_silver = j['price']['amount'] * j["amount"]
                type_gold = silver2gold(type_silver)
                items_value.append(type_gold)
            elif j['price']['type'] == "platinum":
                type_platinum = j['price']['amount'] * j["amount"]
                type_gold = platinum2gold(type_platinum)
                items_value.append(type_gold)
            else:
                items_value.append(j['price']['amount'] * j["amount"])
    return sum(items_value)


##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    cash_in_gold = []
    for i in people:
        cash_in_gold.append(platinum2gold(i['cash']['platinum']))
        cash_in_gold.append(silver2gold(i['cash']['silver']))
        cash_in_gold.append((i['cash']['gold']))
        cash_in_gold.append(copper2gold(i['cash']['copper']))
    return float(sum(cash_in_gold))
    

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    return [i for i in investors if i["profitReturn"] < 10]

def getAdventuringInvestors(investors:list) -> list:
    return [i for i in investors if i["adventuring"] and i["profitReturn"] < 10]

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    totaal = 0
    AdventuringInvestors = getAdventuringInvestors(investors)
    for i in range(len(AdventuringInvestors)):
        totaal += getItemsValueInGold(gear)

    totaal += getJourneyFoodCostsInGold(len(AdventuringInvestors),len(AdventuringInvestors))
    totaal += getTotalRentalCost(len(AdventuringInvestors), len(AdventuringInvestors))
    return totaal

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    humans = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    totaal = int(leftoverGold / (humans + horses))
    return totaal

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    goldANight = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)
    humans =  goldANight * people 
    horsesGold = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)
    horseANight= horsesGold * horses 
    totaal = round((humans + horseANight) * nightsInInn,2)
    return totaal


##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    lijst = []
    for investor in investors:
        if investor['profitReturn'] < 10:
            lijst.append(round(investor['profitReturn'] / 100 * profitGold,2) )
    return lijst

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    deel = 0
    for delen in investorsCuts:
        deel += delen
    totaal = round((profitGold - deel) / fellowship,2)
    return totaal

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()