from django.urls import path
from utilities import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'faqs',views.FaqViews,basename="faqs")
router.register(r'terms',views.TermsViews,basename="terms")
router.register(r'privacy',views.PrivacyViews,basename="privacy")
router.register(r'about-us',views.AboutViews,basename="about-us")

router.register(r'index',views.HomeViews,basename="index")
router.register(r'services',views.ServiceViews,basename="services")
router.register(r'testimonials',views.TestimonialsViews,basename="testimonials")
router.register(r'teams',views.TeamViews,basename="teams")
router.register(r'util',views.UtilitiesViews,basename="util")
router.register(r'user',views.Userme,basename="user")
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',views.RegisterUser.as_view()),
    
]
urlpatterns+= router.urls