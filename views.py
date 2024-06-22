from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TouristData
from .serializers import TouristDataSerializer
from django.http import Http404

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
@api_view(['GET'])
def getData(request, id):
    try:
        data = TouristData.objects.get(id=id)
    except TouristData.DoesNotExist:
        raise Http404("Data does not exist")
    serializer = TouristDataSerializer(data)
    return Response(serializer.data)

@api_view(['PATCH'])
def updateData(request, id):
    try:
        data = TouristData.objects.get(id=id)
    except TouristData.DoesNotExist:
        raise Http404("Data does not exist")
    if data.status != 'new':
        return Response({"state": 0, "message": "Can only edit data with status 'new'."})
    for field in ['full_name', 'email', 'phone_number']:
        request.data.pop(field, None)
    serializer = TouristDataSerializer(data, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"state": 1, "message": "Data updated successfully."})
    return Response({"state": 0, "message": "Failed to update data."})

@api_view(['GET'])
def getUserData(request):
    email = request.query_params.get('user__email', None)
    if email is None:
        return Response({"message": "Email parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
    data = TouristData.objects.filter(user__email=email)
    serializer = TouristDataSerializer(data, many=True)
    return Response(serializer.data)