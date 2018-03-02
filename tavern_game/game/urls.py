from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rations/', views.rations, name='rations'),
    path('add_rations/', views.add_rations, name='add_rations'),
    path('rich_people/', views.rich_people, name='rich_people'),
    path('rich_fortune/', views.rich_fortune, name='rich_fortune'),
    path('login/', LoginView.as_view(template_name='game/login.html', redirect_field_name='index'), name='login'),
    path('logout/', views.user_logout, name='logout'),
]
