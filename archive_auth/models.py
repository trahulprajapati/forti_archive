import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is Required!")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")

        return self.create_user(email, password, **extra_fields)


class ArchiveUser(AbstractUser):
    username = None
    email = models.EmailField(_("Email"), max_length=100, unique=True)
    unique_id = models.CharField(
        _("Username"), max_length=30, unique=True, default="test"
    )
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    # is_admin = models.BooleanField(_("Admin"),default=False)
    is_active = models.BooleanField(_("Active"), default=True)
    is_staff = models.BooleanField(_("Staff"), default=False)
    is_superuser = models.BooleanField(_("Superuser"), default=False)

    objects = UserManager()

    USERNAME_FIELD = "unique_id"

    def __str__(self):
        return self.unique_id

    @property
    def is_admin(self):
        return self.is_superuser or self.is_staff
