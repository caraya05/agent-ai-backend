from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CompanyManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not username:
            raise ValueError(_('The given username must be set'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        # """Create and save a regular User with the given phone and password."""
        # extra_fields.setdefault('is_staff', False)
        # extra_fields.setdefault('is_superuser', False)
        # return self._create_user(phone, password, **extra_fields)
        if not username:
            raise ValueError(_('The given username must be set'))
        user = self.model(username=username, **extra_fields)
        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        #
        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')
        #
        # return self._create_user(phone, password, **extra_fields)

        if not username:
            raise ValueError(_('The given username must be set'))
        user = self.model(username=username, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def load_by_id(self, id: str):  # pylint: disable=redefined-builtin
        return super().filter(id=id).first()
