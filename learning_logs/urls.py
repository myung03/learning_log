from django.urls import path
from . import views 

"""For learning_logs app"""
app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    #topics page 
    path('topics/', views.topics, name='topics'),
    #topic page
    path('topics/<int:topic_id>', views.topic, name='topic'),
    #add topic page 
    path('new_topic/', views.new_topic, name='new_topic'),
    #add entry to topic page 
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #edit entry page 
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]