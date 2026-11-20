
from django.contrib import admin
from .models import movie, Review

@admin.register(movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'genere')
    search_fields = ('title',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('Reviewer', 'movie', 'rating', 'created_at')
    list_filter = ('rating',)
