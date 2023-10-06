from django.urls import path
from applications.focal import views

app_name = 'focal'
urlpatterns = [
    path('', views.focal, name='focal')
]