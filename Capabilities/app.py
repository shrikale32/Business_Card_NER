from chalice import Chalice
from chalicelib import storage_service
from chalicelib import recognition_service
from chalicelib import named_entity_recognition_service #importing the named entity recognition service

import base64

#####
# chalice app configuration
#####
app = Chalice(app_name='Capabilities')
app.debug = True

#####
# services initialization
#####
storage_location = 'contentcen301150258.aws.ai'
storage_service = storage_service.StorageService(storage_location)
recognition_service = recognition_service.RecognitionService(storage_service)
named_entity_recognition_service = named_entity_recognition_service.NamedEntityRecognitionService()



#####
# RESTful endpoints
#####
@app.route('/images', methods = ['POST'], cors = True)
def upload_image():
    """processes file upload and saves file to storage service"""
    request_data = json.loads(app.current_request.raw_body)
    file_name = request_data['filename']
    file_bytes = base64.b64decode(request_data['filebytes'])

    image_info = storage_service.upload_file(file_bytes, file_name)

    return image_info


@app.route('/images/{image_id}/recognize_entities', methods = ['POST'], cors = True)
def recognize_image_entities(image_id):
    """detects then extracts named entities from text in the specified image"""

    MIN_CONFIDENCE = 80.0

    
    text_lines = recognition_service.detect_text(image_id)
    ner_lines = []

    ner_text = ""
    recognized_lines =[]
    

    if float(line['confidence']) >= MIN_CONFIDENCE:
        for line in text_lines:
            recognized_lines.append(
                line['text']
            )

    print(recognized_lines)
    for i in recognized_lines:
        ner_text = ner_text + " " + i
    print(ner_text)

    ner_lines = named_entity_recognition_service.detect_entities(ner_text)
    print(ner_lines, "\n")

    return ner_lines



    





