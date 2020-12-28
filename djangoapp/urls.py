
from django.urls import path , include
from . import views
urlpatterns = [
   path('',views.home,name="appHomePage"),
   path('aboutus',views.about,name="Aboutus"),
   path('htmlpage',views.page,name="htmlpage")
]

