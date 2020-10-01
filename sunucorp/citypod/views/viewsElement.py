from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,permissions,status
from citypod.models import *
from citypod.serializers import *
from rest_framework.response import Response

# Create your views here.


class ElementListView(generics.CreateAPIView):
    serializer_class= ElementSerializer
    # get all Categories
    def get(self, request, *args,**kwargs):
        element = Element.objects.all()

        if not element:
            return Response({
                "status": "failure",
                "message": "no such item",
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = ElementSerializer(element, many = True)

        return Response({
            "status": "success",
            "message ": "item succussfully retrieved",
            # "count": category.count(),
            "data" : serializer.data
        }, status=status.HTTP_200_OK)

class ElementCreateView(generics.CreateAPIView):
    serializer_class= ElementSerializer
    def post(self, request, *args,**kwargs):
            #category = Category.objects.all()
        serializer = ElementSerializer(data=request.data)
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

class ElementEditView(generics.CreateAPIView):
    serializer_class= ElementSerializer
    def put(self, request, *args,**kwargs):
            #category = Category.objects.all()
        try:
            element = Element.objects.get(id = kwargs['pk'])
        except Element.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_400_BAD_REQUEST)

        serializer = ElementSerializer(element, data=request.data, partial=True)

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

class ElementDeleteView(generics.CreateAPIView):
    serializer_class= ElementSerializer
    def delete(self, request, *args,**kwargs):
            #category = Category.objects.all()
        try:
            element = Element.objects.get(id = kwargs['pk'])
        except Element.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_400_BAD_REQUEST)

        element.delete()

        return Response({
            "status": "success",
            "message ": "item succussfully deleted",
        }, status=status.HTTP_200_OK)

class ElementByNameView(generics.CreateAPIView):
    serializer_class= ElementSerializer
    # get all Categories
    def get(self, request, *args,**kwargs):
        try:
            element = Element.objects.get(elementName = kwargs['elementName'])
        except Element.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item",
            }, status= status.HTTP_404_NOT_FOUND)

        #serializer = CategorySerializer(category, data=request.data, partial=True)

        serializer = ElementSerializer(element, data=request.data, partial=True)

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