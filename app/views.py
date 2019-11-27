from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
	title = 'hello, world!'

	return render(
		request,
		'app/page/home.template.html',
		{
			'title': title
		}
	)


def about(request):
	title = 'About'

	return render(
		request,
		'app/page/about.template.html',
		{
			'title': title
		}
	)


def contact(request):
	title = 'Contact'

	return render(
		request,
		'app/page/contact.template.html',
		{
			'title': title
		}
	)
