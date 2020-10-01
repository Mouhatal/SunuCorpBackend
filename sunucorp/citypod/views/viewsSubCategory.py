from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,permissions,status
from citypod.models import *
from citypod.serializers import *
from rest_framework.response import Response

# Create your views here.


class SubCategoryListView(generics.CreateAPIView):
    serializer_class= SubCategorySerializer
    # get all Categories
    def get(self, request, *args,**kwargs):
        subcategory = SubCategory.objects.all()

        if not subcategory:
            return Response({
                "status": "failure",
                "message": "no such item",
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = SubCategorySerializer(subcategory, many = True)

        return Response({
            "status": "success",
            "message ": "item succussfully retrieved",
            # "count": category.count(),
            "data" : serializer.data
        }, status=status.HTTP_200_OK)

class SubCategoryCreateView(generics.CreateAPIView):
    serializer_class= SubCategorySerializer
    def post(self, request, *args,**kwargs):
            #category = Category.objects.all()
        serializer = SubCategorySerializer(data=request.data)
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

class SubCategoryEditView(generics.CreateAPIView):
    serializer_class= SubCategorySerializer
    def put(self, request, *args,**kwargs):
            #category = Category.objects.all()
        try:
            subcategory = SubCategory.objects.get(id = kwargs['pk'])
        except SubCategory.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_400_BAD_REQUEST)

        serializer = SubCategorySerializer(subcategory, data=request.data, partial=True)

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

class SubCategoryDeleteView(generics.CreateAPIView):
    serializer_class= SubCategorySerializer
    def delete(self, request, *args,**kwargs):
            #category = Category.objects.all()
        try:
            subcategory = SubCategory.objects.get(id = kwargs['pk'])
        except SubCategory.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_400_BAD_REQUEST)

        subcategory.delete()

        return Response({
            "status": "success",
            "message ": "item succussfully deleted",
        }, status=status.HTTP_200_OK)

class SubCategoryByNameView(generics.CreateAPIView):
    serializer_class= SubCategorySerializer
    # get all Categories
    def get(self, request, *args,**kwargs):
        try:
            subcategory = SubCategory.objects.get(subcategoryName = kwargs['subcategoryName'])
        except SubCategory.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_404_NOT_FOUND)

        #serializer = CategorySerializer(category, data=request.data, partial=True)

        serializer = SubCategorySerializer(subcategory, data=request.data, partial=True)

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