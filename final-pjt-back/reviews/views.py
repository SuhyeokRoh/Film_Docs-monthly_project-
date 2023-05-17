from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ReviewSerializer


@api_view(['GET', 'POST'])
def review_create(request):
    if request.method == 'GET':
        # todos = Todo.objects.all()
        reviews = request.user.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(username=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if not request.user.review_set.filter(pk=review_pk).exists():
        return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        review.delete()
        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)