from django.http import Http404,JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from .serializers import UserSerializer


# Create your views here.
@csrf_exempt
def register(request):
    if(request.method == 'GET'):
        data = User.objects.all()
        serializer = UserSerializer(data , many = True)
        return JsonResponse(serializer.data , safe = False)

    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        print(data)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
