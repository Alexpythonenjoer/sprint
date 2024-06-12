from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TouristData
from .serializers import TouristDataSerializer

@api_view(['POST'])
def submitData(request):
    serializer = TouristDataSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        return Response(
            {"status": status.HTTP_200_OK, "message": None, "id": instance.id},
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"status": status.HTTP_400_BAD_REQUEST, "message": "Bad Request", "id": None},
            status=status.HTTP_400_BAD_REQUEST
        )
# Create your views here.
