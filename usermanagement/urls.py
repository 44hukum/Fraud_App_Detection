from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout_out,name="logout"),
    path('home',views.home,name='home'),
    path('review',views.review,name='review')
]
