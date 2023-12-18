from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True, blank=True)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Group(models.Model):
    NAMA = (
        ('I (Satu)', 'I (Satu)'),
        ('II (Dua)', 'II (Dua)'),
        ('III (Tiga)', 'III (Tiga)'),
        ('IV (Empat)', 'IV (Empat)'),
        ('V (Lima)', 'V (Lima)')
    )

    kelompok = models.CharField(max_length=50, choices=NAMA)

    def __str__(self):
        return self.kelompok
