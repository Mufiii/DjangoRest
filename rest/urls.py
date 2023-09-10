
from django.contrib import admin
from django.urls import path , include
from restapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person_detail/<int:pk>', views.person_detail),
    path('person_detail/', views.person_list),
]
 