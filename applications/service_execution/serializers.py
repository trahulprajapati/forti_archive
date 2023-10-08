from rest_framework import serializers
from .models import Execution


class ExecutionSerializer(serializers.ModelSerializer):
    table_name = serializers.RelatedField(source="table", read_only=True)
    policy_name = serializers.RelatedField(source="policy", read_only=True)

    class Meta:
        model = Execution
        fields = (
            (
                "exec_id",
                "table_name",
                "status",
                "policy_name",
                "start_at",
                "finished_at",
                "note",
            ),
        )
        extra_kwargs = {
            "password": {"read_only": True},
        }
