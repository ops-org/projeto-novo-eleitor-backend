from django.db import models


class Estado(models.Model):
    state = models.CharField(max_length=60)
    abbreviation = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.state}"
