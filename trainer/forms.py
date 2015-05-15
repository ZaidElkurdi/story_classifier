from django import forms

CATEGORY_CHOICES = (('bug', 'Bug'),
                   ('user_interface', 'User Interface'),
                   ('database', 'Database'),
                   ('optimization', 'Optimization'),
                   ('crash', 'Crash'))

class AddDatumForm(forms.Form):
	text = forms.CharField(max_length=256,
		widget=forms.Textarea(attrs={'rows':4, 'cols':40}))

	categories = forms.MultipleChoiceField(required=True,
        widget=forms.CheckboxSelectMultiple, choices=CATEGORY_CHOICES)

class ClassifyRequestForm(forms.Form):
	query = forms.CharField(max_length=256,
		widget=forms.TextInput(attrs={'size':100}))

class JSONImportForm(forms.Form):
	json_data = forms.CharField(max_length=10000,
		widget=forms.Textarea(attrs={'rows':4, 'cols':80}))