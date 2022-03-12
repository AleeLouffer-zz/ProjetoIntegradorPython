from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, cnpj_cpf, nome, is_staff, is_superuser,  **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError("Usuario sem username")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, cnpj_cpf=cnpj_cpf, nome=nome, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, cnpj_cpf=None, nome=None,  **extra_fields):
        return self._create_user(username, email, password, cnpj_cpf, nome, False, False, **extra_fields)

class Empresa(AbstractUser):      
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cnpj_cpf = models.CharField(unique=True, max_length=18)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cnpj', 'nome_fantasia']

    objects = UserManager()

