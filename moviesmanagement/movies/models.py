from django.db import models
# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length = 50, blank= True)
    pub_date = models.DateField()
    rating = models.FloatField(default=0)
    genres = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.title