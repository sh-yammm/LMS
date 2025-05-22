from django.db import models

from course.models import BaseModelClass

from django.contrib.auth.models import User

# Create your models here.

class Instructors(BaseModelClass):

    profile = models.OneToOneField('authentication.profile', on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    image = models.ImageField(upload_to='instructor-images/')

    description = models.TextField()

    def __str__(self):

        return self.name
    
    class meta:

        verbose_name = 'Instructors'

        verbose_name_plural = 'Instructors' 