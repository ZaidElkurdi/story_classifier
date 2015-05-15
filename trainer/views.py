from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.forms import ValidationError
from django.contrib.auth import authenticate, login, logout
import json

from trainer.models import TrainingDatum
from trainer.forms import AddDatumForm, ClassifyRequestForm, JSONImportForm

from trainer.api import submit_classifier_request, convert_training_data_to_json, convert_json_to_training_data
 
def index(request):
	classifier_result = ''
	if 'classifier_result' in request.session.keys():
		classifier_result = request.session['classifier_result']

	datum_form = AddDatumForm()
	query_form = ClassifyRequestForm()
	return render(request, 'index.html', {'query_form': query_form, 'add_datum_form' : datum_form, 'classifier_result' : classifier_result})

def export_json_data(request):
	new_datum = TrainingDatum
	return HttpResponse(convert_training_data_to_json())

def import_json_data(request):
	if request.method == 'POST':
		form = JSONImportForm(request.POST)
		if form.is_valid():
			json_text = form.cleaned_data['json_data']
			op_msg = convert_json_to_training_data(json_text)
			return HttpResponse(op_msg)

	import_form = JSONImportForm()
	return render(request, 'import.html', {'import_form' : import_form})
	

def submit_query(request):
	if request.method == 'POST':
		form = ClassifyRequestForm(request.POST)
		if form.is_valid():
			query = form.cleaned_data['query']
			result = submit_classifier_request(query)
			request.session['classifier_result'] = result
	return HttpResponseRedirect('/')

def add_datum(request):
	if request.method == 'POST':
		form = AddDatumForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['text']
			categories = form.cleaned_data['categories']

			new_datum = TrainingDatum(text=text, categories=categories)
			new_datum.save()

	return HttpResponseRedirect('/')

def json_handler(obj):
	if isinstance(obj, datetime):
		return str(obj.date())
	return str(obj)

def training_data(request):
	if request.is_ajax():
		envelope = {}
 
		logged_data = list(TrainingDatum.objects.all().values())

		data = {
			'logged_data': logged_data
		}

		envelope = {
			'status': 1, 
			'message': "Data Ready",
			'data': data, 
		}

		return HttpResponse(json.dumps(envelope, default=json_handler), content_type='application/json')

	return render_to_response('index.html', context_instance = RequestContext(request))