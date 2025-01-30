from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    slug = models.SlugField(unique=True, blank=True)  # New slug field
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
