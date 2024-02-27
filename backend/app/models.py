from django.db import models


class User(models.Model):
    id       = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    role     = models.CharField(max_length=10)
    create_datetime = models.DateTimeField()

    class Meta:
        db_table = 'user'
