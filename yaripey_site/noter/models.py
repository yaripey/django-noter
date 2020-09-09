from django.db import models
from django.contrib.auth.models import User


class Notebook(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name



class Note(models.Model):
    notebook = models.ForeignKey(Notebook, on_delete = models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return 'Note from ' + self.notebook.name

