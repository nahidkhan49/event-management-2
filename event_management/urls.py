
from django.contrib import admin
from django.urls import path,include
from event.views import home



urlpatterns = [
    path('admin/', admin.site.urls),
    path("event/", include("event.urls")),
    path("users/", include("users.urls")),
    path('',home,name='home'),
]
