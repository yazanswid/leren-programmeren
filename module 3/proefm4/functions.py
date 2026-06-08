import math
import time
from termcolor import colored
from data import *

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return amount / 50

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    return (copper2gold(personCash["copper"])+ silver2gold(personCash["silver"]) + platinum2gold(personCash["platinum"]) + personCash["gold"])

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
      total_copper = (people * COST_FOOD_HUMAN_COPPER_PER_DAY + horses * COST_FOOD_HORSE_COPPER_PER_DAY) * JOURNEY_IN_DAYS
      return round(copper2gold(total_copper), 2)


##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
     return [item for item in list if item.get(key) == value]

def getAdventuringPeople(people:list) -> list:
     return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
        return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
     return getAdventuringPeople(getShareWithFriends(friends))

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    horse_cost_gold = silver2gold(COST_HORSE_SILVER_PER_DAY * horses * JOURNEY_IN_DAYS)
    weeks = math.ceil(JOURNEY_IN_DAYS / 7)
    tent_cost_gold = COST_TENT_GOLD_PER_WEEK * tents * weeks
    return round(horse_cost_gold + tent_cost_gold, 2)

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    if not items:
        return ''

    parts = []
    for item in items:
        amount = item.get('amount', 0)
        unit = item.get('unit', '')
        name = item.get('name', '')
        if unit:
            parts.append(f"{amount}{unit} {name}")
        else:
            parts.append(f"{amount} {name}")

    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return ' & '.join(parts)
   
    return ', '.join(parts[:-1]) + ' & ' + parts[-1]

def getItemsValueInGold(items:list) -> float:
    total = 0.0
    for item in items:
        amt = item.get('amount', 0)
        price = item.get('price', {})
        price_amount = price.get('amount', 0)
        price_type = price.get('type', 'gold')

        
        total_price = price_amount * amt

        
        if price_type == 'copper':
            total += copper2gold(total_price)
        elif price_type == 'silver':
            total += silver2gold(total_price)
        elif price_type == 'platinum':
            total += platinum2gold(total_price)
        else:  
            total += total_price

    return round(total, 2)

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    return sum([getPersonCashInGold(person['cash']) for person in people], 0.0)

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

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