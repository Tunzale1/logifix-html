from django.db import models
from django.utils.text import slugify
from adminsortable2.admin import SortableAdminMixin
from django.utils.translation import gettext_lazy as _

# service-details
class Service(models.Model):
    services_page_title =  models.CharField(max_length=200, default="Services")  
    services_background_image =  models.ImageField(upload_to='services/', default='images/background/page-title.jpg' , help_text="1600 x 364 px")
    slug = models.SlugField(unique=True, blank=True)
    icon_class = models.CharField(max_length=50, default="flaticon-team")
    title = models.CharField(max_length=200, default="Safety and Reliability")
    text_1 = models.CharField(max_length=200, default="Worldwide service")
    text_2 = models.CharField(max_length=200, default="24/7 Support")
    image = models.ImageField(upload_to='services/' , help_text="370 × 492 px")
    
    service_details_background_image = models.ImageField(upload_to='services/details', default='images/background/page-title.jpg', help_text="1600 x 364 px")
    overview_title = models.CharField(max_length=200, default="Service Overview")
    overview = models.TextField(default="Lorem ipsum is simply free text used by copytyping refreshing...")
    center_title = models.CharField(max_length=200, default="Service Center")
    service_center_text = models.TextField(default="Lorem ipsum is simply free text used by copytyping refreshing...")
    service_image_1 = models.ImageField(upload_to='services/details/', blank=True, null=True, help_text="376 × 209 px")
    service_image_2 = models.ImageField(upload_to='services/details/', blank=True, null=True, help_text="376 × 209 px")
    contact_title = models.CharField(max_length=200, default="Contact with us for any advice")
    contact_phone = models.CharField(max_length=20, default="+892 ( 123 ) 112 - 9999")
    contact_text = models.CharField(max_length=200, default="Need help? Talk to an expert")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# footer-section
class FooterLogo(models.Model):
    logo = models.ImageField(upload_to='footer/logo/', help_text="193 × 47 px")

    def __str__(self):
        return "Footer Logo"


class FooterContactInfo(models.Model):
    background_image = models.ImageField(upload_to='footer/logo/', default='images/icons/footer-bg.png', help_text="1600 x 688 px")
    phone_title = models.CharField(max_length=100, default="Call Us On")
    phone_number = models.CharField(max_length=20)

    email_title = models.CharField(max_length=100, default="Mail to Us")
    email_address = models.EmailField()

    def __str__(self):
        return "Footer Contact Info"


class FooterAboutSection(models.Model):
    title = models.CharField(max_length=100, default="About Us")
    description = models.TextField()
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Footer About Section"


class FooterUsefulLinks(models.Model):
    title = models.CharField(max_length=100, default="Useful Links")
    links = models.JSONField(default=list)  # Example: [{"name": "About Us", "url": "/about/"}, ...]

    def __str__(self):
        return "Footer Useful Links"


class FooterServices(models.Model):
    title = models.CharField(max_length=100, default="Services")
    links = models.JSONField(default=list, blank=True, null=True)  # Example: [{"name": "Air Freight", "url": "/services/air-freight/"}, ...]

    def __str__(self):
        return "Footer Services"


class FooterNewsletter(models.Model):
    title = models.CharField(max_length=100, default="Newsletter")
    description = models.TextField()
    placeholder_text = models.CharField(max_length=100, default="Your Email")

    def __str__(self):
        return "Footer Newsletter"


class FooterCopyright(models.Model):
    text = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Footer Copyright"
    

#header-section
class HeaderTopInfo(models.Model):
    address = models.CharField(max_length=200, default="1901 Horidge Cir. Shiloh, Hawaii 81063")
    working_hours = models.CharField(max_length=100, default="Mon - Fri: 09.00am - 10.00 pm")
    email = models.EmailField(default="info@example.com")
    home_page = models.CharField(max_length=100, default="Home")
    about_page = models.CharField(max_length=100, default="About")
    services_page = models.CharField(max_length=100, default="Services")
    contact_page = models.CharField(max_length=100, default="Contact")
    customers_page =  models.CharField(max_length=100, default="Customers")

    def __str__(self):
        return "Header Top Info"

class HeaderLogo(models.Model):
    logo = models.ImageField(upload_to='header/logo/', help_text="193 x 47 px")
    logo_alt_text = models.CharField(max_length=100, default="Logifix")

    def __str__(self):
        return "Header Logo"

class HeaderSocialLinks(models.Model):
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    pinterest_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Header Social Links"


class HeaderUsefulLinks(models.Model):
    privacy_policy_link = models.URLField(blank=True, null=True)
    faq_link = models.URLField(blank=True, null=True)


    def __str__(self):
        return "Header Useful Links"


