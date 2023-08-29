from .views import *
from django.urls import path
from .sitemaps import PostSitemap
from django.contrib.sitemaps.views import sitemap



sitemaps = {
    'blog': PostSitemap
}



urlpatterns = [
    path('', BlogList, name='home'),
    path('<slug:slug>/', blog_detail, name='blog_detail'),
    path('ckeditor/new_post/', CreateBlogPost, name='create'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('about',  about, name='about'),
    path('contact', contact, name='contact'),
]
