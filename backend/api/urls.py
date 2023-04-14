from django.urls import path
from .views import InformationView

urlpatterns = [
    path('informations/', InformationView.as_view(), name='informations_list')
]