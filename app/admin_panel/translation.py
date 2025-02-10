from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Service, FooterLogo, FooterContactInfo, FooterAboutSection, FooterUsefulLinks, FooterServices, FooterNewsletter, FooterCopyright,
    HeaderTopInfo, HeaderSocialLinks, HeaderUsefulLinks, HeaderContactInfo, HeaderLogo, AboutPageHero, AboutSection, AboutCounter, WhyChooseUs, Feature, ContactPage,
    FAQ, FAQPage, Client, HomePageContent, SiteSettings, CustomersPageSettings
)

# Service Model Translation
class ServiceTranslationOptions(TranslationOptions):
    fields = (
        'services_page_title', 'title', 'text_1', 'text_2', 'overview_title', 'overview', 'center_title', 'service_center_text', 'contact_title', 'contact_text'
    )

# Footer Models Translation
class FooterLogoTranslationOptions(TranslationOptions):
    fields = ()  # No translatable fields

class FooterContactInfoTranslationOptions(TranslationOptions):
    fields = ('phone_title', 'email_title')

class FooterAboutSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class FooterUsefulLinksTranslationOptions(TranslationOptions):
    fields = ('title',)

class FooterServicesTranslationOptions(TranslationOptions):
    fields = ('title',)

class FooterNewsletterTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'placeholder_text')

class FooterCopyrightTranslationOptions(TranslationOptions):
    fields = ('text',)

# Header Models Translation
class HeaderTopInfoTranslationOptions(TranslationOptions):
    fields = ('address', 'working_hours', 'home_page', 'about_page', 'services_page', 'contact_page', 'customers_page')

class HeaderLogoTranslationOptions(TranslationOptions):
    fields = ('logo_alt_text',)

class HeaderSocialLinksTranslationOptions(TranslationOptions):
    fields = ()  # No translatable fields

class HeaderUsefulLinksTranslationOptions(TranslationOptions):
    fields = ()  # No translatable fields

class HeaderContactInfoTranslationOptions(TranslationOptions):
    fields = ()  # No translatable fields

# About Page Models Translation
class AboutPageHeroTranslationOptions(TranslationOptions):
    fields = ('title',)

class AboutSectionTranslationOptions(TranslationOptions):
    fields = ('subtitle', 'title', 'description', 'button_text')

class AboutCounterTranslationOptions(TranslationOptions):
    fields = ('counter_title_1', 'counter_title_2', 'counter_title_3')

class WhyChooseUsTranslationOptions(TranslationOptions):
    fields = ('subtitle', 'title', 'promo_title', 'button_text')

class FeatureTranslationOptions(TranslationOptions):
    fields = ('title',)

# Contact Page Model Translation
class ContactPageTranslationOptions(TranslationOptions):
    fields = (
        'hero_title', 'form_title', 'form_subtitle', 'contact_info_title', 'contact_info_subtitle', 'contact_info_description',
        'phone_title', 'email_title', 'address_title', 'address'
    )

# FAQ Models Translation
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')

class FAQPageTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

# Customers Page Models Translation
class CustomersPageSettingsTranslationOptions(TranslationOptions):
    fields = ('page_title',)

class ClientTranslationOptions(TranslationOptions):
    fields = ('name',)

# Home Page Model Translation
class HomePageContentTranslationOptions(TranslationOptions):
    fields = (
        'banner_badge_title', 'banner_badge_text', 'banner_main_title', 'banner_subtitle', 'banner_button_text',
        'about_subtitle', 'about_title', 'about_description', 'about_experience_description', 'about_checkmark_1', 'about_checkmark_2', 'about_checkmark_3',
        'cta_title', 'why_choose_subtitle', 'why_choose_title', 'why_choose_description', 'feature_block_one_title', 'feature_block_one_text',
        'feature_block_two_title', 'feature_block_two_text', 'offer_subtitle', 'offer_title', 'offer_description', 'list_item_1', 'list_item_2', 'list_item_3',
        'button_text', 'counter_title', 'caption_title'
    )

# Site Settings Model Translation
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'meta_keywords')

# Register all models for translation
translator.register(Service, ServiceTranslationOptions)
translator.register(FooterLogo, FooterLogoTranslationOptions)
translator.register(FooterContactInfo, FooterContactInfoTranslationOptions)
translator.register(FooterAboutSection, FooterAboutSectionTranslationOptions)
translator.register(FooterUsefulLinks, FooterUsefulLinksTranslationOptions)
translator.register(FooterServices, FooterServicesTranslationOptions)
translator.register(FooterNewsletter, FooterNewsletterTranslationOptions)
translator.register(FooterCopyright, FooterCopyrightTranslationOptions)
translator.register(HeaderTopInfo, HeaderTopInfoTranslationOptions)
translator.register(HeaderLogo, HeaderLogoTranslationOptions)
translator.register(HeaderSocialLinks, HeaderSocialLinksTranslationOptions)
translator.register(HeaderUsefulLinks, HeaderUsefulLinksTranslationOptions)
translator.register(HeaderContactInfo, HeaderContactInfoTranslationOptions)
translator.register(AboutPageHero, AboutPageHeroTranslationOptions)
translator.register(AboutSection, AboutSectionTranslationOptions)
translator.register(AboutCounter, AboutCounterTranslationOptions)
translator.register(WhyChooseUs, WhyChooseUsTranslationOptions)
translator.register(Feature, FeatureTranslationOptions)
translator.register(ContactPage, ContactPageTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
translator.register(FAQPage, FAQPageTranslationOptions)
translator.register(CustomersPageSettings, CustomersPageSettingsTranslationOptions)
translator.register(Client, ClientTranslationOptions)
translator.register(HomePageContent, HomePageContentTranslationOptions)
translator.register(SiteSettings, SiteSettingsTranslationOptions)