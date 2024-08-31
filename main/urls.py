from django.urls import path, include
from . import views
# in urls.py
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PropertySitemap
from django.views.generic import TemplateView


sitemaps = {
    'properties': PropertySitemap,
}

urlpatterns = [
     path('', views.home, name='home'),
     path('reserve/<int:property_id>/', views.reserve_property, name='reserve_property'),
     path('my-reservations/', views.my_reservations, name='my_reservations'),
     path('property/<int:pk>/', views.property_detail, name='property_detail'),
     path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
     path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
     path('explore/properties', views.explore, name='explore'),

]
