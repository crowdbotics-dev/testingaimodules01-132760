from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Equipment, User
from django.contrib.auth import authenticate

@require_http_methods(['POST'])
def authenticate_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        return JsonResponse({'message': 'Authentication Successful'}, status=200)
    else:
        return JsonResponse({'message': 'Invalid credentials'}, status=401)

@require_http_methods(['GET'])
def fetch_equipment_data(request):
    equipment_list = list(Equipment.objects.values())
    return JsonResponse({'equipment': equipment_list}, status=200, safe=False)
