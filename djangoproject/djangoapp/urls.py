from .  import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    #path('operation/',views.operation,name='operation')
 ]
