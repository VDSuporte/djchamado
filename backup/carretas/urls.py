from django.urls import path

from .views import CarretasCreate
from .views import CarretasUpdate
from .views import CarretasDelete
from .views import CarretasList
from .views import AcessoriosCreate
from .views import AcessoriosUpdate
from .views import AcessoriosDelete
from .views import AcessoriosList
from . import views

urlpatterns = [
    path('cadastrar/carretas/', CarretasCreate.as_view(), name='cadastrar-carretas'),

    path('editar/cadastros/carretas/<int:pk>', CarretasUpdate.as_view(), name='editar-cadastros-carretas'),

    path('excluir/cadastros/carretas/<int:pk>', CarretasDelete.as_view(), name='excluir-cadastros-carretas'),

    path('listar/cadastros/carretas/', CarretasList.as_view(), name='listar-cadastros-carretas'),

    path('cadastrar/acessorios/', AcessoriosCreate.as_view(), name='cadastrar-acessorios'),

    path('editar/cadastros/acessorios/<int:pk>', AcessoriosUpdate.as_view(), name='editar-cadastros-acessorios'),

    path('excluir/cadastros/acessorios/<int:pk>', AcessoriosDelete.as_view(), name='excluir-cadastros-acessorios'),

    path('listar/cadastros/acessorios/', AcessoriosList.as_view(), name='listar-cadastros-acessorios'),

    path('carreta/<int:carreta_id>/acessorios/', views.acessorios_carreta, name='acessorios-cadastros-carretas'),

]