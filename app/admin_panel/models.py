from django.db import models
from django.utils.text import slugify

# service-details
class Service(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# footer-section
class FooterLogo(models.Model):
    logo = models.ImageField(upload_to='footer/logo/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Footer Logo"


class FooterContactInfo(models.Model):
    phone_icon = models.CharField(max_length=50, default="lnr lnr-icon-phone-handset")
    phone_title = models.CharField(max_length=100, default="Call Us On")
    phone_number = models.CharField(max_length=20)

    email_icon = models.CharField(max_length=50, default="lnr lnr-icon-envelope1")
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
    links = models.JSONField(default=list)  # Example: [{"name": "Air Freight", "url": "/services/air-freight/"}, ...]

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

    def __str__(self):
        return "Header Top Info"

class HeaderLogo(models.Model):
    logo = models.ImageField(upload_to='header/logo/')
    logo_alt_text = models.CharField(max_length=100, default="Logifix")
    logo_link = models.URLField(default="/")  # Default to home page

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
    email = models.EmailField(default="info@example.com")
    working_hours = models.CharField(max_length=100, default="Mon - Sat 8:00 - 6:30, Sunday - CLOSED")

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
    
    image_1 = models.ImageField(upload_to='about/')
    image_2 = models.ImageField(upload_to='about/')
    logo_image = models.ImageField(upload_to='about/')

    def __str__(self):
        return "About Main Section"

class AboutCounter(models.Model):
    distribution_centers = models.IntegerField(default=541)
    years_experience = models.IntegerField(default=35)
    countries_regions = models.IntegerField(default=147)

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