import boto3
import boto3.dynamodb
import uuid

from business_card_list import BusinessCardList
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

    def search_cards(self, filter=None, page=1, pagesize=10):
        response = self.dynamodb.scan(
            TableName=self.table_name,
            # If specific columns needs to be displayed in the list view
            # ProjectionExpression="card_id, card_names, email_addresses, company_name",
            FilterExpression='contains(card_names,:filter_criteria) OR '\
            'contains(email_addresses,:filter_criteria) OR '\
            'contains(company_name,:filter_criteria) OR '\
            'contains(company_website,:filter_criteria) OR '\
            'contains(company_address,:filter_criteria) ',
            ExpressionAttributeValues={
                ':filter_criteria': {'S': filter}
            },
        )
        
        # print(response)
        return BusinessCardList(response, page, pagesize)