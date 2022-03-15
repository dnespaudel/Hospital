from django.urls import path
from services.views import *

app_name = "services"

urlpatterns = [
    path('services', ServicesListCreateView.as_view()),
    path('services/all', ServicesListView.as_view()),
    path('services/<pk>', ServicesDetailView.as_view()),
    path('hospital-services', HospitalServicesListCreateView.as_view()),
    path('hospital-services/all', HospitalServicesListView.as_view()),
    path('hospital-services/<pk>', HospitalServicesDetailView.as_view()),

]