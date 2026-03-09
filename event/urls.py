from django.urls import path
from .views import *



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
    
    path('category-event/<int:id>/',category_event,name='category-event'),
    path('', event_list, name='event-list'),
    path('rsvp/<int:id>/', rsvp_event, name='rsvp-event'),
]
