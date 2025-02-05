from django.db import models
from django.utils.text import slugify

# service-details
class Service(models.Model):
    services_page_title =  models.CharField(max_length=200, default="Services")  
    services_background_image =  models.ImageField(upload_to='services/', default='images/background/page-title.jpg')
    slug = models.SlugField(unique=True, blank=True)
    icon_class = models.CharField(max_length=50, default="flaticon-team")
    title = models.CharField(max_length=200, default="Safety and Reliability")
    text_1 = models.CharField(max_length=200, default="Worldwide service")
    text_2 = models.CharField(max_length=200, default="24/7 Support")
    image = models.ImageField(upload_to='services/')
    
    service_details_background_image = models.ImageField(upload_to='services/details', default='images/background/page-title.jpg')
    overview_title = models.CharField(max_length=200, default="Service Overview")
    overview = models.TextField(default="Lorem ipsum is simply free text used by copytyping refreshing...")
    center_title = models.CharField(max_length=200, default="Service Center")
    service_center_text = models.TextField(default="Lorem ipsum is simply free text used by copytyping refreshing...")
    service_image_1 = models.ImageField(upload_to='services/details/', blank=True, null=True)
    service_image_2 = models.ImageField(upload_to='services/details/', blank=True, null=True)
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
    logo = models.ImageField(upload_to='footer/logo/')

    def __str__(self):
        return "Footer Logo"


class FooterContactInfo(models.Model):
    background_image = models.ImageField(upload_to='footer/logo/', default='images/icons/footer-bg.png')
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

    def __str__(self):
        return "Header Top Info"

class HeaderLogo(models.Model):
    logo = models.ImageField(upload_to='header/logo/')
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
    background_image = models.ImageField(upload_to='about/hero/')

    def __str__(self):
        return "About Page Hero Section"

class AboutSection(models.Model):
    subtitle = models.CharField(max_length=100, default="WHO WE ARE")
    title = models.CharField(max_length=200)
    description = models.TextField()
    years_experience = models.IntegerField(default=25)
    button_text = models.CharField(max_length=200, default="Explore more")
    
    image_1 = models.ImageField(upload_to='about/')
    image_2 = models.ImageField(upload_to='about/')
    logo_image = models.ImageField(upload_to='about/')

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
    subtitle = models.CharField(max_length=100, default="Why select us")
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
    title = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.title



#contact-page
class ContactPage(models.Model):
    # Hero Section
    hero_title = models.CharField(max_length=200, default="Contact Us")
    hero_background_image = models.ImageField(upload_to='contact/hero/')

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
        return "FAQ Page Content"
    
#slider-section
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/logos/')
    link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

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
    banner_background_image = models.ImageField(upload_to='homepage/banner/')
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
    
    about_image_1 = models.ImageField(upload_to='homepage/about/')
    about_image_2 = models.ImageField(upload_to='homepage/about/')


     # Call to Action Section
    cta_title = models.CharField(max_length=200, default='Logistics & Cargo For Business')
    cta_background_image = models.ImageField(upload_to='homepage/cta/')
    cta_video_url = models.URLField(blank=True, null=True)
    cta_image_man = models.ImageField(upload_to='homepage/cta/', default='images/resource/why-choose3-1.png')

    # Why Choose Us Section
    shape_image = models.ImageField(upload_to='images/icons/', default='images/icons/shape-1.png')
    why_choose_subtitle = models.CharField(max_length=100, default='WHY CHOOSE US')
    why_choose_title = models.CharField(max_length=200, default='We create opportunity to reach potential')
    why_choose_description = models.TextField(default='There are many variations of passages of available but majority have suffered alteration in some form.')


    feature_block_one_title = models.CharField(max_length=100, default='Safety and Reliability')
    feature_block_one_text = models.TextField(default='Aenean placerat ut lacus nec pulvinar. Donce eu leo ante at commodo diam dolor sit amet')

    feature_block_two_title = models.CharField(max_length=100, default='Shipping Worldwide')
    feature_block_two_text = models.TextField(default='Aenean placerat ut lacus nec pulvinar. Donce eu leo ante at commodo diam dolor sit amet')

    why_choose_image = models.ImageField(upload_to='images/resource/', default='images/resource/why-choose3-1.png')
    badge_image = models.ImageField(upload_to='images/icons/', default='images/icons/badge.png')

    #Offer section
    offer_subtitle = models.CharField(max_length=100, default='SPECIAL LOGISTICS')
    offer_title = models.CharField(max_length=200, default='Best services for Businesses')
    offer_description = models.TextField(default='There are many variations of passages of Lorem Ipsum available, but the majority have readable content suffered alteration in some form')
    
    list_item_1 = models.CharField(max_length=200, default='Urgent transport solutions')
    list_item_2 = models.CharField(max_length=200, default='Top quality services with reasonable price')
    list_item_3 = models.CharField(max_length=200, default='Reliable & experienced staffs')

    button_text = models.CharField(max_length=50, default='Explore More')

    offer_image = models.ImageField(upload_to='images/resource/', default='images/resource/offer-img-1.jpg')

    counter_title = models.CharField(max_length=100, default='Trusted by')
    counter_value = models.IntegerField(default=4890)

    caption_title = models.CharField(max_length=200, default='Moving Your Products accross border')


    def __str__(self):
        return "Home Page Content"
    

#site-settings
class SiteSettings(models.Model):
    title = models.CharField(max_length=150, help_text="Website title")
    favicon = models.ImageField(upload_to='favicons/', help_text="Upload favicon image", default='images/favicon.png')
    description = models.CharField(max_length=200, help_text="Add your site description here (150-160 characters optimal)", blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, help_text="Comma-separated keywords for SEO", blank=True, null=True)

    def __str__(self):
        return self.title
