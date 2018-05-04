from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:qid>/',views.details,name='details'),
    path('<int:qid>/results/',views.results,name='results'),
    path('<int:qid>/votes/',views.votes,name='votes'),
]
