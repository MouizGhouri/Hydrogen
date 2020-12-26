from django.urls import path

from . import views

urlpatterns = [

	path ('', views.index, name='index'),
	path ('mcqs/', views.random_question, name='random_mcq'),
	path ('contribute/', views.contribute, name='contribution_page'),
	path ('mcqs/<int:question_id>', views.detail, name='detail'),

]