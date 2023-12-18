from django.urls import path
from applications.dashboard import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('chart', views.chart, name='chart')
]