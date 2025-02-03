from django.contrib import admin
from django.utils.text import capfirst
from django.utils.module_loading import import_string
from django.urls import reverse
from django.utils.html import format_html
from .models import (
    Service,
    FooterLogo, FooterContactInfo, FooterAboutSection, FooterUsefulLinks, FooterServices, FooterNewsletter, FooterCopyright,
    HeaderTopInfo, HeaderSocialLinks, HeaderUsefulLinks, HeaderContactInfo, HeaderLogo, AboutPageHero, AboutSection, AboutCounter, WhyChooseUs, Feature, ContactPage, 
)

from .models import FAQ, FAQPage

# Custom Admin Classes for Grouping
class FooterAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

class HeaderAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('question', 'answer')

# Footer Section
@admin.register(FooterLogo)
class FooterLogoAdmin(FooterAdmin):
    list_display = ('__str__', 'link')

@admin.register(FooterContactInfo)
class FooterContactInfoAdmin(FooterAdmin):
    list_display = ('phone_title', 'phone_number', 'email_title', 'email_address')

@admin.register(FooterAboutSection)
class FooterAboutSectionAdmin(FooterAdmin):
    list_display = ('title', 'description')

@admin.register(FooterUsefulLinks)
class FooterUsefulLinksAdmin(FooterAdmin):
    list_display = ('title',)

@admin.register(FooterServices)
class FooterServicesAdmin(FooterAdmin):
    list_display = ('title',)

@admin.register(FooterNewsletter)
class FooterNewsletterAdmin(FooterAdmin):
    list_display = ('title', 'description')

@admin.register(FooterCopyright)
class FooterCopyrightAdmin(FooterAdmin):
    list_display = ('text', 'link')


# Header Section
@admin.register(HeaderTopInfo)
class HeaderTopInfoAdmin(HeaderAdmin):
    list_display = ('address', 'working_hours', 'email')

@admin.register(HeaderLogo)
class HeaderLogoAdmin(HeaderAdmin):
    list_display = ('logo', 'logo_alt_text', 'logo_link')

@admin.register(HeaderSocialLinks)
class HeaderSocialLinksAdmin(HeaderAdmin):
    list_display = ('twitter_link', 'facebook_link', 'pinterest_link', 'instagram_link')

@admin.register(HeaderUsefulLinks)
class HeaderUsefulLinksAdmin(HeaderAdmin):
    list_display = ('privacy_policy_link', 'faq_link')

@admin.register(HeaderContactInfo)
class HeaderContactInfoAdmin(HeaderAdmin):
    list_display = ('phone_number', 'email', 'working_hours')

# Services Section
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

# about-page
@admin.register(AboutPageHero)
class AboutPageHeroAdmin(AboutAdmin):
    list_display = ('title', '__str__')

@admin.register(AboutSection)
class AboutSectionAdmin(AboutAdmin):
    list_display = ('title', 'subtitle', 'years_experience')

@admin.register(AboutCounter)
class AboutCounterAdmin(AboutAdmin):
    list_display = ('distribution_centers', 'years_experience', 'countries_regions')

@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(AboutAdmin):
    list_display = ('title', 'subtitle', 'starting_price')

@admin.register(Feature)
class FeatureAdmin(AboutAdmin):
    list_display = ('title', 'icon_class')  


#contact-page
@admin.register(ContactPage)
class ContactPageAdmin(ContactAdmin):
    list_display = ('hero_title', 'form_title', 'contact_info_title', 'phone_number', 'email_address')
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_background_image')
        }),
        ('Contact Form Section', {
            'fields': ('form_title', 'form_subtitle')
        }),
        ('Contact Info Section', {
            'fields': ('contact_info_title', 'contact_info_subtitle', 'contact_info_description')
        }),
        ('Contact Details', {
            'fields': ('phone_title', 'phone_number', 'email_title', 'email_address', 
                      'address_title', 'address')
        }),
        ('Map', {
            'fields': ('google_map_embed_url',)
        }),
    )
      
