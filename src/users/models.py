from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom manager for User.

    This manager provides methods to create and manage User instances.
    """

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Create and save and User with the given email and password.

        :param str email: The email address of the user.
        :param str password: The user's password.
        :param bool is_staff: Whether the user is staff or not.
        :param bool is_superuser: Whether the user is a superuser or not.
        :param dict extra_fields: Additional fields to include when creating the user.

        :returns: The created EmailUser instance.

        :raises ValueError: If the email is not provided.
        """
        now = timezone.now()
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        is_active = extra_fields.pop("is_active", True)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save User with the given email and password.

        :param str email: The email address of the user.
        :param str password: The user's password.
        :param dict extra_fields: Additional fields to include when creating the user.
        :returns: The created regular user instance.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save User with the given email and password, and mark them as a superuser.

        :param str email: The email address of the user.
        :param str password: The user's password.
        :param dict extra_fields: Additional fields to include when creating the user.
        :returns: The created admin user instance.
        :raises ValueError: If is_staff or is_superuser is not set to True.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model with extended functionality compared to Django's default User.

    This model does not use a username field. Instead, it relies on the email
    field for authentication.

    Use this model if you need to customize user behavior or add additional fields.

    Inherits from both AbstractBaseUser and PermissionMixin.

    Attributes:
        email (str): The email address of the user.
        is_staff (bool): Indicates if the user has staff privileges.
        is_active (bool): Indicates if the user account is active.
        date_joined (datetime): The date and time when the user account was created.
        objects (UserManager): The manager for the User model.
        USERNAME_FIELD (str): The field used for authentication (email).
        REQUIRED_FIELDS (list): The list of fields required when creating a user.

    Methods:
        get_short_name(): Returns a short identifier for the user.
    """

    email = models.EmailField(
        _("email address"), max_length=255, unique=True, db_index=True
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False)
    is_active = models.BooleanField(
        _("active"),
        default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_short_name(self):
        """Return the email."""
        return self.email


