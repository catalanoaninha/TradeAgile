from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dados_funcionarios/',views.user_list_view, name='user_list'),
    path('home/', views.home, name='home'),
    path('cadastro_clientes/', views.cadastro_clientes, name='cadastro_clientes'),
    path('dados_clientes/', views.demonstrativo_tabelas, name='demonstrativo_tabelas'),
    path('galeria_produtos/', views.galeria_produtos, name='galeria_produtos'),
    path('realizar_venda/', views.realizar_venda, name='realizar_venda'),

    path('venda_concluida/', views.obrigado, name='venda_concluida')

]
