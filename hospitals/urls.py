"""hospitals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('register.urls')),
    path('api/v2/', include('news.urls')),
    path('api/v3/', include('about_us.urls')),
    path('api/v4/', include('services.urls')),
    path('api/v5/', include('contact.urls')),
    path('api/v6/', include('extra.urls')),
    path('api-auth/', include('rest_framework.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
