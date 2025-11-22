"""URL configuration for the `core` app.

Provides view routes and registers the DRF router for API endpoints.
Include `core.urls` from the project-level `urls.py` to activate these
routes.
"""

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from . import api
from typing import List

app_name = 'core'

router = DefaultRouter()
router.register(r'api/custommodels', api.CustomModelViewSet,
                basename='custommodel')

urlpatterns: List = [
    path('', views.home, name='home'),
    path('custommodels/', views.CustomModelListView.as_view(),
         name='custommodel_list'),
    path('custommodels/add/', views.CustomModelCreateView.as_view(),
         name='custommodel_add'),
    path('custommodels/<int:pk>/', views.CustomModelDetailView.as_view(),
         name='custommodel_detail'),
]

# Note: include `router.urls` from project urls if you want the API endpoints
