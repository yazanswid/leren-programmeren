

gastheer = input('Wie is de gastheer?: ').strip()  

gasten = False
drank = False
chips = False


naam = "yazan"  
slb_naam = "oorschot"  
gasten = int(input("Hoeveel gasten zijn er? "))



is_gastheer_aanwezig = bool(gastheer)  


start_condition_1 = is_gastheer_aanwezig or gasten

start_condition_2 = is_gastheer_aanwezig or (gasten and chips and drank)

start_condition_3 = not (chips and not drank)

start_condition_4 = not (gasten and not (chips or drank))

start_condition_5 = is_gastheer_aanwezig and drank

start_condition_6 = not (chips and not (gasten or is_gastheer_aanwezig or drank))

genoeg_gasten = 4 <= gasten <= 20 

altijd_feest = gastheer == naam
nooit_feest = gastheer == slb_naam


if start_condition_1 and start_condition_2 and start_condition_3 and start_condition_4 and start_condition_5 and start_condition_6 and altijd_feest and genoeg_gasten:
    print("Het feest kan beginnen!")
else:
    print(f"No Party")





