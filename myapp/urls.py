from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    url(r'^detect$', views.detect, name='detect'),
    path('accounts/profile/',views.profile, name='profile'),
    path('accounts/profile/history',views.patienthistory, name='history'),
    path('accounts/profile/display', views.search, name = 'display'),
    path('accounts/profile/display/delete/<int:patient_id>', views.delete_patienthistory, name='delete_history'),
    path('accounts/profile/display/update/<int:patient_id>', views.update_patienthistory, name='update_history'),
]
