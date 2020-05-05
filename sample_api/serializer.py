from rest_framework import serializers
from .models import Parent, Child1, Child2

class Child1Serializer(serializers.ModelSerializer):
    """
    子供側のserializer1
    """
    class Meta:
        model = Child1
        fields = [
            'id',
            'child1_column',
        ]

class Child2Serializer(serializers.ModelSerializer):
    """
    子供側のserializer2
    """
    class Meta:
        model = Child2
        fields = [
            'id',
            'child2_column',
        ]

class ParentSerializer(serializers.ModelSerializer):
    """
    親側のserializer
    """
    # 子供のserializerを親のfieldとして定義
    # このfield名とmodelのrelated_nameを合わせる
    child1s = Child1Serializer(many=True, read_only=True)
    child2s = Child2Serializer(many=True, read_only=True)

    class Meta:
        model = Parent
        fields = [
            'id',
            'parent_column',
            'child1s',
            'child2s',
        ]
