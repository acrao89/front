import datetime

from django import forms

from .models import CollectEmail 

class CollectEmailForm(forms.ModelForm):
	class Meta:
		model = CollectEmail