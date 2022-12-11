from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer,PositionsSerializer
from .models import Contact,Positions
from rest_framework.decorators import api_view


@api_view(['GET'])
def getContact(request):
    contact = Contact.objects.all()
    serializer = ContactSerializer(contact, many=True)
    return Response(serializer.data)
  
@api_view(['POST'])
def postContact(request):
   
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def postJob(request):
    serializer = PositionsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)