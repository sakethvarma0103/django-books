from typing import Iterable, Optional
from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,null=False, db_index=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        return super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.title} - {self.rating}"