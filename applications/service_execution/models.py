import uuid
import datetime
from django.db import models


class Execution(models.Model):
    """
    To record every execution for archival or deletion of archival.
    When agents start the archive or delete proces then record will be created to track the event.
    Unique id is generated for every table archive or delete associate with and with help of this status of event
    can be updated by destination or source agents.
    """

    ARCHIVE = 0
    PURGE = 1

    TYPE = ((ARCHIVE, "Archive"), (PURGE, "Purge"))

    CREATED = 0
    SOURCE_SUCCESS = 1
    SOURCE_FAILED = 2
    DEST_FAILED = 3
    COMPLETED = 4

    STATUS = (
        (CREATED, "Created"),
        (SOURCE_SUCCESS, "Source Success"),
        (SOURCE_FAILED, "Source Failed"),
        (DEST_FAILED, "Dest Failed"),
        (COMPLETED, "Completed"),
    )
    exec_id = models.UUIDField(
        default=uuid.uuid4, unique=True, help_text="Execution unique ID"
    )
    table = models.ForeignKey(
        "service_catalog.Tables", related_name="exec_tables", on_delete=models.CASCADE
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS, default=CREATED, help_text="Status"
    )
    policy = models.ForeignKey(
        "service_catalog.Policy", related_name="exec_policy", on_delete=models.CASCADE
    )
    start_at = models.DateTimeField(auto_now_add=True, help_text="Start of activity")
    last_updated = models.DateTimeField(null=True)
    finished_at = models.DateTimeField(help_text="End of activity")
    note = models.CharField(max_length=50, null=True)

    @property
    def table(self):
        return self.policy.source_table

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.last_updated = datetime.datetime.now()
        if self.status == self.COMPLETED:
            self.finished_at = datetime.datetime.now()
        super(Execution, self).save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )
