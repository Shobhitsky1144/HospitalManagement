"""Hospitalmgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.About,name="about"),
    path('',views.Index,name="home"),
    path('view_doctor',views.View_Doctor,name="view_doctor"),
    path('add_doctor',views.Add_Doctor,name="add_doctor"),
    path('add_patient',views.Add_Patient,name="add_patient"),
    path('view_patient',views.View_Patient,name="view_patient"),
    path('add_appointment',views.Add_Appointment,name="add_appointment"),
    path('view_appointment',views.View_Appoinment,name="view_appointment"),
    path('delete_appointment/<int:pid>',views.Delete_Appointment,name="delete_appointment"),
    path('delete_doctor/<int:pid>',views.Delete_Doctor,name="delete_doctor"),
    path('delete_patient/<int:pid>',views.Delete_Patient,name="delete_patient"),
    path('contact/',views.Contact,name="contact"),
    path('admin_login/',views.Login,name="login"),
    path('logout/',views.Logout_admin,name="logout"),

]
