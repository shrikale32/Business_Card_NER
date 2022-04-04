import json
from locale import format_string


class BusinessCard:

    def __init__(self,
                 card_id=-1,
                 names='',
                 telephone_numbers=[],
                 email_addresses=[],
                 company_name='',
                 company_website='',
                 company_address=''):
        self.card_id = card_id
        self.names = str(names)
        self.telephone_numbers = telephone_numbers
        self.email_addresses = email_addresses
        self.company_name = company_name
        self.company_website = company_website
        self.company_address = company_address
        
        self.names = self._format_strings(self.names, all_caps=True)
        self.company_address = self._format_strings(self.company_address)
    
    def _format_strings(self, value, all_caps=False):
        response = str(value).strip()
        if all_caps:
            response = response.capitalize()
        return response

    def __repr__(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __str__(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def toDynamoFormat(self, isUpdate=False):

        value = {
            'card_id': {'S': str(self.card_id)},
            'names': {'S': self.names},
            'telephone_numbers': {'NS': [str(tn) for tn in self.telephone_numbers]},
            'email_addresses': {'SS': self.email_addresses},
            'company_name': {'S': self.company_name},
            'company_website': {'S': str(self.company_website)},
            'company_address': {'S': self.company_address},
        }

        if isUpdate:
            value = {
                'names': {'Value': {'S': self.names}, 'Action': 'PUT'},
                'telephone_numbers': {'Value': {'NS': [str(tn) for tn in self.telephone_numbers]},  'Action': 'PUT'},
                'email_addresses': {'Value': {'SS': self.email_addresses},  'Action': 'PUT'},
                'company_name': {'Value': {'S': self.company_name},  'Action': 'PUT'},
                'company_website': {'Value': {'S': str(self.company_website)},  'Action': 'PUT'},
                'company_address': {'Value': {'S': self.company_address},  'Action': 'PUT'}
            }
        return value
