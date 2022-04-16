from pprint import pprint
from Capabilities.chalicelib import dynamo_service

dynamo = dynamo_service('BusinessCards')

# for idx in range(1,31,1):
#     card = BusinessCard(12345, f'User_name{idx}', f'Nero{idx}', [55567890], [
#                     'pepe@pepe.com'], f'NeroCorp{idx}', 'www.nero.com.co', f'123-{idx} address road')
#     response = dynamo.store_card(card)
#     print('Card Created')
#     pprint(response)
# print('Search filter')
# ps = 12
# cards = dynamo.search_cards('nero', 1, ps)
# print(cards.get_list())
# cards = dynamo.search_cards('nero', 2, ps)
# print(cards.get_list())
# cards = dynamo.search_cards('nero', 3, ps)
# print(cards.get_list())
# cards = dynamo.search_cards('nero', 4, ps)
# print(cards.get_list())
# cards = dynamo.search_cards('nero', 5, ps)
# print(cards.get_list())
# cards = dynamo.search_cards('nero', 6, ps)
# print(cards.get_list())
# cards = dynamo.search_cards('nero', 0, ps)
# print(cards.get_list())
# cards = dynamo.search_cards('nero', 4, 0)
# print(cards.get_list())
# cards = dynamo.search_cards('nero', 2, 40)
# print(cards.get_list())

# print(len(cards))
# print(cards)

response = dynamo.get_card('67be7bc1-5aef-4831-a938-e0d2cd532268')
print('Card 2 Retrieved')
pprint(response)

# card2 = BusinessCard(12346, 'Nero2', [555678902], [
#                      'pepe2@pepe.com'], 'NeroCorp2', 'www.nero2.com.co', '234 address road')
# dynamo = DynamoService('BusinessCards')
# response = dynamo.store_card(card2)
# print('Card 2 Created')
# pprint(response)

# card2.company_name = 'COMP258'
# response = dynamo.update_card(card2)
# print('Card 2 Updated')
# pprint(response)

# response = dynamo.delete_card(12345)
# print('Card 1 Removed')
# pprint(response)

# response = dynamo.get_card(12346)
# print('Card 2 Retrieved')
# pprint(response)
