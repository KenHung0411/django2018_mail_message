from django.shortcuts import render

from django.contrib import messages
from django.core.mail import send_mail
# from Demo.Settings import EMAIL_HOST_USER
# from demoapp.forms import Contactform

# Create your views here.

def index(request):
	posts = {"page":"home"
	
	}
	return render(request,'mailServiceApp/index.html',posts)


def about(request):
	posts = {"page":"contact"
	
	}
	return render(request,'mailServiceApp/contact.html',posts)

def send_mail(contact_form_data):
	email_message_format = "name: %s \n email: %s \n message: %s \n"
	name = contact_from_data.get('name','')
	message = contact_form_data.get('message','')
	email = contact_form_data.get('email','')
	email_message_format = email_message_format.format(name,email,message)


	'''
	send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
	'''
	send_mail('Demo Website',
		     email_message_format,
		     EMAIL_HOST_USER,
		     [EMAIL_HOST_USER],
		     fail_silently =False)

def contact_us(request):

	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			send_mail(form.cleaned_data)
			message.success(request, "Your response has been record")
		else:
			form = ContactForm()

	return render(request, 'contact.html',{'page':'contact', 'form':form})

def clear(request):
	form = ContactForm()
	message.error(request, 'Firld cleared successfully')

	return render(request, 'contact.html', {'page':'contact', 'form': form})



