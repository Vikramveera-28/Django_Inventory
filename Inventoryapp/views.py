from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Inventory
from .serializers import ItemSerializer

from rest_framework.views import APIView
from django.http import JsonResponse


# Create your views here.

def home(request):
    return render(request, "Index.html")


# @api_view()  #default accept GET method
# def GetItems(request):
#     items = Inventory.objects.all()
#     serializer = ItemSerializer(items, many=True)
#     #return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET', 'DELETE'])
# def Item(request, pk):
#     if request.method == 'GET':
#         item = Inventory.objects.get(pk=pk)
#         serializer = ItemSerializer(item)
#         #return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == 'DELETE':
#         snippet = Inventory.objects.get(pk=pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class GetItems(APIView):
    def get(self, request):
        items = Inventory.objects.all().order_by('-id')
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Items(APIView):
    def get(self, request, pk):
        items = Inventory.objects.get(pk=pk)
        serializer = ItemSerializer(items)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        snippet = Inventory.objects.get(pk=pk)
        serializer = ItemSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = Inventory.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)