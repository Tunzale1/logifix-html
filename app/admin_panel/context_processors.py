# context_processors.py
from .models import (
    FooterLogo, FooterContactInfo, FooterAboutSection,
    FooterUsefulLinks, FooterServices, FooterNewsletter, FooterCopyright
)

from .models import (
    HeaderTopInfo, HeaderSocialLinks, HeaderUsefulLinks, HeaderContactInfo, HeaderLogo
)


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