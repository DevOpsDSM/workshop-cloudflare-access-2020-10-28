from django.http import JsonResponse
from django.contrib import admin
from django.urls import path

def secret(request):
    return JsonResponse({'secret': '1337'})

urlpatterns = [
    path("secret/", secret, name="secret"),
    path('admin/', admin.site.urls),
]
