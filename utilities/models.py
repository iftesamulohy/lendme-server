from django.db import models
from solo.models import SingletonModel
from fontawesome_5.fields import IconField
from django.contrib.auth.models import User
# Create your models here.

class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    def __str__(self):
        return f"{self.question}"
    class Meta:
        verbose_name = "Faqs"

class Terms(SingletonModel):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Terms & Conditions"
class Privacy(SingletonModel):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Privacy Policies"

class Button(models.Model):
    text = models.CharField(max_length=200)
    url = models.URLField()
    icon = IconField()
    def __str__(self):
        return f"{self.text}"
    class Meta:
        verbose_name = "Button"
class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="upload")
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Images"
class Card(models.Model):
    title = models.CharField(max_length=200)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,null=True,blank=True)
    text = models.TextField(max_length=500)
    icon = IconField()
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Cards"
class SliderItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,null=True,blank=True)
    text = models.TextField(max_length=500)
    button = models.ManyToManyField(Button)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Slider Items"
class Slider(models.Model):
    title = models.CharField(max_length=200)
    slider_item = models.ManyToManyField(SliderItem)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Slider"
class Video(models.Model):
    title = models.CharField(max_length=200)
    slider_item = models.FileField(upload_to='upload/')
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Video"
class Reviews(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    rating_star = models.IntegerField()
    rating_text = models.TextField()
    def __str__(self):
        return f"{self.user}"
class TeamSingle(models.Model):
    name= models.CharField(max_length=100)
    button = models.ManyToManyField(Button,blank=True,null=True)
    text = models.TextField(blank=True,null=True)
    def __str__(self):
        return f"{self.name}"

class Utilities(SingletonModel):
    site_name = models.CharField(max_length=200)
    site_logo = models.ImageField(upload_to="upload/")
    favicon = models.ImageField(upload_to="upload/")
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    menu = models.TextField(null=True,blank=True)
    social = models.ManyToManyField(Button)
    def __str__(self):
        return f"{self.site_name}"
    class Meta:
        verbose_name = "Utilities"
#################################
#Page Models
#################################

class Aboutus(models.Model):
    section_title = models.CharField(max_length=100,null=True)
    slider = models.ManyToManyField(Slider,blank=True,null=True)
    image = models.ManyToManyField(Image,blank=True,null=True)
    button = models.ManyToManyField(Button,blank=True,null=True)
    text = models.TextField(blank=True,null=True)
    card = models.ManyToManyField(Card,blank=True,null=True)
    video = models.ManyToManyField(Video,blank=True,null=True)
    def __str__(self):
        return f"{self.section_title}"
    class Meta:
        verbose_name = "About Us"
class Home(models.Model):
    section_title = models.CharField(max_length=100,null=True)
    slider = models.ManyToManyField(Slider,blank=True,null=True)
    image = models.ManyToManyField(Image,blank=True,null=True)
    button = models.ManyToManyField(Button,blank=True,null=True)
    text = models.TextField(blank=True,null=True)
    card = models.ManyToManyField(Card,blank=True,null=True)
    video = models.ManyToManyField(Video,blank=True,null=True)
    def __str__(self):
        return f"{self.section_title}"
    class Meta:
        verbose_name = "Home"
class Services(models.Model):
    section_title = models.CharField(max_length=100,null=True)
    slider = models.ManyToManyField(Slider,blank=True,null=True)
    image = models.ManyToManyField(Image,blank=True,null=True)
    button = models.ManyToManyField(Button,blank=True,null=True)
    text = models.TextField(blank=True,null=True)
    card = models.ManyToManyField(Card,blank=True,null=True)
    video = models.ManyToManyField(Video,blank=True,null=True)
    def __str__(self):
        return f"{self.section_title}"
    class Meta:
        verbose_name = "Services"
class Testimonials(models.Model):
    section_title = models.CharField(max_length=100,null=True)
    slider = models.ManyToManyField(Slider,blank=True,null=True)
    image = models.ManyToManyField(Image,blank=True,null=True)
    button = models.ManyToManyField(Button,blank=True,null=True)
    text = models.TextField(blank=True,null=True)
    card = models.ManyToManyField(Card,blank=True,null=True)
    video = models.ManyToManyField(Video,blank=True,null=True)
    def __str__(self):
        return f"{self.section_title}"
    class Meta:
        verbose_name = "Testimonials"
class Teams(models.Model):
    section_title = models.CharField(max_length=100,null=True)
    slider = models.ManyToManyField(Slider,blank=True,null=True)
    image = models.ManyToManyField(Image,blank=True,null=True)
    button = models.ManyToManyField(Button,blank=True,null=True)
    text = models.TextField(blank=True,null=True)
    card = models.ManyToManyField(Card,blank=True,null=True)
    video = models.ManyToManyField(Video,blank=True,null=True)
    def __str__(self):
        return f"{self.section_title}"
    class Meta:
        verbose_name = "Teams"


########################
