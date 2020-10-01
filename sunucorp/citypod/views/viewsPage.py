from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,permissions,status
from citypod.models import *
from citypod.serializers import *
from rest_framework.response import Response

# Create your views here.


class PageListView(generics.CreateAPIView):
    serializer_class= PageSerializer
    # get all Categories
    def get(self, request, *args,**kwargs):
        page = Page.objects.all()

        if not page:
            return Response({
                "status": "failure",
                "message": "no such item",
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = PageSerializer(page, many = True)

        return Response({
            "status": "success",
            "message ": "item succussfully retrieved",
            # "count": category.count(),
            "data" : serializer.data
        }, status=status.HTTP_200_OK)

class PageCreateView(generics.CreateAPIView):
    serializer_class= PageSerializer
    def post(self, request, *args,**kwargs):
            #category = Category.objects.all()
        serializer = PageSerializer(data=request.data)
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

class PageEditView(generics.CreateAPIView):
    serializer_class= PageSerializer
    def put(self, request, *args,**kwargs):
            #category = Category.objects.all()
        try:
            page = Page.objects.get(id = kwargs['pk'])
        except Page.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_400_BAD_REQUEST)

        serializer = PageSerializer(page, data=request.data, partial=True)

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

class PageDeleteView(generics.CreateAPIView):
    serializer_class= PageSerializer
    def delete(self, request, *args,**kwargs):
            #category = Category.objects.all()
        try:
            page = Page.objects.get(id = kwargs['pk'])
        except Page.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_400_BAD_REQUEST)

        page.delete()

        return Response({
            "status": "success",
            "message ": "item succussfully deleted",
        }, status=status.HTTP_200_OK)

class PageByNameView(generics.CreateAPIView):
    serializer_class= PageSerializer
    # get all Categories
    def get(self, request, *args,**kwargs):
        try:
            page = Page.objects.get(pageName = kwargs['pageName'])
        except Page.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_404_NOT_FOUND)

        #serializer = CategorySerializer(category, data=request.data, partial=True)

        serializer = PageSerializer(page, data=request.data, partial=True)

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