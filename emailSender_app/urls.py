from django.urls import path
from . import views
 
urlpatterns = [
  path('', views.home, name='home'),
  path("emailForm", views.send_email, name="emailcreate"),
  path("thankYou", views.thankYoupage, name="thankYou"),
]