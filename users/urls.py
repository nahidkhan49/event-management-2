from django.urls import path 
from users.views import *

urlpatterns = [
    path('sign_up/',sign_up,name='sign_up'),
    path('sign_in/',sign_in,name='sign_in'),
    path('sign_out/',sign_out,name="sign_out"),
    path("activate/<int:user_id>/<str:token>/",activate_user,name="activate"),
    path('admin_dashboard/',admin_dashboard,name="admin_dashboard"),
    path("<int:user_id>/assign_role/", assign_role, name="assign_role"),
    path("create_group/",create_group,name="create_group"),
    path('group_list/',group_list,name="group_list"),
    path('organizer_dashboard/',organizer_dashboard,name="organizer_dashboard"),
    path('participant_dashboard/',participant_dashboard,name="participant_dashboard"),
    path('no_permission/', no_permission, name='no_permission'),
]
