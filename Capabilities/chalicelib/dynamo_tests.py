from pprint import pprint
from chalicelib.dynamo_service import DynamoService
from chalicelib.business_card import BusinessCard

dynamo = DynamoService('BusinessCards')

### CREATE DUMMY DATA

# for idx in range(1,11,1):
#     card = BusinessCard(12345, f'User_name{idx}', f'Nero{idx}', [55567890], [
#                     'pepe@pepe.com'], f'NeroCorp{idx}', 'www.nero.com.co', f'123-{idx} address road', f'bucket/img-{idx}')
#     response = dynamo.store_card(card)
#     print('Card Created')
#     pprint(response)

### SEARCH FUNCTIONALITY 
# ps = 12
# cards = dynamo.search_cards('nero', 1, ps)
# print(cards.get_list())
# cards = dynamo.search_cards('nero', 2, ps)
# print(cards.get_list())
# cards = dynamo.search_cards('nero', 3, ps)
# cards = dynamo.search_cards('nero', 4, 0)
# print(cards.get_list())
# cards = dynamo.search_cards('nero', 2, 40)
# print(cards.get_list())

### GET CARD FUNCTIONALITY
# card = dynamo.get_card('bb901143-643b-4f46-95b9-696fecffca9f')
# print('Card 2 Retrieved')
# pprint(card)

### CREATE CARD FUNCTIONALITY
# card = BusinessCard(0,'pparker', 'Peter Parker', [555678902], 
#                         ['peter@spidey.com'], 'Spiderman Corp', 'www.spiderman.com', '9987 friendly road',
#                         'bucket//123//img.123')
# response = dynamo.store_card(card)
# print('Card New Created')
# pprint(response)
# pprint(card.card_id)

### UPDATE CARD FUNCTIONALITY
# card.company_name = 'COMP258'
# response = dynamo.update_card(card)
# print('Card Updated')
# pprint(response)

### DELETE CARD FUNCTIONALITY
# response = dynamo.delete_card('bb7f9c49-1d8b-493d-98d6-1165d4d3673c')
# print('Card 1 Removed')
# pprint(response)