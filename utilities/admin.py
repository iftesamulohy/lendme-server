from django.contrib import admin
from .models import Aboutus, Button, Faq, Home, Image, Reviews, Services, Slider, SliderItem, TeamSingle, Teams,Terms,Privacy,Card, Testimonials, Utilities, Video
from django import forms
from ckeditor.widgets import CKEditorWidget
from solo.admin import SingletonModelAdmin
from fontawesome_5.widgets import IconWidget

# Register your models here.
class IconAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Card
        fields = '__all__'
        widgets = {
            'icon': IconWidget(),
        }
class IconAdminForm2(forms.ModelForm):
   
    class Meta:
        model = Card
        fields = '__all__'
        widgets = {
            'icon': IconWidget(),
        }

class MyModelAdminForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget())

    class Meta:
        models = [Faq,]
        fields = '__all__'

class MyModelMenuAdminForm(forms.ModelForm):
    menu = forms.CharField(widget=CKEditorWidget())

    class Meta:
        models = [Utilities]
        fields = '__all__'

class MyModelAdminForm2(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        models = [Terms,Privacy]
        fields = '__all__'



class FaqAdmin(admin.ModelAdmin):
    form = MyModelAdminForm
admin.site.register(Faq,FaqAdmin)
@admin.register(Terms)
class TermsAdmin(SingletonModelAdmin):
    list_display = ['title']
    form = MyModelAdminForm2
@admin.register(Privacy)
class PrivacyAdmin(SingletonModelAdmin):
    list_display = ['title']
    form = MyModelAdminForm2
@admin.register(Image)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Card)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['title']
    form = IconAdminForm

@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ['text']
    form = IconAdminForm2
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(SliderItem)
class SliderItemAdmin(admin.ModelAdmin):
    list_display = ['title']
    form = MyModelAdminForm2
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(Aboutus)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['section_title']
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['section_title']
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['section_title']
@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['section_title']
@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ['section_title']
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(TeamSingle)
class TeamSingleAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Utilities)
class UtilitiesAdmin(SingletonModelAdmin):
    list_display = ['site_name']
    
