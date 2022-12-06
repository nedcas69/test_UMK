from django.urls import path

from .views import *

urlpatterns = [
    path('', categories, name='categories'),
    path('questions/<int:quiz_id>/<int:user_id>/', index, name='index'),
    path('user_auth/<int:quiz_id>/', user_auth, name='user_auth'),
    path('results/<int:user_id>/', results, name='results'),
    
]