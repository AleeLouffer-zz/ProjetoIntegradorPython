from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, cnpj, nome_fantasia, razao_social, is_staff, is_superuser,  **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError("Usuario sem username")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, cnpj=cnpj, nome_fantasia=nome_fantasia, razao_social=razao_social, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, cnpj=None, nome_fantasia=None, razao_social=None, **extra_fields):
        return self._create_user(username, email, password, cnpj, nome_fantasia, razao_social, False, False, **extra_fields)

class Empresa(AbstractUser):      
    id = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=100, null=True)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cnpj', 'nome_fantasia']

    objects = UserManager()

