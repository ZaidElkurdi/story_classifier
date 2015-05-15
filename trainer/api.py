from django.db import models

from trainer.models import *
from datetime import datetime
from django.utils import timezone
import requests
import json
import string, random

CLASSIFIER_UUID = '' # The UUID of your Watson Natural Language Classifier
WATSON_API_BASE_URL = 'https://gateway.watsonplatform.net/natural-language-classifier-experimental/api/v1/classifiers/'
API_USERNAME = '' # Your classifier username
API_PASSWORD = '' # Your classifier password

def submit_classifier_request(query):
	url = WATSON_API_BASE_URL + CLASSIFIER_UUID + '/classify'
	queryParam = {'text' : query}
	headers = {'Content-Type': 'application/json'}

	r = requests.post(url, auth=(API_USERNAME, API_PASSWORD), data=json.dumps(queryParam), headers=headers)
	try:
		result_json = r.json()
		result_string = ''
		for class_confidence_pair in result_json['classes']:
			class_name = class_confidence_pair['class_name']
			confidence = class_confidence_pair['confidence']
			result_string += str(class_name) + u'\xa0\xa0\xa0\xa0' + str(confidence) + '\n'
		return result_string
	except Exception as e:
		return 'Error decoding JSON!'

def convert_training_data_to_json():
	try:
		logged_data = list(TrainingDatum.objects.all().values())
		for curr_dict in logged_data: curr_dict.pop("id", None)
		return json.dumps(logged_data)
	except Exception as e:
		return 'Error converting data to JSON!'

def convert_json_to_training_data(json_text):
	try:
		json_data = json.loads(json_text)
		print str(json_data)
		if 'training_data' in json_data:
			for class_text_pair in json_data['training_data']:
				text = class_text_pair['text']
				categories = class_text_pair['classes']

				new_datum = TrainingDatum(text=text, categories=categories)
				new_datum.save()
			return 'Successfully imported JSON!'
	except Exception as e:
		return 'Error importing JSON: ' + str(e)
