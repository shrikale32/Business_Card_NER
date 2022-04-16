from chalice import Chalice
from chalicelib.dynamo_service import DynamoService
from chalicelib.business_card_list import BusinessCardList
from chalicelib.business_card import BusinessCard
from chalicelib import storage_service
from chalicelib import recognition_service
# importing the named entity recognition service
from chalicelib import named_entity_recognition_service

import base64
import json
from urllib.parse import parse_qs

#####
# chalice app configuration
#####
app = Chalice(app_name='Capabilities')
app.debug = True

#####
# services initialization
#####
storage_location = 'contentcen301150258.aws.ai'
table_name = 'BusinessCards'
storage_service = storage_service.StorageService(storage_location)
recognition_service = recognition_service.RecognitionService(storage_service)
named_entity_recognition_service = named_entity_recognition_service.NamedEntityRecognitionService()
dynamo_service = DynamoService(table_name)


#####
# RESTful endpoints
#####
@app.route('/images', methods=['POST'], cors=True)
def upload_image():
    """processes file upload and saves file to storage service"""
    request_data = json.loads(app.current_request.raw_body)
    file_name = request_data['filename']
    file_bytes = base64.b64decode(request_data['filebytes'])

    image_info = storage_service.upload_file(file_bytes, file_name)

    return image_info


@app.route('/images/{image_id}/recognize_entities', methods=['POST'], cors=True)
def recognize_image_entities(image_id):
    """detects then extracts named entities from text in the specified image"""

    MIN_CONFIDENCE = 80.0

    text_lines = recognition_service.detect_text(image_id)
    ner_lines = []

    ner_text = ""
    recognized_lines = []

    # appending lines with confidence score > 80 to an empty list
    for line in text_lines:
        if float(line['confidence']) >= MIN_CONFIDENCE:
            recognized_lines.append(
                line['text']
            )

    print(recognized_lines)

    # appending all recognized lines together to form a text string
    for i in recognized_lines:
        ner_text = ner_text + " " + i
    print(ner_text)

    # calling the named_entity_recognition_service to detected entities from the recognized text
    ner_lines = named_entity_recognition_service.detect_entities(ner_text)
    print(ner_lines, "\n")

    return ner_lines


@app.route('/cards/{query}/{page}/{pagesize}', methods=['GET'], cors=True)
def get_cards(query, page, pagesize):
    """Get the paginated list of cards from a query"""
    cardlist_container = dynamo_service.search_cards(query, page, pagesize)
    # This object has 3 main methods: get_list(), get_count(), get_numpages()
    cards = cardlist_container.get_list()
    print( [c.names for c in cards] )
    

@app.route('/cards', methods=['POST'], cors=True,
           content_types=['application/json'])
def post_card():
    """Creates a card"""
    parsed = parse_qs(app.current_request.json_body)
    
    card = BusinessCard(parsed['card_id'], 
                        parsed['user_id'], 
                        parsed['user_names'], 
                        parsed['telephone_numbers'],
                        parsed['email_addresses'], 
                        parsed['company_name'], 
                        parsed['company_website'],
                        parsed['company_address'],
                        parsed['image_storage'])
    
    result = dynamo_service.store_card(card) # True  / False
    new_card_id = card.card_id # Created by the service
    
    


@app.route('/cards', methods=['PUT'], cors=True,
           content_types=['application/json'])
def put_card():
    """Updates a card"""
    parsed = parse_qs(app.current_request.json_body)
    card = BusinessCard(parsed['card_id'], 
                        parsed['user_id'], 
                        parsed['user_names'], 
                        parsed['telephone_numbers'],
                        parsed['email_addresses'], 
                        parsed['company_name'], 
                        parsed['company_website'],
                        parsed['company_address'],
                        parsed['image_storage'])
    result = dynamo_service.update_card(card) # True  / False
    

@app.route('/cards/{card_id}', methods=['DELETE'], cors=True)
def delete_card(card_id):
    """Deletes a card"""
    dynamo_service.delete_card(card_id)


@app.route('/cards/{card_id}', methods=['GET'], cors=True)
def get_card(card_id):
    """Query a specific card by id"""
    return dynamo_service.get_card(card_id)
