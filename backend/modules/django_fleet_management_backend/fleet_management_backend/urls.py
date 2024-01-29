from django.urls import path
from .views import authenticate_user, fetch_equipment_data

urlpatterns = [
    path('authenticate/', authenticate_user, name='authenticate_user'),
    path('equipment/', fetch_equipment_data, name='fetch_equipment_data'),
]