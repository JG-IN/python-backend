from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from tweet.models import Tweet
from tweet.serializers import TweetSeriallizer
from rest_framework.decorators import api_view

@api_view(['GET'])
def user(request, user):
    try:
        tweet_serializer = TweetSeriallizer(Tweet.objects.filter(user=user), many=True).data
        return JsonResponse(tweet_serializer, safe=False)

    except Tweet.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
