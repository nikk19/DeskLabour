from django.contrib.auth.models import BaseUserManager




class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phone_no, password, **extra_fields):
        """Create and save a User with the given Phoneno and password."""
        if not phone_no:
            raise ValueError('The given Phoneno must be set')
        # phone_no = self.normalize_phone_no(phone_no)
        user = self.model(phone_no=phone_no, **extra_fields)
        user.set_password(password)
        # user.save(using=self._db)
        return user

    def create_user(self, phone_no, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        # extra_fields.setdefault('is_active', False)
        return self._create_user(phone_no, password, **extra_fields)

    def create_superuser(self, phone_no, password, **extra_fields):
        """Create and save a SuperUser with the given Phoneno and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_no, password, **extra_fields)