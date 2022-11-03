from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewsSerializers
from .models import Director, Movie, Review
from rest_framework import status


@api_view(['GET'])
def director_view(request):
    director = Director.objects.all()
    serializer = DirectorSerializer(director, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Director not found!'})
    serializer = DirectorSerializer(director)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Movie not found!'})
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_view(request):
    movies = Review.objects.all()
    serializer = ReviewSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found!'})
    serializer = MovieSerializer(review)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_review_views(request):
    movies = Movie.objects.all()
    serializer = MovieReviewsSerializers(movies, many=True)
    return Response(data=serializer.data)
