from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import MyUser, TokenTest
from .serializers import MyUserSerializer, TokenTestSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def MyUserAPI(request, id=0):
    if request.method == 'GET':
        users = MyUser.objects.all()
        users_serializer = MyUserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        users_add_data = JSONParser().parse(request)
        users_serializer = MyUserSerializer(data = users_add_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added successfully!", safe=False)
        return JsonResponse("Failed to add!", safe=False)
    elif request.method == 'PUSH':
        users_update_data = JSONParser.parse(request)
        user_to_edit = MyUser.objects.filter(email=users_update_data["email"])
        users_serializer = MyUserSerializer(user_to_edit,data = users_update_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated successfully!", safe=False)
        return JsonResponse("Failed to update!", safe=False)
    elif request.method == 'DELETE':
        user_to_delete = MyUser.objects.get(email = id)
        user_to_delete.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def TestTokenAPI(request):
    if request.method == 'GET':
        tokentests = TokenTest.objects.all()
        #tokentest_serializer = TokenTestSerializer(tokentests, many = True)
        return JsonResponse("Success!", safe=False)


    
