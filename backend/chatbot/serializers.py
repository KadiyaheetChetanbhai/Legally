from rest_framework import serializers

class LegalQuerySerializer(serializers.Serializer):
    query = serializers.CharField(max_length=1000)
