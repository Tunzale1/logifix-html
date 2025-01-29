from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Service
from .serializers import ServiceSerializer

@api_view(["GET"])
def get_services(request):
    services = Service.objects.all()  # Fetch all services
    serializer = ServiceSerializer(services, many=True)  # Serialize data
    return Response(serializer.data)  # Return JSON response

# Create your views here.
def services_page(request):
    return render(request, "page-services.html")

def home(request):
    return render(request, "index.html")  # Change "index.html" if your main page is different

def about_page(request):
    return render(request, "page-about.html", {})
 