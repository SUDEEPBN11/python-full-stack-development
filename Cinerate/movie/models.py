from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    genere = models.CharField(max_length=100)
    poster_image = models.ImageField(upload_to='posters/',blank=True,null=True)


    def __str__(self):
        return self.title

    def average_rating(self):
        reviews = self.rating.all()
        if reviews.count() == 0:
             return 0
        total = sum(review.rating for review in reviews)
        return round(total / reviews.count(), 1)

class Review(models.Model):
    Reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(movie, on_delete=models.CASCADE, related_name='rating')
    rating = models.IntegerField()  
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('Reviewer', 'movie')  # Ensure one review per user per movie
        ordering = ['-created_at']  # Order reviews by creation date, newest first

        def __str__(self):
            return f"{self.Reviewer.username} - {self.movie.title} ({self.rating})"
                
             

