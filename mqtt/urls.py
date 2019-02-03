from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('tenMin', views.tenMin, name='tenMin'),
    path('shed', views.shed, name='shed'),
    #path('', views.index, {'pagename': ''}, name='home'),
    #path('<str:pagename>', views.index, name='index'),
]