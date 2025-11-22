from django.urls import path
from . import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from . import api

app_name = 'core'

router = DefaultRouter()
router.register(r'api/custommodels', api.CustomModelViewSet,
                basename='custommodel')

urlpatterns = [
    path('', views.home, name='home'),
    path('custommodels/', views.CustomModelListView.as_view(),
         name='custommodel_list'),
    path('custommodels/add/', views.CustomModelCreateView.as_view(),
         name='custommodel_add'),
    path('custommodels/<int:pk>/', views.CustomModelDetailView.as_view(),
         name='custommodel_detail'),
]

# Include router urls in the project's urls.py by importing core.urls
