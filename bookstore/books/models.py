from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    release_date = models.DateField('publish date')
    price = models.IntegerField()
    image = models.ImageField(upload_to="uploads/image/", null=True)

    def __str__(self):
        return self.name + " - " + self.author

    def __unicode__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('books:list-books', kwargs={})
