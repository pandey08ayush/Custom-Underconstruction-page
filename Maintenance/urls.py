# myapp/urls.py

from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Default route (e.g., /myapp/)
    path('about/', views.about, name='about'),  # About page (e.g., /myapp/about/)
    path('contact/', views.contact, name='contact'),  # Contact page (e.g., /myapp/contact/)
]
