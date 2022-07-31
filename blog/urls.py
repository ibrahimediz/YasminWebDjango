from django.urls import path
from . import views

urlpatterns = [
    path('',views.bloglist,name='bloglist'),
    path('<int:pk>/',views.blogdetail,name='blogdetail'),
    path('add/',views.blogadd,name='blogadd'),
    path('edit/<int:pk>/',views.blogedit,name='blogedit'),
]
