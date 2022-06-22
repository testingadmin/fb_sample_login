from django.urls import path
from facebookpage.views import *

urlpatterns = [
    path('', add_show),
]