class HeaderContactInfo(models.Model):
    phone_number = models.CharField(max_length=20, default="+36 55 540 069")

    def __str__(self):
        return "Header Contact Info"
    

#about-page
from django.db import models

class AboutPageHero(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    background_image = models.ImageField(upload_to='about/hero/', help_text="1600 x 364 px")

    def __str__(self):
        return "About Page Hero Section"

class AboutSection(models.Model):
    subtitle = models.CharField(max_length=100, default="WHO WE ARE")
    title = models.CharField(max_length=200)
    description = models.TextField()
    years_experience = models.IntegerField(default=25)
    button_text = models.CharField(max_length=200, default="Explore more")
    
    image_1 = models.ImageField(upload_to='about/', help_text="515 x 589 px")
    image_2 = models.ImageField(upload_to='about/', help_text="320 x 273 px")
    logo_image = models.ImageField(upload_to='about/', help_text="72 x 64 px")

    def __str__(self):
        return "About Main Section"

class AboutCounter(models.Model):
    distribution_centers = models.IntegerField(default=541)
    counter_title_1 = models.CharField(max_length=100, default="Distribution Center")
    years_experience = models.IntegerField(default=35)
    counter_title_2 = models.CharField(max_length=100, default="Years Of Experience")
    countries_regions = models.IntegerField(default=147)
    counter_title_3 = models.CharField(max_length=100, default="Countries and Regions")


    def __str__(self):
        return "About Counter Section"

class WhyChooseUs(models.Model):
    subtitle = models.CharField(max_length=100, default="bura ile bagli olan her bir seyi bos buraxin zehmet olmasa (bu section sehifede yoxdur)")
    title = models.CharField(max_length=200)
    background_image = models.ImageField(upload_to='about/background/')
    promo_image = models.ImageField(upload_to='about/promo/')
    promo_title = models.CharField(max_length=200)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    price_unit = models.CharField(max_length=20, default="kg")
    button_text = models.CharField(max_length=200, default="Get Started Now")

    def __str__(self):
        return "Why Choose Us Section"

class Feature(models.Model):
    icon_class = models.CharField(max_length=50)
    title = models.CharField(max_length=200, default="bura ile bagli olan her bir seyi bos buraxin zehmet olmasa (bu section sehifede yoxdur)")
    link = models.URLField()

    def __str__(self):
        return self.title



#contact-page
class ContactPage(models.Model):
    # Hero Section
    hero_title = models.CharField(max_length=200, default="Contact Us")
    hero_background_image = models.ImageField(upload_to='contact/hero/', help_text="1600 x 364 px")

    # Contact Form Section
    form_title = models.CharField(max_length=200, default="Feel free to write")
    form_subtitle = models.CharField(max_length=200, default="Send us email")

    # Contact Info Section
    contact_info_title = models.CharField(max_length=200, default="Get in touch with us")
    contact_info_subtitle = models.CharField(max_length=200, default="Need any help?")
    contact_info_description = models.TextField(default="Lorem ipsum is simply free text available dolor sit amet consectetur notted adipisicing elit sed do eiusmod tempor incididunt simply dolore magna.")

    # Contact Details
    phone_title = models.CharField(max_length=100, default="Have any question?")
    phone_number = models.CharField(max_length=20, default="+92 (020)-9850")
    email_title = models.CharField(max_length=100, default="Write email")
    email_address = models.EmailField(default="needhelp@company.com")
    address_title = models.CharField(max_length=100, default="Visit anytime")
    address = models.CharField(max_length=200, default="66 broklyn golden street. New York")

    # Google Map Embed URL
    google_map_embed_url = models.TextField(default="https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=en&amp;q=1%20Grafton%20Street,%20Dublin,%20Ireland+(My%20Business%20Name)&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed")

    def __str__(self):
        return "Contact Page Content"
    
# faq-section
from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question

class FAQPage(models.Model):
    title = models.CharField(max_length=200, default="Frequently Asked Questions")
    description = models.TextField(default="Lorem ipsum is simply free text used by copytyping refreshing.")

    def __str__(self):
        return self.title
    
#slider-section
from django.db import models


class CustomersPageSettings(models.Model):
    background_image = models.ImageField(upload_to='clients/', default='images/background/page-title.jpg', help_text="1600 x 364 px")
    page_title = models.CharField(max_length=200, default="Customers")

    def __str__(self):
        return "Customers Content"


class Client(models.Model):
    INTERNATIONAL = 'international'
    LOCAL = 'local'
    COMPANY_TYPE_CHOICES = [
        (INTERNATIONAL, 'International Company'),
        (LOCAL, 'Local Company'),
    ]

    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/logos/', help_text="95 x 125 px")
    link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    company_type = models.CharField(max_length=20, choices=COMPANY_TYPE_CHOICES, default=LOCAL)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
    

# INDEX.HTML
class HomePageContent(models.Model):
    # Banner Section
    banner_badge_title = models.CharField(max_length=100, default='TRUSTED BY')
    banner_badge_count = models.IntegerField(default=10)
    banner_badge_text = models.CharField(max_length=100, default='Fast and Reliable Shipping')
    banner_main_title = models.CharField(max_length=200, default='Transport Solution 24/7')
    banner_subtitle = models.TextField(default='We strongly support best practice sharing across our operations around the world and across various')
    banner_background_image = models.ImageField(upload_to='homepage/banner/', help_text="1600 x 960 px")
    banner_button_text = models.CharField(max_length=100, default='Request A Quote')

    # About Section
    about_subtitle = models.CharField(max_length=100, default='Who we are')
    about_title = models.CharField(max_length=200, default='We Provide Full Range Logistics Solution')
    about_description = models.TextField(default='Our operations around the world and across various transporation sectors.')
    about_experience_years = models.IntegerField(default=25)
    about_experience_description = models.TextField(default='With over four decades of experience providing solutions to large-scale enterprises throughout the globe we offer end-to-end logistics.')
    
    about_checkmark_1 = models.CharField(max_length=200, default='With over four decades of experience')
    about_checkmark_2 = models.CharField(max_length=200, default='Every pleasure is to be welcomed and every pain')
    about_checkmark_3 = models.CharField(max_length=200, default='Velit esse cillum dolore eu fugiat nulla pariatur')
    
    about_image_1 = models.ImageField(upload_to='homepage/about/', help_text="432 x 605 px")
    about_image_2 = models.ImageField(upload_to='homepage/about/', help_text="410 x 260 px")


     # Call to Action Section
    cta_title = models.CharField(max_length=200, default='Logistics & Cargo For Business')
    cta_background_image = models.ImageField(upload_to='homepage/cta/', help_text="1170 x 332 px")
    cta_video_url = models.URLField(blank=True, null=True)
    cta_image_man = models.ImageField(upload_to='homepage/cta/', default='images/resource/why-choose3-1.png', help_text="265 x 296 px")

    # Why Choose Us Section
    shape_image = models.ImageField(upload_to='images/icons/', default='images/icons/shape-1.png', help_text="615 x 512 px")
    why_choose_subtitle = models.CharField(max_length=100, default='WHY CHOOSE US')
    why_choose_title = models.CharField(max_length=200, default='We create opportunity to reach potential')
    why_choose_description = models.TextField(default='There are many variations of passages of available but majority have suffered alteration in some form.')


    feature_block_one_title = models.CharField(max_length=100, default='Safety and Reliability')
    feature_block_one_text = models.TextField(default='Aenean placerat ut lacus nec pulvinar. Donce eu leo ante at commodo diam dolor sit amet')

    feature_block_two_title = models.CharField(max_length=100, default='Shipping Worldwide')
    feature_block_two_text = models.TextField(default='Aenean placerat ut lacus nec pulvinar. Donce eu leo ante at commodo diam dolor sit amet')

    why_choose_image = models.ImageField(upload_to='images/resource/', default='images/resource/why-choose3-1.png', help_text="738 x 653 px")
    badge_image = models.ImageField(upload_to='images/icons/', default='images/icons/badge.png', help_text="249 x 175 px")

    #Offer section
    offer_subtitle = models.CharField(max_length=100, default='SPECIAL LOGISTICS')
    offer_title = models.CharField(max_length=200, default='Best services for Businesses')
    offer_description = models.TextField(default='There are many variations of passages of Lorem Ipsum available, but the majority have readable content suffered alteration in some form')
    
    list_item_1 = models.CharField(max_length=200, default='Urgent transport solutions')
    list_item_2 = models.CharField(max_length=200, default='Top quality services with reasonable price')
    list_item_3 = models.CharField(max_length=200, default='Reliable & experienced staffs')

    button_text = models.CharField(max_length=50, default='Explore More')

    offer_image = models.ImageField(upload_to='images/resource/', default='images/resource/offer-img-1.jpg', help_text="1000 x 654 px")

    counter_title = models.CharField(max_length=100, default='Trusted by')
    counter_value = models.IntegerField(default=4890)

    caption_title = models.CharField(max_length=200, default='Moving Your Products accross border')


    def __str__(self):
        return "Home Page Content"
    

#site-settings
class SiteSettings(models.Model):
    title = models.CharField(max_length=150, help_text="Website title")
    favicon = models.ImageField(upload_to='favicons/', help_text="Upload favicon image - 32 x 32 px", default='images/favicon.png')
    description = models.CharField(max_length=200, help_text="Add your site description here (150-160 characters optimal)", blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, help_text="Comma-separated keywords for SEO", blank=True, null=True)

    def __str__(self):
        return self.title
