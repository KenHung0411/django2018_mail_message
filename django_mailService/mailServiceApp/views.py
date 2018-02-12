from django.shortcuts import render

# Create your views here.

def index(request):
	posts = {"hello":"helloworld"
	
	}
	return render(request,'mailServiceApp/index.html',posts)
