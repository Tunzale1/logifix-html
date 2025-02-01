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