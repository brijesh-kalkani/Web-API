
from .models import Person

from rest_framework import serializers

class PersonSerializerrs(serializers.Serializer):
    class Meta:
        model = PersonView
        fields = "__all__"
