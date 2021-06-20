from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=25)
    amount = models.IntegerField()

    def __str__(self):
        return self.name.upper()

    class Meta:
        verbose_name_plural = 'stocks'
