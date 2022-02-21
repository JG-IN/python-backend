from rest_framework import serializers
from tweet.models import Tweet

class TweetSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('created_at',
                  'user',
                  'text',
                  'hash_tags',
                  'quote_count',
                  'reply_count',
                  'retweet_count',
                  'favorite_count',
                  'url')