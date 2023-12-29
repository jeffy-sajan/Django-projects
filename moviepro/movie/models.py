from django.db import models

class Movie(models.Model):
    cover=models.ImageField(upload_to='movie/cover',null=True,blank=True)
    title = models.CharField(max_length=20)
    year = models.IntegerField()
    description = models.CharField(max_length=40)

    def __str__(self):
        return self.title


