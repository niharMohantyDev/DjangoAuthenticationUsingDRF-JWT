from django.contrib.auth import authenticate, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
import json
from .models import *

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({'message': 'Both username and password are required.'}, status=400)


        user = User.objects.create_user(username=username, password=password)
        user.save()

        return JsonResponse({'message': 'User created successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = (json.loads(request.body))['username']
        password = (json.loads(request.body))['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)

            return JsonResponse({'access_token': str(refresh.access_token),
                                 'refresh_token': str(refresh)})
        else:
            return JsonResponse({'message': 'Invalid username or password.'}, status=401)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)


def logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'User logged out successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)
