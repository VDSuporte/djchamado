from django.urls import path

from .views import CavalosCreate

from .views import CavalosUpdate
from .views import CavalosDelete
from .views import CavalosList

urlpatterns = [
    path('cadastrar/cavalos/', CavalosCreate.as_view(), name='cadastrar-cavalos'),

    path('editar/cadastros/cavalos/<int:pk>', CavalosUpdate.as_view(), name='editar-cadastros-cavalos'),

    path('excluir/cadastros/cavalos/<int:pk>', CavalosDelete.as_view(), name='excluir-cadastros-cavalos'),

    path('listar/cadastros/cavalos/', CavalosList.as_view(), name='listar-cadastros-cavalos'),
]
