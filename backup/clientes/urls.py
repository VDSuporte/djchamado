from django.urls import path

from .views import ClientesCreate

from .views import ClientesUpdate
from .views import ClientesDelete
from .views import ClientesList

urlpatterns = [
    path('cadastrar/clientes/', ClientesCreate.as_view(), name='cadastrar-clientes'),

    path('editar/cadastros/clientes/<int:pk>', ClientesUpdate.as_view(), name='editar-cadastros-clientes'),

    path('excluir/cadastros/clientes/<int:pk>', ClientesDelete.as_view(), name='excluir-cadastros-clientes'),

    path('listar/cadastros/clientes/', ClientesList.as_view(), name='listar-cadastros-clientes'),
]
