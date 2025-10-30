from django.urls import path
from . import views
urlpatterns = [
    path('',views.jijarformat,name='jijar'),
    path('result',views.add,name='resultsss'),
]