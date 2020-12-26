from django.db import models

# Create your models here.
class Question (models.Model) :

	question_text = models.CharField (max_length = 200)

	question_choice_1 = models.CharField (max_length = 50)
	question_choice_2 = models.CharField (max_length = 50)
	question_choice_3 = models.CharField (max_length = 50)
	question_choice_4 = models.CharField (max_length = 50)

	question_answer = models.IntegerField (default = -1)

	question_subject = models.CharField (max_length = 50, default='Other')

	question_source = models.CharField (max_length = 50, default='Anonymous')

	question_approved = models.BooleanField (default = False)

	def __str__ (self) :
		return self.question_text