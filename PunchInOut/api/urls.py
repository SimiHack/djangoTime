from django.urls import path
# from banner import views
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("time", views.time_view_set, name='time'),  
 
]

urlpatterns = format_suffix_patterns(urlpatterns)