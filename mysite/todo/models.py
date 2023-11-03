from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    done = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return f"{self.id} {self.name} {self.done}"
