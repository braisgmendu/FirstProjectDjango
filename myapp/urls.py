from django.urls import path
from django.views.generic import TemplateView 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('comment/', views.comment_view, name='comment'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]
