from django.urls import path
from .views import create_event,create_category,dashboard,category_list,event_list,update_event,delete_event,participant_list,update_category,create_participant,update_participant,delete_participant,delete_category,category_event



urlpatterns = [
    path('create-event/',create_event,name='create-event'),
    path('update-event/<int:id>/',update_event,name='update-event'),
    path('delete-event/<int:id>/',delete_event,name='delete-event'),
    path('event-list/',event_list,name='event-list'),
    path('create-category/',create_category,name='create-category'),
    path('update-category/<int:id>/',update_category,name='update-category'),
    path('delete-category/<int:id>/',delete_category,name='delete-category'),
    path('dashboard/',dashboard,name='dashboard'),
    path('category-list/',category_list,name='category-list'),
    path('participant-list/',participant_list,name='participant-list'),
    path('create-participant/',create_participant,name='create-participant'),
    path('update-participant/<int:id>/',update_participant,name='update-participant'),
    path('delete-participant/<int:id>/',delete_participant,name='delete-participant'),
    path('category-event/<int:id>/',category_event,name='category-event'),
    
]
