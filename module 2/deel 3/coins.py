# name of student: 
# number of student:
# purpose of program: 
# structure of program: 

coinValues = [500,200,100,50,20,10,5,2,1] #
coinsReturned = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}


toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #

while change > 0 and len(coinValues) > 0: #

  coinValue = coinValues.pop(0) #
  nrCoins = change // coinValue #
  coinsReturned[coinValue] = nrCoinsReturned 

  if nrCoins > 0: #
    print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
    change -= nrCoinsReturned * coinValue #
  else:
    print('All change has been returned.')

if change > 0: #
  print('Change not returned: ', str(change) + ' cents') #
  print('Not all required change could be returned with coins.')
else:
 print('All change has been returned.')


print('\nOverview of returned coins:')
for coin, count in coinsReturned.items():
    if count > 0:
        if coin >= 100:
            print(f'{count} coin(s) of {coin // 100} euro')
        else:
            print(f'{count} coin(s) of {coin} cent')

print('done')