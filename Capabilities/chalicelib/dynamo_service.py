from pprint import pprint
import boto3
import uuid
import json

from business_card import BusinessCard


class DynamoService:
    def __init__(self, table_name):
        self.table_name = table_name
        self.dynamodb = boto3.client('dynamodb')

    def store_card(self, card: BusinessCard):

        # Ensure primary key - low collision
        card.card_id = str(uuid.uuid4())
        response = self.dynamodb.put_item(
            TableName=self.table_name,
            Item=card.toDynamoFormat()
        )
        return response

    def update_card(self, card: BusinessCard):
        response = self.dynamodb.update_item(
            TableName=self.table_name,
            Key={'card_id': {'S': str(card.card_id)}},
            AttributeUpdates=card.toDynamoFormat(isUpdate=True),
            ReturnValues='UPDATED_NEW'
        )
        return response

    def delete_card(self, card_id):
        response = self.dynamodb.delete_item(
            TableName=self.table_name,
            Key={'card_id': {'S': str(card_id)}}
        )
        return response

    def get_card(self, card_id):
        response = self.dynamodb.get_item(
            TableName=self.table_name,
            Key={'card_id': {'S': card_id}}
        )
        return response

    def search_cards(self, filter=None, sort=None):
        response = self.dynamodb.scan(
            TableName=self.table_name,
            Limit=10,
            ProjectionExpression= "card_id, card_names, email_addresses, company_name",
            # FilterExpression='card_names = :filter_criteria',
            # ExpressionAttributeValues={
            #     ':filter_criteria': {'S': filter}
            # }
        )
        return response


if __name__ == '__main__':

    dynamo = DynamoService('BusinessCards')

    # for idx in range(1,51,1):
    #     card = BusinessCard(12345, f'Nero{idx}', [55567890], [
    #                     'pepe@pepe.com'], f'NeroCorp{idx}', 'www.nero.com.co', f'123-{idx} address road')
    #     response = dynamo.store_card(card)
    #     print('Card Created')
    #     pprint(response)

    response = dynamo.search_cards('Nero1')
    print('Search filter')
    print(response)

    # response = dynamo.get_card('')

    # print('Card 2 Retrieved')
    # pprint(response)

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
