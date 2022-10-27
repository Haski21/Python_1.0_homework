distance = int(input('distance:'))
fuel = int(input('fuel:'))
PRICE_OF_FUEL = 52

temp = distance /100 * fuel * PRICE_OF_FUEL #а как происходит переход от int к float

print('Price of trip is: ', temp)
# print('Price of trip is: ', round(temp,0))  не совсем понятно дял чего round