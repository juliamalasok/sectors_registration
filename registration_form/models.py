from django.db import models
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class User(TimeStampedModel):

    name = models.CharField(max_length = 255)

    def __str__(self):
        return "ID=" + str(self.id) + ", name=" + self.name

'''
class Sector(models.Model):
    code = models.IntegerField()
'''


class SectorAnswer(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    MANUFACTURING = 1
    CONSTRUCTION_MATERIALS = 19

    SECTOR_CHOICES = ((MANUFACTURING, "Manufacturing"),
                      (CONSTRUCTION_MATERIALS, "Construction materials"))

    sector_choice = models.IntegerField(choices=SECTOR_CHOICES)

    def __str__(self):
        return self.user.name + " " + str(self.sector_choice)
