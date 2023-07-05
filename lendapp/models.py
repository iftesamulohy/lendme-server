from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="upload")
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Category"
class Location(models.Model):
    area_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="upload")
    def __str__(self):
        return f"{self.area_name}"
    class Meta:
        verbose_name = "Location"
class ProductGallery(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="upload")
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Product Gallery"
class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    free_days = models.IntegerField()
    rental_charge = models.IntegerField()
    CHOICE_OPTION1 = 'Free'
    CHOICE_OPTION2 = 'Lended'
    

    CHOICES = [
        (CHOICE_OPTION1, 'Free'),
        (CHOICE_OPTION2, 'Lended'),
        
    ]
    status =  models.CharField(max_length=20, choices=CHOICES)
    CHOICE_OPTION3 = 'Featured'
    CHOICE_OPTION4 = 'Latest'
    

    CHOICES2 = [
        (CHOICE_OPTION3, 'Featured'),
        (CHOICE_OPTION4, 'Latest'),
        
    ]
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    tag = models.CharField(max_length=20, choices=CHOICES2)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True,blank=True)
    product_image = models.ManyToManyField(ProductGallery)
    address = models.TextField()
    phone_no = models.CharField(max_length=18)
    email = models.EmailField()
    website = models.URLField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    linkedin = models.URLField(null=True,blank=True)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "All Item"
class LendProduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    item = models.ForeignKey(Item,on_delete=models.CASCADE,null=True,blank=True)
    CHOICE_OPTION1 = 'Recieved'
    CHOICE_OPTION2 = 'Back'
    

    CHOICES = [
        (CHOICE_OPTION1, 'Recieved'),
        (CHOICE_OPTION2, 'Back'),
        
    ]
    status =  models.CharField(max_length=20, choices=CHOICES)
    date = models.DateField(null=True,blank=True)
    def __str__(self):
        return f"{self.user.username}"
    class Meta:
        verbose_name = "Product Lending"
class Keyword(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    keyword = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.user.username}"
    class Meta:
        verbose_name = "Keywords"