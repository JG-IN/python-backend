from djongo import models

# Create your models here.
class Tweet(models.Model):
    # data = models.JSONField(default=dict)
    created_at = models.CharField(default='', max_length=100)
    user = models.CharField(default='', max_length=100)
    text = models.CharField(default='', max_length=100)
    hash_tags = models.CharField(default='', max_length=100)
    quote_count = models.CharField(default='', max_length=100)
    reply_count = models.CharField(default='', max_length=100)
    retweet_count = models.CharField(default='', max_length=100)
    favorite_count = models.CharField(default='', max_length=100)
    url = models.CharField(default='', max_length=100)
   
    class Meta:
        db_table = 'tweets'
   