from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from collections import OrderedDict


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1024)
    keywords = models.TextField(max_length=500)
    url = models.URLField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ip_address = models.GenericIPAddressField()
    history = HistoricalRecords()

    def clean(self):

        raw_keywords = self.keywords.split(',')
        processed_keywords = [k.strip() for k in raw_keywords if k.strip()]

        seen = set()
        unique_keywords = []
        for keyword in processed_keywords:
            lower_keyword = keyword.lower()
            if lower_keyword not in seen:
                seen.add(lower_keyword)
                unique_keywords.append(keyword) 
        
        self.keywords = ', '.join(unique_keywords)


        if self.title.lower() in [k.lower() for k in unique_keywords]:
            raise ValidationError({
                'keywords': "Słowa kluczowe nie mogą zawierać tytułu postu"
            })

        if slugify(self.title) == slugify(self.keywords):
            raise ValidationError({
                'keywords': "Słowa kluczowe nie mogą być identyczne z tytułem"
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title