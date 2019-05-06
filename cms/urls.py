from django.urls import path
from . import views
from .models import Story

app_name='cms'
urlpatterns=[
    path(r'^<slug:slug>/',views.story_detail,name='story'),
    path(r'',views.story_list,name='home'),
    path(r'category/<slug:slug>/',views.category,name='category'),
    path(r'search/',views.search,name='search'),
]