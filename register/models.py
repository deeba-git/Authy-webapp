from django.db import models


class Register(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    username = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    class Meta:
        db_table = 'register'
