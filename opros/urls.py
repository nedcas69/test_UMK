from django.urls import path

from .views import *

urlpatterns = [
    path('', categories, name='categories'),
    path('questions/<slug:quiz_slug>/', index, name='index'),
    path('user_auth/<slug:quiz_slug>/', user_auth, name='user_auth'),
    path('results/<slug:quiz_slug>/', results, name='results_user'),
    
]