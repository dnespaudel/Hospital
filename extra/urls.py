from django.urls import path
from extra.views import *

app_name = "extra"

urlpatterns = [
    path('career', CareerListCreateView.as_view()),
    path('career/all', CareerListView.as_view()),
    path('career/<pk>', CareerDetailView.as_view()),
    path('feedback', FeedbackListCreateView.as_view()),
    path('feedback/all', FeedbackListView.as_view()),
    path('feedback/<pk>', FeedbackDetailView.as_view()),
    path('appointment', AppointmentListCreateView.as_view()),
    path('appointment/all', AppointmentListView.as_view()),
    path('appointment/<pk>', AppointmentDetailView.as_view()),
]