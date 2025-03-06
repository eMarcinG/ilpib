from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'keywords', 'url', 'author', 'created_at', 'updated_at', 'ip_address']
        read_only_fields = ['author', 'created_at', 'updated_at', 'ip_address']

    def validate_keywords(self, value):
        keywords = value.split(',')
        if len(keywords) < 3:
            raise serializers.ValidationError("Musisz podać co najmniej 3 różne słowa kluczowe.")
        return value

