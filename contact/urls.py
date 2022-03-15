from django.urls import path
from contact.views import *

app_name = "contact"

urlpatterns = [
    path('contact-us', ContactUsListCreateView.as_view()),
    path('contact-us/all', ContactUsListView.as_view()),
    path('contact-us/<pk>', ContactUsDetailView.as_view()),
    path('get-connected', GetConnectedListCreateView.as_view()),
    path('get-connected/all', GetConnectedListView.as_view()),
    path('get-connected/<pk>', GetConnectedDetailView.as_view()),
    path('social-media', SocialMediaListCreateView.as_view()),
    path('social-media/all', SocialMediaListView.as_view()),
    path('social-media/<pk>', SocialMediaDetailView.as_view()),

]