from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


"""
O nome Meta é uma convenção usada pelo DRF para definir metadados relacionados 
ao serializer, mas poderia ser qualquer outro nome exemplo: ConfiguracaoSerializer.
"""
