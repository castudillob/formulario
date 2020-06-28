# pages/urls.py
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import contact
from .views import HomePageView, AboutPageView # new

urlpatterns = [
     path('admin/', admin.site.urls),
     path('contact/', contact.contact, name='contact'),
     path('about/', AboutPageView.as_view(), name='about'), # new
     path('', HomePageView.as_view(), name='home'),
]