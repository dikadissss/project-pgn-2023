from django.urls import path
from applications.checklist import views

app_name = 'checklist'
urlpatterns = [
    path('toast', views.toast, name='toast')
]