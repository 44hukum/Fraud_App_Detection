from django.urls import path 
from .views import review_analysis

urlpatterns = [
    path('',review_analysis,name='review_analysis')
]
