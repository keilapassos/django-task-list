from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    """
    usamos __str__ principalmente para deixar mais legível o output de uma instância 
    quando você imprime ou converte para string. Por exemplo:
    task = Task.objects.get(pk=1)
    print(task)  # Isso chamará o método __str__ da instância e imprimirá o título da tarefa.
    
    Em vez de ver algo como <Task: Task object (1)>, você verá o título real da tarefa, 
    o que é muito mais informativo e útil.
    """
