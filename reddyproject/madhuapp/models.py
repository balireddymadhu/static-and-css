from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    age = models.PositiveIntegerField()
    Remarks = models.TextField()
    about = models.TextField()

    def __str__(self):
        return self.name