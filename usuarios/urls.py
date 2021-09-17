from django.urls import path

from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashbord', views.dashbord, name='dashbord'),    
    path('cria/receita', views.cria_receita, name='cria_receita'),
    path('deleta/<int:receita_id>', views.deleta_receita, name='deleta_receita'),
]