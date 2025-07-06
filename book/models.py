from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator
class Book(models.Model):
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('adventure', 'Adventure'),
        ('animation', 'Animation'),
        ('biography', 'Biography'),
        ('comedy', 'Comedy'),
        ('crime', 'Crime'),
        ('documentary', 'Documentary'),
        ('drama', 'Drama'),
        ('family', 'Family'),
        ('fantasy', 'Fantasy'),
        ('history', 'History'),
        ('horror', 'Horror'),
        ('music', 'Music'),
        ('musical', 'Musical'),
        ('mystery', 'Mystery'),
        ('romance', 'Romance'),
        ('sci-fi', 'Science Fiction'),
        ('sport', 'Sport'),
        ('thriller', 'Thriller'),
        ('war', 'War'),
        ('western', 'Western'),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=209)
    description = models.TextField()
    genre = models.CharField(max_length=20,choices=GENRE_CHOICES)
    isbn  = models.CharField('ISBN',max_length=13,unique=True)
    publication_date = models.DateField()
    average_rating = models.DecimalField()
    
