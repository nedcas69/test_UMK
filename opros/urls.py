from django.urls import path

from .views import *

urlpatterns = [
    path('', categories, name='categories'),
    path('questions/<int:quiz_id>/', index, name='index'),
    path('user_auth/<int:quiz_id>/', user_auth, name='user_auth'),
    path('results/<int:quiz_id>/', results, name='results_user'),
    
]