from rest_framework import serializers
from django.contrib.auth import get_user_model
from applications.service_catalog.serializers import TableSerializer
from applications.service_catalog.models import Tables

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    tables = TableSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "password", "tables")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


# User serializer
class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class EmptySerializer(serializers.Serializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    tables = TableSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "unique_id",
            "email",
            "password",
            "tables",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def get_or_create_tables(self, tables):
        table_ids = []
        for table in tables:
            table_instance, created = Tables.objects.get_or_create(
                pk=table.get("id"), defaults=table
            )
            table_ids.append(table_instance.pk)
        return table_ids

    def create_or_update_tables(self, tables):
        table_ids = []
        for table in tables:
            table_instance, created = Tables.objects.update_or_create(
                pk=table.get("id"), defaults=table
            )
            table_ids.append(table_instance.pk)
        return table_ids

    def create(self, validated_data):
        tables = validated_data.pop("tables", [])
        user = User.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            unique_id=validated_data["unique_id"],
        )
        user.set_password(validated_data["password"])
        user.table_user.set(self.get_or_create_tables(tables))
        return user

    def update(self, instance, validated_data):
        tables = validated_data.pop("tables", [])
        instance.table_user.set(self.create_or_update_tables(tables))
        instance.save()
        return instance
