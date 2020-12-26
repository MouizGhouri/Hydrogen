from django import forms

answerChoices = (('1', 'Option 1'), 
                 ('2', 'Option 2'), 
                 ('3', 'Option 3'), 
                 ('4', 'Option 4'))

subjectChoices = (('Maths', 'Maths'),
                  ('Physics', 'Physics'),
                  ('Chemistry', 'Chemistry'),
                  ('Biology', 'Biology'),
                  ('English', 'English'),
                  ('Other', 'Other'))

class SubmissionForm (forms.Form):

    username = forms.CharField (label='Name (Optional)', required=False, help_text='The name of this question\'s source (your name), that will be displayed to the users viewing this question.', max_length=50)

    question = forms.CharField (label='Question', max_length=250)

    choice_1 = forms.CharField (label='Option 1', max_length=100)
    choice_2 = forms.CharField (label='Option 2', max_length=100)
    choice_3 = forms.CharField (label='Option 3', max_length=100)
    choice_4 = forms.CharField (label='Option 4', max_length=100)

    answer = forms.ChoiceField (label="Correct Option", choices = answerChoices)

    subject = forms.ChoiceField (label="Subject", choices = subjectChoices)