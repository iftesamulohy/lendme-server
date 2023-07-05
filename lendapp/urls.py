from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(),name="index"),
    path("about", views.About.as_view(),name="about"),
    path("add-listing", views.Addlisting.as_view(),name="add-listing"),
    path("bookmarks", views.Bookmarks.as_view(),name="bookmarks"),
    path("categories", views.Categories.as_view(),name="categories"),
    path("contact", views.Contact.as_view(),name="contact"),
    path("dashboard", views.Dashboard.as_view(),name="dashboard"),
    path("404", views.Error404.as_view(),name="404"),
    path("500", views.Error500.as_view(),name="500"),
    path("faq", views.Faq.as_view(),name="faq"),
    path("forgot-password", views.ForgotPass.as_view(),name="forgot-password"),
    path("gallery", views.Gallery.as_view(),name="gallery"),
    path("howitworks", views.HowWorks.as_view(),name="howitworks"),
    path("login", views.Login.as_view(),name="login"),
    path("my-listing", views.MyListing.as_view(),name="my-listing"),
    path("my-lending", views.MyLending.as_view(),name="my-lending"),
    path("pricing", views.Pricing.as_view(),name="pricing"),
    path("privacy-policy", views.PrivacyPolicy.as_view(),name="privacy"),
    path("profile", views.Profile.as_view(),name="profile"),
    path("reviews", views.Reviews.as_view(),name="reviews"),
    path("service-details", views.ServiceDetails.as_view(),name="service"),
    path("signup", views.Signup.as_view(),name="signup"),
    path("terms-conditions", views.Terms.as_view(),name="terms"),
    path("posts/<int:id>",views.ServiceDetails.as_view(),name="post-detail-page"),
    path('logout/', views.logout_view, name='logout'),
    path('category/<int:category_id>/', views.ProductByCategoryView.as_view(), name='product_by_category'),
]

