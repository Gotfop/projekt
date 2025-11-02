"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from first import views
from first.views import TomatoListView, TomatView, CreateTomatView, DeleteTomatView, CreateOderView, api_search
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.first,name='qwe'),
    path('hi/', views.second),
    path('helo/',views.hello, name='hello'),
    path('tomat/',views.tomati),
    path('tomat/<int:pk>',views.tomat),
    
    path('',TomatoListView.as_view(),name='list'),
    path('detailtomat/<int:pk>', TomatView.as_view(),name='detailtomat'),
    path('createtomat/',CreateTomatView.as_view(),name='createtomat'),
    path('deletetomat/<int:pk>',DeleteTomatView.as_view(),name='deletetomat'),
    path('createoder', CreateOderView.as_view(), name='createoder'),
    path('api/search',api_search)

]
if settings.DEBUG:
    from django.conf.urls.static  import static

    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)