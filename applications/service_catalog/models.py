import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Service(models.Model):
    """
    For MicroService details
    """

    ACTIVE = 0
    INACTIVE = 1
    SUSPEND = 2

    STATUS = (
        (ACTIVE, "active"),
        (INACTIVE, "inactive"),
        (SUSPEND, "suspend"),
    )
    name = models.CharField(max_length=20, help_text="Service name")
    domain = models.CharField(max_length=20, help_text="Domain name")
    description = models.TextField(help_text="Description")
    status = models.PositiveSmallIntegerField(choices=STATUS, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(null=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.last_updated = datetime.datetime.now()
        super(Service, self).save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )


class DbServer(models.Model):
    """
    Db server of service , it holds db server conf details. With the help of this agents can find related db details
    and perform activity.
    """

    SOURCE = 0
    DESTINATION = 1
    TYPE = ((SOURCE, "Source"), (DESTINATION, "Destination"))
    ACTIVE = 0
    INACTIVE = 1
    SUSPEND = 2

    STATUS = (
        (ACTIVE, "active"),
        (INACTIVE, "inactive"),
        (SUSPEND, "suspend"),
    )
    name = models.CharField(max_length=20, help_text="Db name")
    ip = models.CharField(max_length=20, help_text="IP address")
    is_ssh_enabled = models.BooleanField(
        default=True, help_text="Is ssh enables on server"
    )
    service = models.ForeignKey(
        Service, related_name="db_service", on_delete=models.CASCADE
    )
    type = models.PositiveSmallIntegerField(
        choices=TYPE, default=SOURCE, help_text="Type of db source or destination"
    )
    hostname = models.CharField(max_length=20, help_text="Hostname")
    host_username = models.CharField(max_length=20, help_text="Username")
    status = models.PositiveSmallIntegerField(choices=STATUS, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(null=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.last_updated = datetime.datetime.now()
        super(DbServer, self).save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )


class Schema(models.Model):
    """
    Schema details of db
    """

    schema_name = models.CharField(max_length=20, help_text="Schema name")
    db = models.ForeignKey(DbServer, related_name="schema_db", on_delete=models.CASCADE)
    common_username = models.CharField(max_length=20, help_text="Username common")
    common_password = models.TextField(help_text="Password common")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(null=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.last_updated = datetime.datetime.now()
        super(Schema, self).save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )


class Tables(models.Model):
    """
    Tables details, this will be associated with role to access the table
    """

    name = models.CharField(max_length=20, help_text="Table name")
    schema = models.ForeignKey(
        Schema,
        related_name="table_schema",
        on_delete=models.CASCADE,
        help_text="Schema",
    )
    table_size = models.CharField(max_length=50, help_text="Table size")
    partition_count = models.IntegerField(help_text="Partition count")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(null=True)
    users = models.ManyToManyField(
        User,
        related_name="table_user",
        help_text="User can access particular table in order to see"
        " archival for that table and configure policy for that table",
    )

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.last_updated = datetime.datetime.now()
        super(Tables, self).save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )


class PolicyManager(models.Manager):
    pass


class Policy(models.Model):
    """
    Policy is the one where all conf can be done for archive and deletion for a table.
    This will be used by agents to run the activity based on the conf is configured for particular table.
    """

    ACTIVE = 0
    INACTIVE = 1
    SUSPEND = 2

    STATUS = (
        (ACTIVE, "active"),
        (INACTIVE, "inactive"),
        (SUSPEND, "suspend"),
    )
    DAILY = 0
    WEEKLY = 1
    MONTHLY = 2
    YEARLY = 3
    OTHER = 4

    TIME = (
        (DAILY, "Daily"),
        (WEEKLY, "Weekly"),
        (MONTHLY, "Monthly"),
        (YEARLY, "Yearly"),
        (OTHER, "Other"),
    )
    ONCE = 0
    RECCUR = 1
    TYPE = ((ONCE, "Once"), (RECCUR, "Reoccur"))
    objects = PolicyManager()
    name = models.CharField(max_length=20, help_text="Policy name")
    status = models.PositiveSmallIntegerField(choices=STATUS, default=ACTIVE)
    source_table = models.ForeignKey(
        Tables,
        related_name="policy_source_table",
        on_delete=models.CASCADE,
        help_text="Source table to archive",
    )
    dest_db = models.ForeignKey(
        DbServer,
        related_name="policy_dest_db",
        on_delete=models.CASCADE,
        help_text="Destination db",
    )
    dest_schema = models.ForeignKey(
        Schema,
        related_name="policy_dest_schema",
        on_delete=models.CASCADE,
        help_text="Destination schema",
    )
    type = models.PositiveSmallIntegerField(
        choices=TYPE, default=ONCE, help_text="Policy type. eg Once or reoccur"
    )
    frequency = models.PositiveSmallIntegerField(
        choices=TIME,
        default=MONTHLY,
        help_text="How policy should run, Weely, Monthly etc ",
    )
    starting_date = models.DateTimeField(
        help_text="Policy starting time. After this  policy will start running"
    )
    ending_date = models.DateTimeField(
        help_text="Policy ending time. After this  policy will not run"
    )
    archive_data_type = models.PositiveSmallIntegerField(
        choices=TIME,
        default=MONTHLY,
        help_text="Archived data duration"
        "We can define duration like Month, year etc"
        " For example archive_data_type is Month and archive_from_count = 3"
        "that means archive table data  3 month old",
    )
    archive_from_count = models.IntegerField(
        default=0,
        help_text="Archived data deletion time count, it depend on archive_data_type"
        "We can define time count in this field."
        " For example archive_data_type is Month and archive_from_count = 3"
        "that means archive table data 3 month old",
    )
    archive_deletetion_type = models.PositiveSmallIntegerField(
        choices=TIME,
        default=MONTHLY,
        help_text="Archived data deletion duration"
        "We can define duration like Month, year etc"
        " For example archive_deletetion_type is Month and archive_deletetion_count = 3"
        "that means delete archive 3 month old",
    )
    archive_deletetion_count = models.IntegerField(
        default=0,
        help_text="Archived data deletion time count, it depend on archive_deletetion_type"
        "We can define time count in this field."
        " For example archive_deletetion_type is Month and archive_deletetion_count = 3"
        "that means delete archive 3 month old",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(null=True)

    def get_executions(self):
        self.objects.exec_policy.all()

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.last_updated = datetime.datetime.now()
        super(Policy, self).save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )
