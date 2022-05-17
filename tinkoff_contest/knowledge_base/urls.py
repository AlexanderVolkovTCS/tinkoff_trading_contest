from django.urls import path

from . import views

urlpatterns = [
    path('', views.KnowledgeBase.as_view(), name='info'),
    path('strategies/', views.Strategies.as_view(), name='info_strats'),
    path('about/', views.About.as_view(), name='info_about'),
    path('contacts/', views.Contacts.as_view(), name='info_contacts'),
]