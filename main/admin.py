from django.contrib import admin
from .models import Property, Consultation, Reservation, UserProfile, Institute, Amenity, PropertyInstitute, PropertyImage, RoomType, Food, Testimonials

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class RoomTypeInline(admin.TabularInline):
    model = RoomType
    extra = 1

class PropertyInstituteInline(admin.TabularInline):
    model = PropertyInstitute
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'locality', 'property_type', 'contact_name', 'contact_number')
    inlines = [PropertyImageInline, RoomTypeInline, PropertyInstituteInline]

class InstituteAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'institute', 'get_email', 'whatsapp_no', 'dob', 'gender', 'fathers_name', 'mothers_name', 'course', 'semester', 'address']
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'

admin.site.register(Testimonials)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Food)
admin.site.register(Institute, InstituteAdmin)
admin.site.register(Amenity)
admin.site.register(PropertyInstitute)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Consultation)
admin.site.register(Reservation)
