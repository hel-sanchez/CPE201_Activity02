from django.db import models


# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', null=False, blank=False)

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'

    def __str__(self):
        return "Home"


class About(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', null=False, blank=False)
    description = models.TextField(verbose_name='Description', null=False, blank=False)
    image = models.ImageField(upload_to='about', verbose_name='Image', null=False, blank=False)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.TextField(verbose_name='Description', null=False, blank=False)
    image = models.ImageField(upload_to='works')

    def __str__(self):
        return self.title

