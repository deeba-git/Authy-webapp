from django.db import models


class SignIn(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=10)

    class Meta:  # mentioning the Meta class to show table name in db
        db_table = 'signin'