# faq-section
@admin.register(FAQPage)
class FAQPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


# Custom AdminSite to Group Models
class CustomAdminSite(admin.AdminSite):
    site_header = 'My Custom Admin'
    site_title = 'My Custom Admin Portal'
    index_title = 'Welcome to the Custom Admin Portal'

    def get_app_list(self, request):
        """
        Override get_app_list to group models into custom sections.
        """
        app_list = super().get_app_list(request)

        # Define custom groups
        custom_groups = [
            {
                'name': 'Footer',
                'models': [
                    FooterLogo, FooterContactInfo, FooterAboutSection, FooterUsefulLinks,
                    FooterServices, FooterNewsletter, FooterCopyright
                ]
            },
            {
                'name': 'Header',
                'models': [
                    HeaderTopInfo, HeaderLogo, HeaderSocialLinks, HeaderUsefulLinks, HeaderContactInfo
                ]
            },
            {
                'name': 'Services',
                'models': [
                    Service
                ]
            },
            {
                'name': 'About Page',
                'models': [
                    AboutPageHero, AboutSection, AboutCounter, WhyChooseUs, Feature
                ]
            },
            {
                'name': 'Contact Page',  # New group for Contact Page
                'models': [
                    ContactPage
                ]
            },
            {
                'name': 'FAQ',  # Add new FAQ group
                'models': [
                    FAQ, FAQPage
                ]
            }
        ]

        # Create a new app_list with custom groups
        new_app_list = []
        for group in custom_groups:
            group_dict = {
                'name': group['name'],
                'app_label': group['name'].lower(),
                'models': []
            }
            for model in group['models']:
                model_dict = {
                    'name': model._meta.verbose_name_plural,
                    'object_name': model._meta.object_name,
                    'admin_url': reverse(f'admin:{model._meta.app_label}_{model._meta.model_name}_changelist'),
                    'view_only': False
                }
                group_dict['models'].append(model_dict)
            new_app_list.append(group_dict)

        return new_app_list

# Replace the default admin site with the custom one
custom_admin_site = CustomAdminSite(name='custom_admin')

# Register all models with the custom admin site
custom_admin_site.register(Service, ServiceAdmin)
custom_admin_site.register(FooterLogo, FooterLogoAdmin)
custom_admin_site.register(FooterContactInfo, FooterContactInfoAdmin)
custom_admin_site.register(FooterAboutSection, FooterAboutSectionAdmin)
custom_admin_site.register(FooterUsefulLinks, FooterUsefulLinksAdmin)
custom_admin_site.register(FooterServices, FooterServicesAdmin)
custom_admin_site.register(FooterNewsletter, FooterNewsletterAdmin)
custom_admin_site.register(FooterCopyright, FooterCopyrightAdmin)
custom_admin_site.register(HeaderTopInfo, HeaderTopInfoAdmin)
custom_admin_site.register(HeaderLogo, HeaderLogoAdmin)
custom_admin_site.register(HeaderSocialLinks, HeaderSocialLinksAdmin)
custom_admin_site.register(HeaderUsefulLinks, HeaderUsefulLinksAdmin)
custom_admin_site.register(HeaderContactInfo, HeaderContactInfoAdmin)
custom_admin_site.register(AboutPageHero, AboutPageHeroAdmin)
custom_admin_site.register(AboutSection, AboutSectionAdmin)
custom_admin_site.register(AboutCounter, AboutCounterAdmin)
custom_admin_site.register(WhyChooseUs, WhyChooseUsAdmin)
custom_admin_site.register(Feature, FeatureAdmin)
custom_admin_site.register(ContactPage, ContactPageAdmin)
custom_admin_site.register(FAQ, FAQAdmin) 
custom_admin_site.register(FAQPage, FAQPageAdmin) 


# Replace the default admin site
admin.site = custom_admin_site