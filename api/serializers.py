from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=128)
    email = serializers.CharField(required=False, allow_blank=True, max_length=128)
    phone = serializers.CharField(required=False, allow_blank=True, max_length=128)
    street = serializers.CharField(required=False, allow_blank=True, max_length=128)

    def create(self, validated_data):
        c = Company()
        c.name = validated_data.get("name")
        c.email = validated_data.get("email")
        c.phone = validated_data.get("phone")
        c.street = validated_data.get("street")
        c.save()
        return c

    def update(self, c, validated_data):
        c.id = validated_data.get("id", c.id)
        c.name = validated_data.get("name", c.name)
        c.email = validated_data.get("email", c.email)
        c.save()
        return c
