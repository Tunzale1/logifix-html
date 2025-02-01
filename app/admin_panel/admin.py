from django.contrib import admin
from .models import Service
from .models import FooterLogo, FooterContactInfo, FooterAboutSection, FooterUsefulLinks, FooterServices, FooterNewsletter, FooterCopyright
from .models import HeaderTopInfo, HeaderSocialLinks, HeaderUsefulLinks, HeaderContactInfo, HeaderLogo

# service-details
admin.site.register(Service)

# footer-section
@admin.register(FooterLogo)
class FooterLogoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'link')


@admin.register(FooterContactInfo)
class FooterContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone_title', 'phone_number', 'email_title', 'email_address')


@admin.register(FooterAboutSection)
class FooterAboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(FooterUsefulLinks)
class FooterUsefulLinksAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(FooterServices)
class FooterServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(FooterNewsletter)
class FooterNewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(FooterCopyright)
class FooterCopyrightAdmin(admin.ModelAdmin):
    list_display = ('text', 'link')


# header-section
from django.contrib import admin

@admin.register(HeaderTopInfo)
class HeaderTopInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'working_hours', 'email')

@admin.register(HeaderLogo)
class HeaderLogoAdmin(admin.ModelAdmin):
    list_display = ('logo', 'logo_alt_text', 'logo_link')

@admin.register(HeaderSocialLinks)
class HeaderSocialLinksAdmin(admin.ModelAdmin):
    list_display = ('twitter_link', 'facebook_link', 'pinterest_link', 'instagram_link')


@admin.register(HeaderUsefulLinks)
class HeaderUsefulLinksAdmin(admin.ModelAdmin):
    list_display = ('privacy_policy_link', 'faq_link')


@admin.register(HeaderContactInfo)
class HeaderContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'working_hours')