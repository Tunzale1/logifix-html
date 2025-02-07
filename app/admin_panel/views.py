from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import Service

def service_detail(request, service_slug):
    service = get_object_or_404(Service, slug=service_slug)
    services = Service.objects.all() 
    return render(request, 'page-service-details.html', {'service': service, 'services': services})

def services_page(request):
    services = Service.objects.all()
    print(services)
    return render(request, 'page-services.html', {'services': services})

def home(request):
    return render(request, "index.html")  # Change "index.html" if your main page is different

def about_page(request):
    return render(request, "page-about.html", {})

def customers_page(request):
    return render(request, "customers.html")

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


 