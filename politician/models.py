from django.db import models


class Party(models.Model):
    name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.name}'


class Politician(models.Model):
    SEX_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female')
    )

    id_site = models.PositiveIntegerField()
    party = models.ForeignKey(Party, related_name='politicians', on_delete=models.SET_NULL, null=True, blank=False)

    name = models.CharField(max_length=128)
    name_full = models.CharField(max_length=254)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.name} {self.party}'


class Stats(models.Model):
    politician = models.ForeignKey(Politician, related_name='stats', on_delete=models.SET_NULL, null=True, blank=False)
    fetch_time = models.DateTimeField()

    cehap_sum = models.PositiveIntegerField(default=0)
    secretary_sum = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.politician}'