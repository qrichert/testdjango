from django.http import HttpResponse
from django.shortcuts import render

import json

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

	if 'contact[message]' in request.POST:
		message = request.POST.get('contact[message]', None)

		if message:
			return HttpResponse(json.dumps({
				'message': "Thank you! We will answer shortly!",
				'status': 'SUCCESS'
			}))
		else:
			return HttpResponse(json.dumps({
				'message': "The form contains errors.",
				'status': 'ERROR'
			}))

	return render(
		request,
		'app/page/contact.template.html',
		{
			'title': title
		}
	)
