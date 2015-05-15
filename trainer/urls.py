from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^training_data$', views.training_data, name='training_data'),
	url(r'^export_json_data$', views.export_json_data, name='export_json_data'),
	url(r'^import_json_data$', views.import_json_data, name='import_json_data'),
 	url(r'^add_datum$', views.add_datum),
 	url(r'^submit_query$', views.submit_query),
]