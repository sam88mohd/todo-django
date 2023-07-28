from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.TextField(null=False, max_length=1000)
    status = models.BooleanField(null=False, default=False)

    def __str__(self):
        return "Title: " + self.title + ", Status: " + str(self.status)
