from datetime import date

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from .forms import CollectEmailForm

def collectemail(request):
	form = CollectEmailForm(request.POST or None)
	if form.is_valid():
		this_form = form.save(commit=False)
		this_form.save()
		message = 'Thank you for signing up, we will be in touch!'
		return render_to_response('thankyou.html', {'message':message}, context_instance = RequestContext(request))

	return render_to_response('form.html', locals(), context_instance = RequestContext(request))