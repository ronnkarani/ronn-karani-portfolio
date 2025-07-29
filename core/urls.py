from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path("send-message/", views.send_message, name="send_message"),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('projects/<slug:slug>/', views.project_detail, name='project_details'),
]
