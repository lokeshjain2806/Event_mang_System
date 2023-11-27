from django.db import models


# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email


class SlideModel(models.Model):
    image = models.ImageField(upload_to='slides/')

    def __str__(self):
        return f'Slide {self.id}'


class Review(models.Model):
    image = models.ImageField(upload_to='review/')
    name = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    message = models.TextField()


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
