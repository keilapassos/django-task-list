## TASK LIST

Aqui descrevo a ordem mais ou menos de como fui criando esse projeto e alguns comandos ou trechos de código que utilizei ou julgo interessante pro meu conhecimento.

### Criar ambiente virtual e ativá-lo

```
python3 -m venv venv && source venv/bin/activate
```

### Instalar Django Rest Framework (DRF)

- django já é instalado junto com o DRF

```
pip install djangorestframework
```

### Criar arquivo com as dependências usadas neste projeto

```
pip freeze > requirements.txt
```

### Adicionar 'rest_framework' a installed_apps

- fica em settings.py do projeto

```
INSTALLED_APPS = [
...
'rest_framework',
]
```

### Criar um novo PROJETO Django

- O "ponto" faz com que crie apenas um diretório, sem diretórios aninhados

```
    django-admin startproject tasklist .
```

### Criar um novo APLICATIVO

```
python manage.py startapp tasks
```

### Adicionar o aplicativo ao installed_apps

```
INSTALLED_APPS = [
...
'rest_framework',
'tasks'
]
```

### Fazer a model que representa uma task

```

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

```

```
# sobre __str__
usamos __str__ principalmente para deixar mais legível o output de uma instância quando você imprime ou converte para string. Por exemplo:
task = Task.objects.get(pk=1)
print(task)  # Isso chamará o método __str__ da instância e imprimirá o título da tarefa.
Em vez de ver algo como
<Task: Task object (1)>,
você verá o título real da tarefa, o que é muito mais informativo e útil.
```

### Criar migrações e aplicar ao banco de dados

- fazer com que alterações sejam vistas pelo django

```
python manage.py makemigrations
```

- fazer com que as alterações sejam gravadas no banco de dados

```
python manage.py migrate
```

### Criar um serializer

- criar arquivo serializer no app

```
# sobre o serializer
- permite converter objetos complexos, como modelos de banco de dados, em formatos de dados que podem ser facilmente representados em JSON, XML ou outros formatos de resposta.
- permite desserializar os dados recebidos em solicitações HTTP (como POST ou PUT) em objetos Python que podem ser facilmente manipulados e salvos no banco de dados.
```

exemplo de serializer:

```
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    # O nome Meta é uma convenção usada pelo DRF para definir metadados relacionados
    # ao serializer, mas poderia ser qualquer outro nome exemplo: ConfiguracaoSerializer.
```

### Criar as views

```
# sobre as views
As Views são responsáveis por processar solicitações HTTP e retornar respostas, geralmente na forma de JSON ou XML
```

exemplo de uma view usando APIView:

```
# tasks/views.py
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
queryset = Task.objects.all()
serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
queryset = Task.objects.all()
serializer_class = TaskSerializer
```

### Colocar as rotas no arquivo urls.py

- crie esse arquivo se ele não existir. Exemplo de urls.py:

```
# tasks/urls.py

from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView

urlpatterns = [
path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]
```

### Adicionar as urls no arquivo de urls principal

- dentro do projeto

```
# tasklist/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
path('admin/', admin.site.urls),
path('api/', include('tasks.urls')), # as URLs do aplicativo são incluídas aqui
]
```

### Rodar o servidor

```
python manage.py runserver
```

### Acessar rotas

Agora, podemos usar as seguintes rotas para acessar as visualizações baseadas em APIView:

```
GET /api/tasks/: Lista todas as tarefas.
POST /api/tasks/: Cria uma nova tarefa.
GET /api/tasks/<id>/: Obtém detalhes de uma tarefa específica.
PUT /api/tasks/<id>/: Atualiza todos os campos de uma tarefa.
PATCH /api/tasks/<id>/: Atualiza parcialmente uma tarefa.
DELETE /api/tasks/<id>/: Exclui uma tarefa.
Essa é uma abordagem usando APIView para criar uma API CRUD básica para tarefas.
```

### exemplo de endereço de requisição GET da minha máquina:

```
# GET de todas as tasks
http://127.0.0.1:8000/api/tasks

# GET de uma task específica
http://127.0.0.1:8000/api/tasks/2
```
