from django.db import models
from applications.account.models import CustomUser, Group


# Create your models here.
class Toast(models.Model):
    SHIFT = (
        ('PAGI', 'PAGI'),
        ('SIANG', 'SIANG'),
        ('MALAM', 'MALAM')
    )

    BOOL_CHOICE = (
        (True, 'Ya'),
        (False, 'Tidak')
    )

    user = models.ForeignKey(CustomUser, related_name='user', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='group', on_delete=models.CASCADE)
    shift = models.CharField(max_length=10, choices=SHIFT)
    datetime = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    siren_one = models.BooleanField(choices=BOOL_CHOICE, default=False)
    siren_two = models.BooleanField(choices=BOOL_CHOICE, default=False)
    siren_three = models.BooleanField(choices=BOOL_CHOICE, default=False)
    siren_four = models.BooleanField(choices=BOOL_CHOICE, default=False)
    seiscomp_one = models.BooleanField(choices=BOOL_CHOICE, default=False)
    seiscomp_two = models.BooleanField(choices=BOOL_CHOICE, default=False)
    seiscomp_three = models.BooleanField(choices=BOOL_CHOICE, default=False)
    toast_one = models.BooleanField(choices=BOOL_CHOICE, default=False)
    toast_two = models.BooleanField(choices=BOOL_CHOICE, default=False)
    disseminate_one = models.BooleanField(choices=BOOL_CHOICE, default=False)
    disseminate_two = models.BooleanField(choices=BOOL_CHOICE, default=False)
    tsp_one = models.BooleanField(choices=BOOL_CHOICE, default=False)
    tsp_two = models.BooleanField(choices=BOOL_CHOICE, default=False)
    wrs = models.BooleanField(choices=BOOL_CHOICE, default=False)
    temperature1 = models.CharField(max_length=10)
    temperature2 = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.datetime}_{self.shift}"
