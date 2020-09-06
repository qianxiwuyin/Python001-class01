from django.urls import path
from . import views

urlpatterns = [
    #path('',views.open),
    path('dianping/',views.movie_short),
    path('login',views.login2),
]

