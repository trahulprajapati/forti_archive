from rest_framework import serializers
from .models import Service, DbServer, Schema, Tables, Policy
from django.contrib.auth import get_user_model

User = get_user_model()


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("name", "domain", "description", "status")


class DbServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbServer
        fields = (
            "name",
            "ip",
            "is_ssh_enabled",
            "service",
            "type",
            "hostname",
            "host_username",
            "status",
        )


class DbServerSerializerList(serializers.ModelSerializer):
    service_name = serializers.RelatedField(source="service", read_only=True)

    class Meta:
        model = DbServer
        fields = (
            "name",
            "ip",
            "is_ssh_enabled",
            "service_name",
            "type",
            "hostname",
            "host_username",
            "status",
        )


class SchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = ("schema_name", "db", "common_username", "common_password")


class SchemaSerializerList(serializers.ModelSerializer):
    db_name = serializers.RelatedField(source="db", read_only=True)

    class Meta:
        model = Schema
        fields = ("schema_name", "common_username", "common_password", "db_name")


class TableSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Tables
        fields = ("name", "schema", "table_size", "partition_count", "users")


class TableSerializerList(serializers.ModelSerializer):
    schema_name = serializers.RelatedField(source="schema", read_only=True)
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Tables
        fields = ("name", "table_size", "partition_count", "schema_name", "users")


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = (
            "name",
            "status",
            "source_table",
            "dest_db",
            "dest_schema",
            "type",
            "frequency",
            "starting_date",
            "ending_date",
            "archive_data_type",
            "archive_from_count",
            "archive_deletetion_type",
            "archive_deletetion_count",
        )


class PolicySerializerList(serializers.ModelSerializer):
    service_name = serializers.RelatedField(source="source_service", read_only=True)
    source_db_name = serializers.RelatedField(source="source_db", read_only=True)
    source_schema_name = serializers.RelatedField(
        source="source_schema", read_only=True
    )
    source_table_name = serializers.RelatedField(source="source_table", read_only=True)
    dest_db_name = serializers.RelatedField(source="dest_db", read_only=True)
    dest_schema_name = serializers.RelatedField(source="dest_schema", read_only=True)

    class Meta:
        model = Policy
        fields = (
            "name",
            "status",
            "source_table_name",
            "dest_db_name",
            "dest_schema_name",
            "type",
            "frequency",
            "starting_date",
            "ending_date",
            "archive_data_type",
            "archive_from_count",
            "archive_deletetion_type",
            "archive_deletetion_count",
        )
