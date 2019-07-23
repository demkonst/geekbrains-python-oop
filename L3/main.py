import json
import requests

iataUrl = 'http://autocomplete.travelpayouts.com/places2?term={}'

cityFrom = input('Откуда: ')
res = requests.get(iataUrl.format(cityFrom)).text
resJson  = json.loads(res)
iataFrom = resJson[0]['code']
print('IATA: {}'.format(iataFrom))

cityTo = input('Куда: ')
res = requests.get(iataUrl.format(cityTo)).text
resJson  = json.loads(res)
iataTo = resJson[0]['code']
print('IATA: {}'.format(iataTo))

pricesUrl = 'http://min-prices.aviasales.ru/calendar_preload?one_way=true&origin={}&destination={}'

res = requests.get(pricesUrl.format(iataFrom,iataTo)).text
resJson  = json.loads(res)
minPrice = resJson['best_prices'][0]['value']
print('Минимальная цена: {}'.format(minPrice))