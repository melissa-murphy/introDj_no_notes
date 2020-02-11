from django.db import models

# Create your models here.
class Note(models.Models):
    title = models.CharField(_(""), max_length=200)