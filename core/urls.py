from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import signup_view, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(next_page='home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='custom_logout'),
    path('blog/', views.blog, name='blog'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path("send-message/", views.send_message, name="send_message"),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('projects/<slug:slug>/', views.project_detail, name='project_details'),
]
