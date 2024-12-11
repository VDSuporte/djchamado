from django.urls import path

from .views import ChamadosCreate

from .views import ChamadosUpdate
from .views import ChamadosDelete
from .views import ChamadosList
from .views import solicitar_chamado
from .views import reverter_status
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('solicitar/chamado/', ChamadosCreate.as_view(), name='chamado'),

    path('chamados/edicao/<int:pk>', ChamadosUpdate.as_view(), name='chamados-edição'),

    path('chamados/excluir/<int:pk>', ChamadosDelete.as_view(), name='chamados-excluir'),

    path('chamados/listar/', ChamadosList.as_view(), name='listar-chamados'),

    path('solicitar_chamado/', solicitar_chamado, name='solicitar_chamado'),

    path('chamados/reverter-status/<int:pk>/', reverter_status, name='reverter-status'),  # Nova rota
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
