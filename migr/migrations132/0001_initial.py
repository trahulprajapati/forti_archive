# Generated by Django 4.2.2 on 2023-10-07 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DbServer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(help_text="Db name", max_length=20)),
                ("ip", models.CharField(help_text="IP address", max_length=20)),
                (
                    "is_ssh_enabled",
                    models.BooleanField(
                        default=True, help_text="Is ssh enables on server"
                    ),
                ),
                (
                    "type",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "Source"), (1, "Destination")],
                        default=0,
                        help_text="Type of db source or destination",
                    ),
                ),
                ("hostname", models.CharField(help_text="Hostname", max_length=20)),
                (
                    "host_username",
                    models.CharField(help_text="Username", max_length=20),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "active"), (1, "inactive"), (2, "suspend")],
                        default=0,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Schema",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "schema_name",
                    models.CharField(help_text="Schema name", max_length=20),
                ),
                (
                    "common_username",
                    models.CharField(help_text="Username common", max_length=20),
                ),
                ("common_password", models.TextField(help_text="Password common")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(null=True)),
                (
                    "db",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schema_db",
                        to="service_catalog.dbserver",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(help_text="Service name", max_length=20)),
                ("domain", models.CharField(help_text="Domain name", max_length=20)),
                ("description", models.TextField(help_text="Description")),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "active"), (1, "inactive"), (2, "suspend")],
                        default=0,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tables",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(help_text="Table name", max_length=20)),
                ("table_size", models.CharField(help_text="Table size", max_length=50)),
                ("partition_count", models.IntegerField(help_text="Partition count")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(null=True)),
                (
                    "schema",
                    models.ForeignKey(
                        help_text="Schema",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="table_schema",
                        to="service_catalog.schema",
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        help_text="User can access particular table in order to see archival for that table and configure policy for that table",
                        related_name="table_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Policy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(help_text="Policy name", max_length=20)),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "active"), (1, "inactive"), (2, "suspend")],
                        default=0,
                    ),
                ),
                (
                    "type",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "Once"), (1, "Reoccur")],
                        default=0,
                        help_text="Policy type. eg Once or reoccur",
                    ),
                ),
                (
                    "frequency",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Daily"),
                            (1, "Weekly"),
                            (2, "Monthly"),
                            (3, "Yearly"),
                            (4, "Other"),
                        ],
                        default=2,
                        help_text="How policy should run, Weely, Monthly etc ",
                    ),
                ),
                (
                    "starting_date",
                    models.DateTimeField(
                        help_text="Policy starting time. After this  policy will start running"
                    ),
                ),
                (
                    "ending_date",
                    models.DateTimeField(
                        help_text="Policy ending time. After this  policy will not run"
                    ),
                ),
                (
                    "archive_data_type",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Daily"),
                            (1, "Weekly"),
                            (2, "Monthly"),
                            (3, "Yearly"),
                            (4, "Other"),
                        ],
                        default=2,
                        help_text="Archived data durationWe can define duration like Month, year etc For example archive_data_type is Month and archive_from_count = 3that means archive table data  3 month old",
                    ),
                ),
                (
                    "archive_from_count",
                    models.IntegerField(
                        default=0,
                        help_text="Archived data deletion time count, it depend on archive_data_typeWe can define time count in this field. For example archive_data_type is Month and archive_from_count = 3that means archive table data 3 month old",
                    ),
                ),
                (
                    "archive_deletetion_type",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Daily"),
                            (1, "Weekly"),
                            (2, "Monthly"),
                            (3, "Yearly"),
                            (4, "Other"),
                        ],
                        default=2,
                        help_text="Archived data deletion durationWe can define duration like Month, year etc For example archive_deletetion_type is Month and archive_deletetion_count = 3that means delete archive 3 month old",
                    ),
                ),
                (
                    "archive_deletetion_count",
                    models.IntegerField(
                        default=0,
                        help_text="Archived data deletion time count, it depend on archive_deletetion_typeWe can define time count in this field. For example archive_deletetion_type is Month and archive_deletetion_count = 3that means delete archive 3 month old",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(null=True)),
                (
                    "dest_db",
                    models.ForeignKey(
                        help_text="Destination db",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="policy_dest_db",
                        to="service_catalog.dbserver",
                    ),
                ),
                (
                    "dest_schema",
                    models.ForeignKey(
                        help_text="Destination schema",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="policy_dest_schema",
                        to="service_catalog.schema",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        help_text="Source service",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="policy_source_service",
                        to="service_catalog.service",
                    ),
                ),
                (
                    "source_db",
                    models.ForeignKey(
                        help_text="Source Databsse",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="policy_source_db",
                        to="service_catalog.dbserver",
                    ),
                ),
                (
                    "source_schema",
                    models.ForeignKey(
                        help_text="Source Schema",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="policy_source_schema",
                        to="service_catalog.schema",
                    ),
                ),
                (
                    "source_table",
                    models.ForeignKey(
                        help_text="Source table to archive",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="policy_source_table",
                        to="service_catalog.tables",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="dbserver",
            name="service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="db_service",
                to="service_catalog.service",
            ),
        ),
    ]
