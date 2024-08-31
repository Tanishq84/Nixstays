from django.contrib.sitemaps import Sitemap
from .models import Property
from django.conf import settings
class PropertySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Property.objects.all()

    def location(self, item):
        return f"/property/{item.id}/"

    def lastmod(self, obj):
        return obj.updated_at  # Ensure you have a field for the last modified date in your Property model
