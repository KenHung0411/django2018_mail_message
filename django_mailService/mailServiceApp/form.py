#from.py 
from django import forms

class ContactForm(forms.Form):
	names = forms.CharField(max_length = 100, required=True) 
	email = forms.EmailFiled()
	message = forms.CharField(widget=forms.TextArea, required=True)

	def __init__(self,*args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)

		self.fields['name'].attrs = {'class': 'form-control'}
		self.fields['email'].attrs = {'class': 'form-control'}
		self.fields['message'].attrs = {'class': 'form-control'}

