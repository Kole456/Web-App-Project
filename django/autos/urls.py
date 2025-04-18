from django.urls import path
from . import views

app_name = 'autos'

urlpatterns = [
    # Auto routes
    path('', views.AutoListView.as_view(), name='auto_list'),
    path('auto/create/', views.AutoCreateView.as_view(), name='auto_create'),
    path('auto/<int:pk>/update/', views.AutoUpdateView.as_view(), name='auto_update'),
    path('auto/<int:pk>/delete/', views.AutoDeleteView.as_view(), name='auto_delete'),
    
    # Make routes
    path('makes/', views.MakeListView.as_view(), name='make_list'),
    path('make/create/', views.MakeCreateView.as_view(), name='make_create'),
    path('make/<int:pk>/update/', views.MakeUpdateView.as_view(), name='make_update'),
    path('make/<int:pk>/delete/', views.MakeDeleteView.as_view(), name='make_delete'),
]