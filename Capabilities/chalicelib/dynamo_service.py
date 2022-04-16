import boto3
import boto3.dynamodb
import uuid

from chalicelib.business_card import BusinessCard
from chalicelib.business_card_list import BusinessCardList

class DynamoService:
    """Service to manage interaction with AWS DynamoDB
    """
    def __init__(self, table_name):
        """Constructor

        Args:
            table_name (str): Table name in DynamoDB service
        """
        self.table_name = table_name
        self.dynamodb = boto3.client('dynamodb')

    def store_card(self, card: BusinessCard):
        """Creates a new card record

        Args:
            card (BusinessCard): Card to be included in the DynamoBD

        Returns:
            bool: Operation result
        """
        
        # Ensure primary key - low collision
        card.card_id = str(uuid.uuid4())
        response = self.dynamodb.put_item(
            TableName=self.table_name,
            Item=card.toDynamoFormat()
        )
        return response['ResponseMetadata']['HTTPStatusCode'] == 200

    def update_card(self, card: BusinessCard):
        """Updates a new card record

        Args:
            card (BusinessCard): Card to be updated in the DynamoBD

        Returns:
            bool: Operation result
        """
        response = self.dynamodb.update_item(
            TableName=self.table_name,
            Key={'card_id': {'S': str(card.card_id)}},
            AttributeUpdates=card.toDynamoFormat(isUpdate=True),
            ReturnValues='UPDATED_NEW'
        )
        return response['ResponseMetadata']['HTTPStatusCode'] == 200

    def delete_card(self, card_id):
        """Deletes a card record in DynamoDB

        Args:
            card_id (str): Card unique identifier

        Returns:
            bool: Operation result, true if card does not exist
        """
        response = self.dynamodb.delete_item(
            TableName=self.table_name,
            Key={'card_id': {'S': str(card_id)}}
        )
        return response['ResponseMetadata']['HTTPStatusCode'] == 200

    def get_card(self, card_id):
        """Retrieves card information from DynamoDB

        Args:
            card_id (str): Card unique identifier

        Returns:
            BusinessCard: Card information, None if card_id does not exists
        """
        response = self.dynamodb.get_item(
            TableName=self.table_name,
            Key={'card_id': {'S': card_id}}
        )

        c = None
        if response.__contains__('Item'):
            c = BusinessCard(
                card_id=response['Item']['card_id']['S'],
                user_id=response['Item']['user_id']['S'],
                names=response['Item']['card_names']['S'],
                email_addresses=response['Item']['email_addresses']['SS'],
                telephone_numbers=response['Item']['telephone_numbers']['NS'],
                company_name=response['Item']['company_name']['S'],
                company_website=response['Item']['company_website']['S'],
                company_address=response['Item']['company_address']['S'],
                image_storage=response['Item']['image_storage']['S'],
            )
        return c

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
