a=5
b=3
c=2

# if statement 1
if (a==6 and b==4 or c==2):
   print("De conditie is waar")
else: 
   print("De conditie is niet waar")    

# if statement 2
if (a==6 and (b==4 or c==2)):
   print("De conditie is waar")
else:
   print("De conditie is niet waar")


print("UITLEG: sta1 gebruikt de volgorde waar (or) later beoordeeld als waar, sta2 beoordeeld binnen het haakjes eerst waardoor (and) belangerijke wordt en dus moet beide voorwaarden voldaan zijn daarom is het onwaar ")