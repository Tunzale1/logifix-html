from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
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


def contact_page(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('form_name')
        email = request.POST.get('form_email')
        subject = request.POST.get('form_subject')
        phone = request.POST.get('form_phone')
        message = request.POST.get('form_message')
        
        
        return JsonResponse({
            'status': 'true',
            'message': 'Thank you for your message. We will contact you soon!'
        })
    
    return render(request, 'page-contact.html')


 