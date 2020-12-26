import json

from django.core import serializers

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .models import Question
from .forms import SubmissionForm

# Create your views here.

def index (request) :
	template = loader.get_template ('mcqs/index.html')
	return HttpResponse (template.render ())

def random_question (request) :

	question_objects = serializers.serialize ('json', Question.objects.filter (question_approved=True))

	content = {
		"questions": question_objects,
	}

	return render (request, 'mcqs/random_question.html', content)

def contribute (request) :

	if request.method == 'POST':

		form = SubmissionForm (request.POST)

		if form.is_valid ():

			username = form.cleaned_data ['username']

			question = form.cleaned_data ['question']

			choice_1 = form.cleaned_data ['choice_1']
			choice_2 = form.cleaned_data ['choice_2']
			choice_3 = form.cleaned_data ['choice_3']
			choice_4 = form.cleaned_data ['choice_4']

			answer = form.cleaned_data ['answer']

			subject = form.cleaned_data ['subject']

			Question (question_source=username if username is not None else 'Anonymous', question_text=question, question_choice_1=choice_1, question_choice_2=choice_2, question_choice_3=choice_3, question_choice_4=choice_4, question_answer=answer, question_subject=subject).save ()

			response = HttpResponseRedirect ('/contribute/')

			response.set_cookie ('contributed', '1')

			return response

	else :

		form = SubmissionForm () 

	return render (request, 'mcqs/contribute.html', {'form': form, 'contributed': request.COOKIES ['contributed'] if 'contributed' in request.COOKIES else '0'})

def detail (request, question_id) :
	return HttpResponse ("This is details regarding a specific MCQ.")
