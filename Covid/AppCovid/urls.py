from django.conf import settings
from django.urls import include, path
from .views import home, lista_pacientes, lista_testes, paciente_novo, paciente_update, paciente_delete, testes_novo, \
    testes_update, testes_delete
from django.conf.urls.static import static

urlpatterns = [
                  path('contas/', include('django.contrib.auth.urls')),
                  path('', lista_pacientes, name='home'),
    
                  path('paciente', lista_pacientes, name="lista_paciente"),
                  path('paciente/cadastro', paciente_novo, name="cadastro_paciente"),
                  path('paciente/update/<id>', paciente_update, name="update_paciente"),
                  path('paciente/delete/<id>', paciente_delete, name="delete_paciente"),
    
                  path('testes', lista_testes, name="lista_testes"),
                  path('testes/cadastro', testes_novo, name="cadastro_testes"),
                  path('testes/update/<id>', testes_update, name="update_testes"),
                  path('testes/delete/<id>', testes_delete, name="delete_testes"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
