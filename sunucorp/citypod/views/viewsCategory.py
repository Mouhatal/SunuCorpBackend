from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,permissions,status
from citypod.models import *
from citypod.serializers import *
from rest_framework.response import Response

# Create your views here.


class CategoryListView(generics.CreateAPIView):
    serializer_class= CategorySerializer
    # get all Categories
    def get(self, request, *args,**kwargs):
        category = Category.objects.all()

        if not category:
            return Response({
                "status": "failure",
                "message": "no such item",
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, many = True)

        return Response({
            "status": "success",
            "message ": "item succussfully retrieved",
            # "count": category.count(),
            "data" : serializer.data
        }, status=status.HTTP_200_OK)

class CategoryCreateView(generics.CreateAPIView):
    serializer_class= CategorySerializer
    def post(self, request, *args,**kwargs):
            #category = Category.objects.all()
        serializer = CategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "status": "failure",
                "message": serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response({
            "status": "success",
            "message ": "item succussfully created",
        }, status=status.HTTP_201_CREATED)

class CategoryEditView(generics.CreateAPIView):
    serializer_class= CategorySerializer
    def put(self, request, *args,**kwargs):
            #category = Category.objects.all()
        try:
            category = Category.objects.get(id = kwargs['pk'])
        except Category.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_400_BAD_REQUEST)

        serializer = CategorySerializer(category, data=request.data, partial=True)

        if not serializer.is_valid():
                return Response({
                "status": "failure",
                "message": serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response({
            "status": "success",
            "message ": "item succussfully edited",
        }, status=status.HTTP_200_OK)

class CategoryDeleteView(generics.CreateAPIView):
    serializer_class= CategorySerializer
    def delete(self, request, *args,**kwargs):
            #category = Category.objects.all()
        try:
            category = Category.objects.get(id = kwargs['pk'])
        except Category.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_400_BAD_REQUEST)

        category.delete()

        return Response({
            "status": "success",
            "message ": "item succussfully deleted",
        }, status=status.HTTP_200_OK)

class CategoryByNameView(generics.CreateAPIView):
    serializer_class= CategorySerializer
    # get all Categories
    def get(self, request, *args,**kwargs):
        try:
            category = Category.objects.get(categoryName = kwargs['categoryName'])
        except Category.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_404_NOT_FOUND)

        #serializer = CategorySerializer(category, data=request.data, partial=True)

        serializer = CategorySerializer(category, data=request.data, partial=True)

        if not serializer.is_valid():
                return Response({
                "status": "failure",
                "message": "No such item",
            }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "status": "success",
            "message ": "item succussfully retrieved",
            # "count": category.count(),
            "data" : serializer.data
        }, status=status.HTTP_200_OK)