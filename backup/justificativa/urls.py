from django.urls import path

from .views import JustificativaCreate

from .views import JustificativaUpdate
from .views import JustificativaDelete
from .views import JustificativaList

urlpatterns = [
    path('justificativa/abertura/', JustificativaCreate.as_view(), name='justificativa-abertura'),

    path('justificativa/edicao/<int:pk>', JustificativaUpdate.as_view(), name='justificativa-edição'),

    path('justificativa/apagar/<int:pk>', JustificativaDelete.as_view(), name='justificativa-apagar'),

    path('justificativa/lista/', JustificativaList.as_view(), name='justificativa-lista'),
    ]