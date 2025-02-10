# context_processors.py
from .models import (
    FooterLogo, FooterContactInfo, FooterAboutSection,
    FooterUsefulLinks, FooterServices, FooterNewsletter, FooterCopyright
)

from .models import (
    HeaderTopInfo, HeaderSocialLinks, HeaderUsefulLinks, HeaderContactInfo, HeaderLogo
)

from .models import (
    AboutPageHero, AboutSection, AboutCounter, 
    WhyChooseUs, Feature, Service
)

from .models import ContactPage

from .models import FAQPage, FAQ

from .models import Client

from .models import HomePageContent
from .models import SiteSettings


def footer_data(request):
    return {
        'footer_logo': FooterLogo.objects.first(),
        'footer_contact_info': FooterContactInfo.objects.first(),
        'footer_about': FooterAboutSection.objects.first(),
        'footer_useful_links': FooterUsefulLinks.objects.first(),
        'footer_services': FooterServices.objects.first(),
        'footer_newsletter': FooterNewsletter.objects.first(),
        'footer_copyright': FooterCopyright.objects.first(),
    }

def header_data(request):
    return {
        'header_logo': HeaderLogo.objects.first(),
        'header_top_info': HeaderTopInfo.objects.first(),
        'header_social_links': HeaderSocialLinks.objects.first(),
        'header_useful_links': HeaderUsefulLinks.objects.first(),
        'header_contact_info': HeaderContactInfo.objects.first(),
    }

def about_page(request):
    return {
        'about_hero': AboutPageHero.objects.first(),
        'about_section': AboutSection.objects.first(),
        'about_counter': AboutCounter.objects.first(),
        'why_choose_us': WhyChooseUs.objects.first(),
        'features': Feature.objects.all(),
        'services': Service.objects.all()[:4]  # Get first 4 services for the list
    }

def contact_page_data(request):
    return {
        'contact_page': ContactPage.objects.first(),
    }

def faq_data(request):
    return {
        'faq_page': FAQPage.objects.first(),
        'faqs': FAQ.objects.filter(is_active=True),
    }

def clients_data(request):
    return {
        'clients': Client.objects.filter(is_active=True),
    }


def home_page_data(request):
    return {
        'home_page_content': HomePageContent.objects.first(),
    }

def site_settings(request):
    site_settings = SiteSettings.objects.first()  # Get the first settings entry
    return {'site_settings': site_settings}

