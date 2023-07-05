from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User, auth
import requests
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from lendapp.models import Category, Item, Keyword, LendProduct, Location, ProductGallery
from datetime import date
from django.contrib.auth import logout
from django.views.generic import ListView
# Create your views here.
site_url = 'http://192.168.31.163:8000'
def handle_uploaded_file(f):  
    with open(f'upload/{f}', 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 
class Index(TemplateView):
    template_name = "lendapp/index-2.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured'] = Item.objects.filter(tag="Featured",status='Free')
        context['latests'] = Item.objects.filter(tag="Latest",status='Free')
        context['categories'] = Category.objects.all()
        context['locations'] = Location.objects.all()
        context['images'] = ProductGallery.objects.all()
        try:
            search_category = Keyword.objects.filter(user = self.request.user).last()
            context['recomends'] = Item.objects.filter(category__name=search_category.keyword,status='Free')
        except:
            return context
        return context
    def post(self, request, *args, **kwargs):
        search = request.POST['search']
        item = Category.objects.get(name=search)
        Keyword.objects.create(
            user = self.request.user,
            keyword = search
            )
        return redirect('category/'+str(item.id)+'/')
class About(TemplateView):
    template_name = "lendapp/about.html"
class Addlisting(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = "lendapp/add-listing.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['locations'] = Location.objects.all()
        context['images'] = ProductGallery.objects.all()
        print(Item.objects.filter(tag="Featured"))
        print(site_url)
        return context
    def post(self, request, *args, **kwargs):
        title = request.POST['title']
        description = request.POST['description']
        freedays = request.POST.get('freedays')
        rentalcharge = request.POST.get('rentalcharge')
        category = request.POST.get('category')
        location = request.POST.get('area')
        address = request.POST.get('address')
        phoneno = request.POST.get('phone')
        email = request.POST.get('email')
        website = request.POST.get('website')
        facebook = request.POST.get('facebook')
        twitter = request.POST.get('twitter')
        instagram = request.POST.get('instagram')
        linkedin = request.POST.get('linkedin')
        images = request.FILES.getlist('image[]')
        id_list=[]
        print(title,description,freedays,rentalcharge,category,location,address,phoneno,email,website,facebook,twitter,instagram,linkedin)
        print(images)
        for image in images:
            img_id = ProductGallery.objects.create(
                name = image.name,
                image = image
                )
            id_list.append(img_id.id)

        post = Item.objects.create(
            user = request.user,
            title = title,
            description = description,
            free_days = freedays,
            rental_charge = rentalcharge,
            status = 'Free',
            category= Category.objects.get(name=category),
            address = address,
            location = Location.objects.get(area_name=location),
            phone_no = phoneno,
            email = email,
            website = website,
            facebook = facebook,
            instagram = instagram,
            linkedin = linkedin,
            

            )
        Item.objects.get(title=title).product_image.set(id_list)
        print(id_list)
        
        return redirect('add-listing')
class Bookmarks(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = "lendapp/bookmarks.html"
class Categories(TemplateView):
    template_name = "lendapp/categories.html"
class Contact(TemplateView):
    template_name = "lendapp/contact.html"
class Dashboard(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = "lendapp/dashboard.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = "dasboard"
        return context
class Error404(TemplateView):
    template_name = "lendapp/error-404.html"
class Error500(TemplateView):
    template_name = "lendapp/error-500.html"
class Faq(TemplateView):
    template_name = "lendapp/faq.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faqs'] = requests.get(site_url+'/utilities/faqs/').json()
        return context

class ForgotPass(TemplateView):
    template_name = "lendapp/forgot-password.html"
class Gallery(TemplateView):
    template_name = "lendapp/gallery.html"
class HowWorks(TemplateView):
    template_name = "lendapp/howitworks.html"
class Login(TemplateView):
    template_name = "lendapp/login.html"
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('login')
class MyListing(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = "lendapp/my-listing.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.filter(user=self.request.user)
        context['status'] = "listing"
        return context
class MyLending(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = "lendapp/my-lending.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = LendProduct.objects.filter(user=self.request.user)
        context['status'] = "lending"
        return context
class Pricing(TemplateView):
    template_name = "lendapp/pricing.html"
class PrivacyPolicy(TemplateView):
    template_name = "lendapp/privacy-policy.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['privacy'] = requests.get(site_url+'/utilities/privacy/').json()
        return context

class Profile(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = "lendapp/profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = "profile"
        return context
class Reviews(TemplateView):
    template_name = "lendapp/reviews.html"
class ServiceDetails(TemplateView):
    template_name = "lendapp/service-details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('id')
        context['data'] = Item.objects.get(id=id)
        return context
    def post(self, request, *args, **kwargs):
        post_id =  request.POST.get('id')
        LendProduct.objects.create(
            user= request.user,
            item = Item.objects.get(id=post_id),
            status = "Recieved",
            date = date.today()
            )
        return redirect('index')
class Signup(TemplateView):
    template_name = "lendapp/signup.html"
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        name= request.POST['name']
        username = email.split('@')[0]
        print(username)
        print(password)
        try:
            user = User.objects.get(username=username)
        except:
            user= None
        print(user)
        if user is None:
            User.objects.create(
                first_name = name,
                email = email,
                username = username,
                password = password
                )
            return redirect('login')
        else:
             return redirect('signup')
        #return redirect('signup')
class Terms(TemplateView):
    template_name = "lendapp/terms-condition.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['terms'] = requests.get(site_url+'/utilities/terms/').json()
        return context

class ProductByCategoryView(ListView):
    model = Item
    template_name = 'lendapp/listing-grid.html'
    context_object_name = 'items'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Item.objects.filter(category_id=category_id)
#logout
def logout_view(request):
    logout(request)
    # Redirect to a specific URL after logout
    return redirect('index')  # Replace 'home' with the desired URL name or path