from django.db import models
from django.urls import reverse
# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    directed = models.CharField(max_length=150)
    cast = models.CharField(max_length=500)
    date = models.CharField(max_length=50)
    short_text = models.TextField()
    text = models.TextField()
    link = models.URLField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("film_detail", kwargs={"pk": self.pk})
    