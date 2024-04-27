from django.urls import path
from .import views 


urlpatterns = [
    path('',views.index,name='index-url'),
    path('about',views.about,name='about-url'),
    path('contact',views.contact,name='contact-url'),
    path('news',views.news,name='news-url'),
]





