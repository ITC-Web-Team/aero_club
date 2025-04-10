"""aeroclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from aero_club import views
from aero_club.views import ListBlogView, SingleBlogView, CreateBlogView, UpdateBlogView, DeleteBlogView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('events/', views.events, name='aero-events'),
    path('gallery/', views.gallery, name='aero-gallery'),
    path('about/', views.about, name='aero-about'),
    path('team/', views.teampage, name='aero-teampage'),
    
    # Blog URLs
    path('blogs/', ListBlogView.as_view(), name="aero-blogs"),
    path('blogs/<int:pk>/', SingleBlogView.as_view(), name="single"),
    path('blogs/new/', CreateBlogView.as_view(), name="new"),
    path('blogs/<int:pk>/edit/', UpdateBlogView.as_view(), name="edit"),
    path('blogs/<int:pk>/delete/', DeleteBlogView.as_view(), name='delete'),
    
    # Project URLs
    path('projects/itsp/', views.itsp_projects, name="aero-itsp"),
    path('projects/other/', views.other_projects, name="aero-other"),
    path('projects/glider/', views.glider_projects, name="aero-glider"),
]
