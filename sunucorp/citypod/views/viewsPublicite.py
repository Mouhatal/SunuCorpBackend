from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,permissions,status
from citypod.models import *
from citypod.serializers import *
from rest_framework.response import Response

# Create your views here.


class PubliciteListView(generics.CreateAPIView):
    serializer_class= PubliciteSerializer
    # get all Categories
    def get(self, request, *args,**kwargs):
        publicite = Publicite.objects.all()

        if not publicite:
            return Response({
                "status": "failure",
                "message": "no such item",
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = PubliciteSerializer(Publicite, many = True)

        return Response({
            "status": "success",
            "message ": "item succussfully retrieved",
            # "count": category.count(),
            "data" : serializer.data
        }, status=status.HTTP_200_OK)

class PubliciteCreateView(generics.CreateAPIView):
    serializer_class= PubliciteSerializer
    def post(self, request, *args,**kwargs):
            #category = Category.objects.all()
        serializer = PubliciteSerializer(data=request.data)
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

class PubliciteEditView(generics.CreateAPIView):
    serializer_class= PubliciteSerializer
    def put(self, request, *args,**kwargs):
            #category = Category.objects.all()
        try:
            publicite = Publicite.objects.get(id = kwargs['pk'])
        except Publicite.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_400_BAD_REQUEST)

        serializer = PubliciteSerializer(publicite, data=request.data, partial=True)

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

class PubliciteDeleteView(generics.CreateAPIView):
    serializer_class= PubliciteSerializer
    def delete(self, request, *args,**kwargs):
            #category = Category.objects.all()
        try:
            publicite = Publicite.objects.get(id = kwargs['pk'])
        except Publicite.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_400_BAD_REQUEST)

        publicite.delete()

        return Response({
            "status": "success",
            "message ": "item succussfully deleted",
        }, status=status.HTTP_200_OK)

class PubliciteByNameView(generics.CreateAPIView):
    serializer_class= SubCategorySerializer
    # get all Categories
    def get(self, request, *args,**kwargs):
        try:
            publicite = Publicite.objects.get(pubName = kwargs['pubName'])
        except Publicite.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_404_NOT_FOUND)

        #serializer = CategorySerializer(category, data=request.data, partial=True)

        serializer = PubliciteSerializer(Publicite, data=request.data, partial=True)

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