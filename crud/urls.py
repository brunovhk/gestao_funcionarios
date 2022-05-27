from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('funcionario/add/', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('funcionario/edit/<int:funcionario_pk>', views.editar_funcionario, name='editar_funcionario'),
    path('funcionario/delete/<int:funcionario_pk>', views.deletar_funcionario, name='deletar_funcionario')
]
