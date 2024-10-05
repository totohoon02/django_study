from rest_framework import serializers

from mytodo.models import Todo


class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'complete', 'important')


class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'important')